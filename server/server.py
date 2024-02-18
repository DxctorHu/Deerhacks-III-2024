
from flask import Flask, jsonify, request
from flask_cors import CORS
import cohere
import PyPDF2
import os
from new import gist



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

  dates, definitions, examples, summary = gist(file_path)
  
  res = jsonify({
    'date': dates,
    'definition': definitions,
    'examples': examples,
    'summary': summary
  })
  res.headers.add("Access-Control-Allow-Origin", '*')
  return res



if __name__ == "__main__":
  app.run(debug=True,port=8080)

