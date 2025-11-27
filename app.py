from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "NovaMart service online for CIE set 71\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
