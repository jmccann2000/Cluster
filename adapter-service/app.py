from flask import Flask, jsonify
import random
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow all origins

@app.route('/datatable', methods=['GET'])
def get_datatable():
    fake_states = ["Draft", "Released", "Obsolete", "In Review"]
    data = []

    for i in range(1, 6):  # 5 rows
        bom_id = f"BOM-{1000 + i}"
        revision = f"Rev-{chr(64 + i)}"  # A, B, C...
        start_date = (datetime.date.today() - datetime.timedelta(days=random.randint(1, 100))).isoformat()
        end_date = (datetime.date.today() + datetime.timedelta(days=random.randint(1, 100))).isoformat()
        state = random.choice(fake_states)
        data.append([bom_id, revision, start_date, end_date, state])

    return jsonify({"data": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
