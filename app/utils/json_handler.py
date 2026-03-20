import json


def save_summary(data, property_count, status):
    """
    Saves final summary into JSON file
    """

    summary = {
        "name": data["name"],
        "location": data["location"],
        "property_type": data["type"],
        "subtype": data["subtype"],
        "budget": data["budget"],
        "consent": data["consent"],
        "property_matches": property_count,
        "status": status
    }

    # Save to file
    with open("data/output.json", "w") as f:
        json.dump(summary, f, indent=4)

    return summary