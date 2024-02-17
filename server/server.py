from flask import Flask, jsonify 
from flask_cors import CORS
import cohere

co = cohere.Client('QwHQXqOQgLg0Sjv9aUKt5wVBVazIC6KqWlGnd2yw')

message = "what is this formula in latex: \sqrt{\sin ^2\left(-1\right)}\le \:1-\sin \left(x\right)"
response = co.chat(
  model='command-nightly',
  message=message,
)
intro_paragraph = response.text


app = Flask(__name__)
CORS(app)












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

