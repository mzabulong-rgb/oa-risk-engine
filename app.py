from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "OA Risk Engine Running"

@app.route("/report", methods=["POST"])
def report():

    data = request.get_json()

    csv_data = data.get("csv_data", "")

    report_html = """
    <h2>Operational Audit Risk Report</h2>
    <p>API is working successfully.</p>
    """

    return jsonify({
        "status": "success",
        "report_html": report_html
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
