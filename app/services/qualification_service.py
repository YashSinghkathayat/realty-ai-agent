def qualify_lead(data, property_count):
    consent = data.get("consent", "").lower()

    if property_count <= 0:
        return "Not Qualified"

    if consent != "yes":
        return "Not Qualified"

    return "Qualified"