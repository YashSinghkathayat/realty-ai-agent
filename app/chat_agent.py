# app/chat_agent.py

# Store user sessions (temporary memory)
user_sessions = {}


def chat_agent(user_id, user_input):
    """
    Stateful chat agent for realty conversation
    """

    # Initialize session if new user
    if user_id not in user_sessions:
        user_sessions[user_id] = {
            "step": 0,
            "data": {}
        }

    session = user_sessions[user_id]
    step = session["step"]
    data = session["data"]

    user_input = user_input.strip()

    # Step 0: Greeting + Name
    if step == 0:
        session["step"] = 1
        return "Hello — this is RealtyAssistant. May I know your name?"

    # Step 1: Save Name
    elif step == 1:
        data["name"] = user_input
        session["step"] = 2
        return f"Nice to meet you {user_input}! Which location are you searching in?"

    # Step 2: Location
    elif step == 2:
        data["location"] = user_input
        session["step"] = 3
        return "Are you looking for Residential or Commercial property?"

    # Step 3: Property Type
    elif step == 3:
        data["type"] = user_input.lower()

        if "residential" in user_input.lower():
            session["step"] = 4
            return "Which BHK are you looking for? (1/2/3/4)"
        else:
            session["step"] = 4
            return "What type? (Shop / Office / Plot)"

    # Step 4: Subtype
    elif step == 4:
        data["subtype"] = user_input
        session["step"] = 5
        return "What is your budget?"

    # Step 5: Budget
    elif step == 5:
        data["budget"] = user_input
        session["step"] = 6
        return "Would you like a sales representative to call you? (yes/no)"

    # Step 6: Consent
    elif step == 6:
        data["consent"] = user_input.lower()
        session["step"] = 7

        # Final summary
        return f"""
✅ Thank you {data.get('name')}!

Here are your details:
📍 Location: {data.get('location')}
🏠 Type: {data.get('type')}
📌 Subtype: {data.get('subtype')}
💰 Budget: {data.get('budget')}
📞 Callback: {data.get('consent')}

Our team will contact you soon!
"""

    # After completion
    else:
        return "Conversation completed. Start again by refreshing."