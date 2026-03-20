def qualify_lead(data, property_count):
    """
    Determines whether the lead is Qualified or Not Qualified
    """

    consent = data.get("consent", "").lower()

    # Rule 1: Must have matching properties
    if property_count <= 0:
        return "Not Qualified"

    # Rule 2: User must agree to sales call
    if consent != "yes":
        return "Not Qualified"

    # If both conditions satisfied
    return "Qualified"