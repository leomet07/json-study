# USAGE
# python ocr.py --image images/example_01.png 
# python ocr.py --image images/example_02.png  --preprocess blur

# import the necessary packages
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
import argparse
import cv2
import os


def recog(passedimg):
	# load the example image and convert it to grayscale
	image = passedimg
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	#cv2.imshow("Image", gray)

	

	# write the grayscale image to disk as a temporary file so we can
	# apply OCR to it
	

	# load the image as a PIL/Pillow image, apply OCR, and then delete
	# the temporary file
	text = pytesseract.image_to_string(Image.fromarray(gray))
	if text != "":
		#print(text)
		pass

	# show the output images
	# cv2.imshow("Image", image)
	return text
