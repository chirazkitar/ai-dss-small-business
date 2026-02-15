from flask import Flask, request, jsonify
from src.predict import predict

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def make_prediction():
    try:
        data = request.get_json()
        result = predict(data)
        return jsonify({"predicted_revenue": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
