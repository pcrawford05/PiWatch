from piWatchlib import send_image
import time
import socket
from camera import take_pic
import picamera

def main(HOST='127.0.0.1', PORT=65432, image_path='piwatch_photo.jpg'):
    # image_path = 'piwatch_photo.jpg'
    # HOST = '127.0.0.1'
    # PORT = 65432

    # Send image every second
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    while True:
        take_pic(camera)
        print("Trying to connect")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket created.")
        s.connect((HOST, PORT))
        print("Connected to socket!")
        # Read the image file in binary mode
        print("Reading image...")
        with open(image_path, 'rb') as f:
            image_data = f.read()
        print("Sending image...")
        s.sendall(image_data)
        print("Image sent successfully.")
        # send_image('image.jpg', '127.0.0.1', 65432)
        s.close()

        time.sleep(3)
    

if __name__ == "__main__":
    HOST = input("Enter the Computer address to connect to: ")
    main(HOST)
    