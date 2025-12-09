import picamera
from time import sleep
import os

def take_pic(camera):
	file_path = "./piwatch_photo.jpg"

	if os.path.isfile(file_path):
		os.remove(file_path)
		print("File deleted successfully.")

	print("Starting preview...")
	camera.start_preview()

	print("Taking image...")
	camera.capture('./piwatch_photo.jpg')

	camera.stop_preview()
	