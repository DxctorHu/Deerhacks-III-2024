
from flask import Flask, jsonify, request
from flask_cors import CORS
import cohere
import PyPDF2
import os

co = cohere.Client('QwHQXqOQgLg0Sjv9aUKt5wVBVazIC6KqWlGnd2yw')

app = Flask(__name__)
CORS(app)


@app.route("/api/home", methods=["GET"])
def return_home():
  return jsonify({
    'message': "Hi this is my app"
  })


UPLOAD_FOLDER = 'pdfuploads'
@app.route('/upload', methods=['POST','GET'])
def upload_file():
  file = request.files['file']
  req_msg = "error"
  if 'file' in request.files:
    req_msg="all good"
  
  unique_filename = 'info_pdf' + '.pdf'  # Generate the file name 
  file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
  file.save(file_path)  # Save the file with the unique filename
  print(req_msg)
  print(request.files)
  return jsonify({
    'msg': req_msg
  })

if __name__ == "__main__":
  app.run(debug=True,port=8080)

