def send_alert(image_path):
    import requests

    N8N_WEBHOOK_URL = 'https://pcrawseesaw.app.n8n.cloud/webhook/send-sms-alert'

    print(f"Attempting to upload: {image_path}")

    # Open the file in binary mode
    with open(image_path, 'rb') as img_file:
        # 'file' is the key name n8n uses
        imgfile = {
            'file': (image_path, img_file, 'image/jpeg')
        }

        try: # Gemini wrote this entire error checking part when I asked to add image as a parameter
            # Send the POST request
            response = requests.post(N8N_WEBHOOK_URL, files=imgfile)
            
            # Check results
            if response.status_code == 200:
                print("✅ Success! Image sent to n8n.")
            else:
                print(f"⚠️ Failed with Status Code: {response.status_code}")
                print(f"Response: {response.text}")

        except requests.exceptions.ConnectionError:
            print(f"❌ Connection Refused. Is n8n running and listening on localhost:5678?")

def log_image(image_path):
    import requests
    requests.post('http://localhost:5000/log_img', json={"new_img": image_path})
    print(f"Logging image @{image_path}")

def current_time():
    import time
    return time.strftime("%Y%m%d-%H%M%S")

def send_image(image_path='image.jpg', HOST='172.20.10.5', PORT=65432):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        # Read the image file in binary mode
        with open(image_path, 'rb') as f:
            image_data = f.read()
        
        s.sendall(image_data)
        print("Image sent successfully.")