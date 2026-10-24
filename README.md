# PiWatch

PiWatch is a Raspberry Pi security camera prototype that detects people and sends an alert with an annotated image. A Raspberry Pi 4B captures photos, a laptop runs YOLOv8n inference, and a React dashboard displays a log of detections.

**[Watch the demo](https://youtube.com/shorts/W8BkkR_2Nfc)** · [Read the project reflection](EE%20250%20Final%20Project%20Reflection.pdf)

## How it works

1. A Raspberry Pi 4B with a Camera Module 2 captures 640 × 480 JPEG images and sends them to a laptop over a TCP socket on the local network.
2. The laptop receives each image in 4 KB chunks and runs YOLOv8n to check for a person.
3. When a person is detected, PiWatch saves a timestamped annotated image, adds it to a log served by Flask, and posts the image to an n8n webhook. Our workflow sent the alert to Discord.
4. The React dashboard polls Flask for new detections and lets the user review saved images.

```text
Raspberry Pi + camera
        │ JPEG over TCP
        ▼
Laptop: socket receiver → YOLOv8n person detection
                            ├─→ Flask log → React dashboard
                            └─→ n8n webhook → Discord alert
```

The camera and inference run on separate devices because YOLO and OpenCV were too demanding for the Raspberry Pi setup we used. A delay between captures gives the laptop time to receive and process each image. The project stores a timestamped image only when a person is detected, rather than retaining every frame.

## Stack

- **Hardware:** Raspberry Pi 4B and Raspberry Pi Camera Module 2
- **Image transfer and detection:** Python TCP sockets, OpenCV, and Ultralytics YOLOv8n
- **Dashboard:** Flask API, React, Vite, and Bootstrap
- **Alerts:** n8n webhook connected to Discord in the original setup

## Run locally

This project uses the legacy `picamera` Python module on the Raspberry Pi. It requires a Raspberry Pi OS and camera configuration compatible with that module. The Pi and laptop must be on the same local network. Run the commands below from the repository root unless a step says otherwise.

### 1. Prepare the laptop

Install Python 3 and a Node.js version compatible with the project's Vite dependency (`20.19+` or `22.12+`), then install the laptop dependencies:

```bash
python3 -m pip install flask flask-cors requests ultralytics opencv-python
cd frontend
npm install
cd ..
```

The repository includes `yolov8n.pt`, which `yolo.py` loads for inference. The Flask server listens on port `5000`; the image receiver listens on port `65432`.

### 2. Prepare the Raspberry Pi

Connect and enable the Camera Module 2, confirm that `picamera` works on the Pi, and make sure Python 3 is available. The capture script expects `picamera` to be installed on the Pi.

### 3. Configure alerts

`piWatchlib.py` currently contains the webhook URL used for the original project. To receive your own alerts, replace `N8N_WEBHOOK_URL` in `send_alert()` with an n8n webhook that accepts a multipart image under the `file` field and routes it to your notification destination. Without a working workflow, image detection and the local dashboard can still run, but alert delivery will fail.

Images of detected people are sent to the configured webhook. Use a workflow and destination you control.

### 4. Start the system

Open separate laptop terminals in the repository root and start these in order:

```bash
python3 flaskServer.py
```

```bash
python3 computerListen.py
```

When `computerListen.py` prompts for the computer address, enter the laptop's local network IP address. Use an address the Raspberry Pi can reach, not `127.0.0.1`.

On the Raspberry Pi, run `piWatch.py` from a copy of the repository. When prompted, enter the **same laptop IP address**:

```bash
python3 piWatch.py
```

Finally, on the laptop, start the dashboard:

```bash
cd frontend
npm run dev
```

Open the local URL printed by Vite, usually `http://localhost:5173`. The dashboard shows the detection log. The capture loop waits three seconds after sending each image, with additional time spent capturing and processing it.

## Current scope

- The dashboard displays logged detections. The code also saves the latest annotated frame, but the current React interface does not display that continuously updated frame.
- Alerts depend on an external n8n workflow. The workflow configuration is not included in this repository.
- PiWatch is a course project prototype, not a production security system.

## Team

Built by Alex Frederic and Peyton Crawford for USC EE 250. The [project reflection](EE%20250%20Final%20Project%20Reflection.pdf) describes the implementation choices, experiments, and limitations in more detail.
