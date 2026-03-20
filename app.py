from flask import Flask, request, jsonify, render_template
from app.chat_agent import chat_agent

app = Flask(__name__)


# ✅ Home Route (UI)
@app.route("/")
def home():
    return render_template("index.html")


# ✅ Chat API Route
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        # Get message from frontend
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({"response": "Please enter a message"}), 400

        # Simple user tracking (IP-based)
        user_id = request.remote_addr

        # Call chat agent
        response = chat_agent(user_id, user_input)

        # Debug (check in terminal)
        print("User:", user_input)
        print("Bot:", response)

        # IMPORTANT: must return "response"
        return jsonify({
            "response": response
        })

    except Exception as e:
        print("Error:", str(e))
        return jsonify({
            "response": "Something went wrong"
        }), 500


# ✅ Optional Result Page
@app.route("/result")
def result():
    return render_template("result.html")


# ✅ Run Flask App
if __name__ == "__main__":
    app.run(debug=True)