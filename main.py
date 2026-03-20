from flask import Flask, request, jsonify
from app.chat_agent import chat_agent
from app.services.property_service import get_property_count
from app.services.qualification_service import qualify_lead
from app.utils.json_handler import save_summary

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Agent Running 🚀"

@app.route("/run-agent", methods=["POST"])
def run_agent():
    lead = request.json

    data = chat_agent(lead)

    property_count = get_property_count(
        data["location"],
        data["type"],
        data["budget"]
    )

    status = qualify_lead(data, property_count)

    summary = save_summary(data, property_count, status)

    return jsonify({
        "property_count": property_count,
        "status": status,
        "summary": summary
    })