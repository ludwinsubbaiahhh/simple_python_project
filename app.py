from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

with open("moods.json", "r") as f:
    mood_data = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-songs", methods=["POST"])
def get_songs():
    mood = request.json.get("mood", "").lower()
    songs = mood_data.get(mood, [])
    return jsonify({"songs": songs})

if __name__ == "__main__":
    app.run(debug=True)
