from flask import Flask, render_template, request, jsonify

from internalAgentchat import get_response

agent2 = Flask(__name__)

@agent2.get("/")
def index_get():
    return render_template("Internel.html")


@agent2.post("/predict")
def predict():
    text = request.get_json().get("message")
    #todo check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ =="__main__":
    agent2.run(debug=True)

@agent2.route("/")
def index():
    return render_template("base.html")

@agent2.route("/predict", methods=["POST"])
def predict():
    data = request.json
    message = data.get("message")

    if not message:
        return jsonify({"error": "Invalid input"}), 400

    response = get_response(message)
    return jsonify({"answer": response})

if __name__ == "__main__":
    agent2.run(debug=True,port=5020)
