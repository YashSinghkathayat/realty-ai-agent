import datetime

LOG_FILE = "logs/conversation.txt"


def log_message(message):
    """Save messages to log file with timestamp"""
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")


def get_input(prompt):
    """Print question, take input, log both"""
    print(prompt)
    user_input = input("> ")

    log_message(f"BOT: {prompt}")
    log_message(f"USER: {user_input}")

    return user_input


def chat_agent(lead):
    """Main conversation flow"""

    print("Hello — this is RealtyAssistant about your enquiry.")
    log_message("Conversation Started")

    # Step 1: Confirm Name
    response = get_input(f"Am I speaking with {lead['name']}? (yes/no)")

    if response.lower() != "yes":
        name = get_input("May I know your name?")
    else:
        name = lead["name"]

    # Step 2: Location
    location = get_input("Which location are you searching in?")

    # Step 3: Property Type
    property_type = get_input("Residential or Commercial?")

    # Step 4: Subtype
    if property_type.lower() == "residential":
        subtype = get_input("Which BHK (1/2/3/4)?")
    else:
        subtype = get_input("Shops / Office / Plot?")

    # Step 5: Budget
    budget = get_input("What is your budget?")

    # Step 6: Consent
    consent = get_input("Would you like a sales representative to call? (yes/no)")

    log_message("Conversation Ended")

    return {
        "name": name,
        "location": location,
        "type": property_type,
        "subtype": subtype,
        "budget": budget,
        "consent": consent
    }