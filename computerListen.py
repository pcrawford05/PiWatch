from piWatchlib import send_alert, log_image, current_time
import socket
from yolo import runInference
import cv2
import requests


def main(HOST = '127.0.0.1', PORT = 65432, image_path='./frontend/public/img/listenoutput.jpg'):
    # HOST = input("Enter the PiWatch address to connect to: ")
    # PORT = 65432 # input("Enter the port to connect to: ")
    # image_path = 'output.jpg' # input("Enter the path to save the received image: ")
    # Main while loop
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        while True:
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                # Receive the image data
                image_data = b''
                while True:
                    chunk = conn.recv(4096)  # Receive data in chunks
                    if not chunk:
                        break
                    image_data += chunk
                
                # Save the received image
                with open(image_path, 'wb') as f:
                    f.write(image_data)
                print(f"Image received and saved as '{image_path}'")

                # Run inference on image
                results = runInference(image_path)
                # Convert to image and save
                success, encoded = cv2.imencode(".jpg", results[0].plot())
                img_bytes = encoded.tobytes()

                annotated_path = './frontend/public/img/annotatedlistenoutput.jpg'
                with open(annotated_path, 'wb') as f:
                    f.write(img_bytes)
                print(f"Image annotated and saved as @{annotated_path}")

                # Refreshes the image on the flask server; probably unnecessary
                requests.post('http://localhost:5000/curr_img', json={"new_img": "img/annotatedlistenoutput.jpg"})

                # Check for humans in results
                human_detected = False
                objects = [int(x) for x in list(results[0].boxes.cls)]
                for x in objects:
                    if x == 0:
                        human_detected = True


                if(human_detected):
                    time_path = str(current_time()) + '.jpg'
                    send_alert(annotated_path)
                    log_image("img/" + time_path)

                    with open('./frontend/public/img/' + time_path, 'wb') as f:
                        f.write(img_bytes)

            

    
    

if __name__ == "__main__":
    HOST = input("Enter the Computer address to connect to: ")
    main(HOST)