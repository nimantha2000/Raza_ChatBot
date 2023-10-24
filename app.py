from flask import Flask, render_template, request, jsonify

from chat import get_response

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    #todo check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ =="__main__":
    app.run(debug=True)

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    message = data.get("message")

    if not message:
        return jsonify({"error": "Invalid input"}), 400

    response = get_response(message)
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(debug=True)
