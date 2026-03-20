def get_property_count(location, property_type, budget):
    """
    Simulates property search based on user input
    """

    location = location.lower()
    property_type = property_type.lower()

    # Dummy dataset logic (simulating real API)
    if location in ["delhi", "noida", "gurgaon"]:
        if property_type == "residential":
            return 5
        else:
            return 3

    elif location in ["mumbai", "pune"]:
        if property_type == "residential":
            return 4
        else:
            return 2

    else:
        return 0