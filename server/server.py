
from flask import Flask, jsonify 
from flask_cors import CORS
import cohere
from db import get_database

co = cohere.Client('QwHQXqOQgLg0Sjv9aUKt5wVBVazIC6KqWlGnd2yw')

message = "Expand on the topic Basketball"
response = co.chat(
  model='command-nightly',
  message=message,
)
intro_paragraph = response.text


app = Flask(__name__)
CORS(app)



#get MDB cluster
dbname = get_database()
collection_name = dbname["info"]

new_info = {"header": "Another test"}
collection_name.insert_one("new_info")


@app.route('/')
def home():
  return 'test'

@app.route("/api/home", methods=["GET"])
def return_home():
  return jsonify({
    'message': "Hi this is my app",
    'categories': ['Heading', 'Definitions', 'Formulas'],
    'output': intro_paragraph
  })

@app.route("/api/cohere", methods=["GET"])
def return_cohere():
  return intro_paragraph



if __name__ == "__main__":
  app.run(debug=True,port=8080)

