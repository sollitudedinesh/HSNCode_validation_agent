# 🧠 HSN Code Validation Agent (Google ADK Conceptual Design)

This project is built as part of an internship evaluation to design an intelligent agent using the **conceptual Google ADK framework**. The agent validates HSN (Harmonized System Nomenclature) codes based on a provided master Excel file.

---

## ✅ What It Does

- Takes a user input HSN code.
- Checks if it follows a valid format (2, 4, 6, or 8 digits).
- Looks up the HSN code in the master Excel data.
- Returns a response: Valid / Invalid / Format Error.

---

## 🧱 Tech Stack

- Python 3.11
- Flask (Web API)
- pandas (Excel reading)
- openpyxl (required by pandas to read .xlsx)
- Postman (to test the webhook)

---

## 📁 Project Structure

```
hsn-code-validation-agent/
│
├── agent/
│   └── webhook.py                  # Main Flask app
├── data/
│   └── HSN_Master_Data.xlsx        # Provided dataset
├── requirements.txt
├── README.md
```

---

## 🚀 Setup Instructions

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python agent/webhook.py
   ```

---

## 📬 Test With Postman

### URL:

```
POST http://127.0.0.1:5000/webhook
```

### Body (raw JSON):

```json
{
  "hsn_code": "01011010"
}
```

### Example Responses:

- ✅ Valid:
  ```
  HSN Code 01011010 is valid: PURE-BRED BREEDING ANIMALS HORSES
  ```
- ❌ Invalid:
  ```
  HSN Code 12345678 is not found in the master database.
  ```
- ⚠️ Format Error:
  ```
  Invalid format. HSN code must be 2, 4, 6 or 8 digits.
  ```

---

## 🧠 How This Uses Google ADK Conceptually

| ADK Concept | Implementation                     |
| ----------- | ---------------------------------- |
| Intent      | Validate HSN Code                  |
| Entity      | HSN Code (as user parameter)       |
| Fulfillment | Python Flask webhook handles logic |
| Response    | JSON `Response` like Dialogflow    |

---

## 🎥 Deliverables

- ✅ Code on GitHub
- ✅ Output screenshots (valid, invalid)
- 🎥 Explanation video (screen recording, walkthrough of app, logic, testing)

---

## 📌 Notes

This agent is designed **based on the conceptual Google ADK model**, not actual Dialogflow implementation. It demonstrates the intent-entity-fulfillment architecture expected from a smart agent.
