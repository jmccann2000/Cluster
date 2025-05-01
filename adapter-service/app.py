import json
import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests from frontend

@app.route('/recent-commands')
def recent_commands():
    log_path = '/app/logs/executed-commands.jsonl'  # inside Docker path

    if not os.path.exists(log_path):
        return jsonify({"error": "Log file not found"})

    try:
        with open(log_path) as f:
            lines = f.readlines()[-10:]  # Get last 10 commands
            return jsonify([json.loads(line) for line in lines])
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # <<< THIS is what makes it reachable from browser