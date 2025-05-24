from flask import Flask, request, jsonify
import pandas as pd
import re

app = Flask(__name__)

# Load the Data
df = pd.read_excel("data/HSN_Master_Data.xlsx")
df['HSNCode'] = df['HSNCode'].astype(str)

# Validate the HSN code format
def is_valid_format(hsn):
    return bool(re.fullmatch(r"\d{2}|\d{4}|\d{6}|\d{8}", hsn))

# Check if HSN code exists in excel data
def hsn_exists(hsn):
    return not df[df['HSNCode'] == hsn].empty

# Get HSN description
def get_description(hsn):
    row = df[df['HSNCode'] == hsn]
    return row.iloc[0]['Description'] if not row.empty else None

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        hsn_code = data.get("hsn_code")

        if not hsn_code:
            return jsonify({
                "Status": "Error",
                "Response": "No HSN code provided. Please enter a valid code.",
            })

        hsn_code = hsn_code.strip()

        if not is_valid_format(hsn_code):
            return jsonify({
                "Status": "Error",
                "Response": "Invalid format. HSN code must be 2, 4, 6 or 8 digits.",
            })

        if hsn_exists(hsn_code):
            description = get_description(hsn_code)
            return jsonify({
                "Status": "Success",
                "Response": f"HSN Code {hsn_code} is valid: {description}",
            })
        else:
            return jsonify({
                "Status": "Error",
                "Response": f"HSN Code {hsn_code} is not found in the master database.",
            })

    except Exception as e:
        return jsonify({
                "Status": "Error",
                "Response": f"An error occurred: {str(e)}",
            })

if __name__ == "__main__":
    app.run(debug=True)
