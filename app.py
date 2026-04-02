from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "service": "devsecops-demo",
        "status": "ok",
        "message": "Sample application showing CI-ready GitHub workflow patterns."
    })

@app.get("/health")
def health():
    return jsonify({"healthy": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
