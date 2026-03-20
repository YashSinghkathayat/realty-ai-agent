from app.chat_agent import chat_agent
from app.services.property_service import get_property_count
from app.services.qualification_service import qualify_lead
from app.utils.json_handler import save_summary

def main():
    # Step 1: Lead input (initial data)
    lead = {
        "name": "Yash",
        "phone": "9876543210",
        "email": "yash@gmail.com"
    }

    print("\n--- Starting AI Agent ---\n")

    # Step 2: Chat Agent (collect user data)
    data = chat_agent(lead)

    # Step 3: Property Search
    property_count = get_property_count(
        data["location"],
        data["type"],
        data["budget"]
    )

    # Step 4: Qualification Decision
    status = qualify_lead(data, property_count)

    # Step 5: Save JSON Summary
    summary = save_summary(data, property_count, status)

    # Step 6: Final Output
    print("\n--- RESULT ---")
    print(f"Property Matches: {property_count}")
    print(f"Lead Status: {status}")
    print("Summary saved in data/output.json")


if __name__ == "__main__":
    main()