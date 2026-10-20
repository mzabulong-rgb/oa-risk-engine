from flask import Flask, request, jsonify
import pandas as pd
from io import StringIO

app = Flask(__name__)

@app.route("/")
def home():
    return "OA Risk Engine Running"

@app.route("/report", methods=["POST"])
def report():

    try:

        data = request.get_json()

        csv_data = data.get("csv_data", "")

        print("CSV RECEIVED")

        df = pd.read_csv(
            StringIO(csv_data),
            engine="python",
            on_bad_lines="skip"
        )

        return jsonify({
            "status": "success",
            "store_count": len(df)
        })

    except Exception as e:

        print(str(e))

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
