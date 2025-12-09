# from typing import Dict, List, Optional
from flask import Flask, request, jsonify
import pathlib
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
thisdir = pathlib.Path(__file__).parent.absolute() # path to directory of this file

def load_imgs():
	try:
		return json.loads(thisdir.joinpath('img_db.json').read_text())
	except:
		return []
	
def save_imgs(img_db):
	thisdir.joinpath('img_db.json').write_text(json.dumps(img_db, indent=4))

def update_curr(curr_img):
	img_db = load_imgs()
	img_db["curr_img"] = curr_img
	save_imgs(img_db)
	return {"curr_img": img_db['curr_img']}

def add_to_log(log_img):
	img_db = load_imgs()
	img_db["log"].append(log_img)
	save_imgs(img_db)
	return {"log": img_db["log"]}



@app.route('/curr_img', methods=['POST'])
def post_curr():
	curr_img = request.get_json()
	curr_saved = update_curr(curr_img["new_img"])
	res = jsonify(curr_saved)
	res.status_code = 200
	return res


@app.route("/curr_img", methods=["GET"])
def get_curr():
	img_db = load_imgs()
	res = jsonify( { "curr_img": img_db["curr_img"] } )
	res.status_code = 200
	return res

@app.route("/log_img", methods=["POST"])
def post_log():
	add_img = request.get_json()
	curr_saved = add_to_log(add_img["new_img"])
	res = jsonify(curr_saved)
	res.status_code = 200
	return res

@app.route("/log_img", methods=["GET"])
def get_log():
	img_db = load_imgs()
	res = jsonify( { "log": img_db["log"] } )
	res.status_code = 200
	return res

if __name__ == '__main__':
    app.run(port=5000, debug=True)