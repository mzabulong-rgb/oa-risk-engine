@app.route("/report", methods=["POST"])
def report():

    try:

        data = request.get_json()

        csv_data = data.get("csv_data", "")

        print("=== RECEIVED DATA START ===")
        print(csv_data[:1000])
        print("=== RECEIVED DATA END ===")

        df = pd.read_csv(
            StringIO(csv_data),
            engine="python",
            on_bad_lines="skip"
        )

        store_count = len(df)

        return jsonify({
            "status": "success",
            "store_count": store_count
        })

    except Exception as e:

        print("ERROR:")
        print(str(e))

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
