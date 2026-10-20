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

        df = pd.read_csv(StringIO(csv_data))

        store_count = len(df)

        html = f"""
        <h2>Executive Summary</h2>

        <p>
        Total stores assessed: {store_count}
        </p>

        <h2>Data Preview</h2>

        {df.head(10).to_html(index=False)}
        """

        return jsonify({
            "status": "success",
            "store_count": store_count,
            "report_html": html
        })

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
