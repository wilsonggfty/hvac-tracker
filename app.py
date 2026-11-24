from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>HVAC Maintenance Tracker</h1><p>Built by Wilson</p>"

if __name__ == "__main__":
    app.run(debug=True)