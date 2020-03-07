import dlib
import openface
import cv2
import face_recognition
import face_recognition.face_recognition_cli as c
import os
import numpy as np

class Face_Recognition:
	def __init__(self):
		currentdir = os.getcwd()
		predictor_model = f"{currentdir}/models/shape_predictor_68_face_landmarks.dat"
		
		# Create a HOG face detector using the built-in dlib class
		self.face_detector = dlib.get_frontal_face_detector()
		self.face_pose_predictor = dlib.shape_predictor(predictor_model)
		self.face_aligner = openface.AlignDlib(predictor_model)
		
		path = f"{currentdir}/training/images/"
		self.known_names, self.known_face_encodings= c.scan_known_people(path)

	def rect_to_bb(self,rect):
		# take a bounding predicted by dlib and convert it
		# to the format (x, y, w, h) as we would normally do
		# with OpenCV
		x = rect.left()
		y = rect.top()
		w = rect.right() - x
		h = rect.bottom() - y
		return x, y, w, h

	def shape_to_np(self,shape, dtype="int"):
		# initialize the list of (x, y)-coordinates
		coords = np.zeros((68, 2), dtype=dtype)

		# loop over the 68 facial landmarks and convert them
		# to a 2-tuple of (x, y)-coordinates
		for i in range(0, 68):
			coords[i] = (shape.part(i).x, shape.part(i).y)

		# return the list of (x, y)-coordinates
		return coords

	def test_image(self,na):
		#unknown_image = face_recognition.load_image_file(na)
		unknown_image = na
		if unknown_image.shape[1] > 1600:
			scale_factor = 1600.0 / unknown_image.shape[1]
			unknown_image = scipy.misc.imresize(unknown_image, scale_factor)
		unknown_encodings = face_recognition.face_encodings(unknown_image)

		for unknown_encoding in unknown_encodings:
			result = face_recognition.compare_faces(self.known_face_encodings, unknown_encoding)
			if True in result:
				for is_match, name in zip(result, self.known_names):
					if is_match:
						return name;
			else:
				return "Unknown"

	def run(self,frame):
		self.frame = frame
		detected_faces = self.face_detector(self.frame, 1)
		# The 1 in the second argument indicates that we should upsample the image 1 time.  This will make everything bigger and allow us to detect more faces.
		color_scheme = (255,0,0)
		
		for i, face_rect in enumerate(detected_faces):
			x,y,w,h = self.rect_to_bb(face_rect)
			self.frame = cv2.rectangle(self.frame,(x,y),(x+w,y+h),color_scheme,2)

			pose_landmarks = self.face_pose_predictor(self.frame, face_rect)

			points = self.shape_to_np(pose_landmarks)
			
			for i in points:
				cv2.line(self.frame, tuple(i), tuple(i), color_scheme, 2)
			
			# Use openface to calculate and perform the face alignment
			alignedFace = self.face_aligner.align(534, self.frame, face_rect, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
			#nam = "aligned_face_{}.jpg".format(i)
			#cv2.imwrite("aligned_face_{}.jpg".format(i), alignedFace)
			name = self.test_image(alignedFace)

			if name == "none":
				name = "Unknown"
			if name == "Nabeel":
				name = "Threat"
				color_scheme = (0,0,255)
				
				x,y,w,h = self.rect_to_bb(face_rect)
				self.frame = cv2.rectangle(self.frame,(x,y),(x+w,y+h),color_scheme,2)

				pose_landmarks = self.face_pose_predictor(self.frame, face_rect)

				points = self.shape_to_np(pose_landmarks)
				print(len(points))
				"""for i in points:
					cv2.line(self.frame, tuple(i), tuple(i), color_scheme, 2)"""
				
				# Use openface to calculate and perform the face alignment
				alignedFace = self.face_aligner.align(534, self.frame, face_rect, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
				nam = "aligned_face_{}.jpg".format(i)
				name = self.test_image(nam)
				
			

			cv2.putText(self.frame, "{}".format(name), (x - 10, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, color_scheme, 2)
