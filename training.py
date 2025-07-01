# A tiny piece of code that represents an HR Employee Training Management system.
# This code will manage a simple string that contains employee data.

employee_data = "Alice,Developer,3|Bob,Manager,1|Charlie,Designer,4"
# Splitting the employee data by '|' to separate each employee's info
employee_list = employee_data.split('|')

# TODO: For each employee, create a formatted string with stripped details and training status
for employee in employee_list:
    # TODO: Parse the employee data and add training refresh note if applicable
    name, role, years_str = [item.strip() for item in employee.split(',')]
    years_since_training = int(years_str)
    
    if years_since_training > 2:
        training_status = " - Needs training refresh"
    else:
        training_status = ""
        
    print(f"Name: {name} - Role: {role} - Years since training: {years_since_training}{training_status}")
    # Example: Name: Alice - Role: Developer - Years since training: 3 - Needs training refresh