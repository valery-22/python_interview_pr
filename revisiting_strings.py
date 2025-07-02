# Space exploration crew members' data, containing their names, missions, and roles
crew_data = "Neil,Armstrong,Apollo 11,C;Buzz,Aldrin,Apollo 11,P;Michael,Collins,Apollo 11,CM"

# Split the crew_data string into a list of individual crew member information using the appropriate delimiter
individual_crew = crew_data.split(';')

# Iterate over the list of crew member data
for individual in individual_crew:
    # For each member, split their data string using commas as delimiters
    parts = individual.split(',')

    # Print the crew member's details in a formatted string
    print(f"{parts[0]} {parts[1]} {parts[2]} {parts[3]}")
