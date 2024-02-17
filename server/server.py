
from flask import Flask, jsonify, request
import requests
from flask_cors import CORS
import cohere

co = cohere.Client('QwHQXqOQgLg0Sjv9aUKt5wVBVazIC6KqWlGnd2yw')




app = Flask(__name__)
CORS(app)




@app.route("/api/home", methods=["GET"])
def return_home():
  return jsonify({
    'message': "Hi this is my app",
    'categories': ['Heading', 'Definitions', 'Formulas'],
    'output': intro_paragraph
  })



@app.route("/api/upload", methods=["POST"])
def upload():
  file = request.files['file']
  
  content = file.read()

  print(content)




@app.route("/api/cohere", methods=["GET"])
def return_cohere():
  
  message = upload()
  response = co.chat(
    model='command-nightly',
    message=message,
  )
  intro_paragraph = response.text
  return intro_paragraph
  
if __name__ == "__main__":
  app.run(debug=True,port=8080)

