def get_property_count(location, property_type, budget):
    location = location.lower()

    if location in ["delhi", "noida", "gurgaon"]:
        return 5
    elif location in ["mumbai", "pune"]:
        return 3
    else:
        return 0