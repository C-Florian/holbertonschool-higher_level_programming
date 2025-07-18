import os

def generate_invitations(template, attendees):
    # Check for specific errors and types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Error: Attendees must be a list.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for person in attendees:
        if not isinstance(person, dict):
            print("Error: Attendees must be a list of dictionaries.")
            return

    # Generate invitations and create output files
    for i, person in enumerate(attendees, start=1):
        # i: index of the person in the list, starting from 1
        # person: dictionary containing the current guest's information

        invitation_text = template
        # Create a copy of the template to avoid modifying the original
        # invitation_text will be customized for this person

        keys = ["name", "event_title", "event_date", "event_location"]
        # List of keys to replace in the template

        for key in keys:
            value = person.get(key)
            # Retrieve the value associated with the key from the dictionary
            # If the key doesn't exist, get() returns None

            if not value:
                value = "N/A"
            invitation_text = invitation_text.replace("{" + key + "}", value)
            # Replace the placeholder {key} in the template with the corresponding value

        filename = f"output_{i}.txt"
        # Generate the filename using the person's number

        if os.path.exi
