# Start quiz creation function
# Print welcome messages
# Ask user to input category

# Set file name based on category
# Initialize empty list for questions

# Loop to input questions
    # Ask user to input question

    # Initialize dictionary for options
    # Loop through choices (a, b, c, d)
        # Ask user to input choices

        # Store the choices in options

    # Ask user to input the correct answer
    # Check if valid input

    # Add the question and options to the questions list 
    # Print confirmation message

# Write the question in JSON format

# Print ending message

import json

def create_quiz_file():
    print("\n Welcome to Quiz Creation!")
    print("(Type 'exit' anytime to quit.)\n")

    category = input("Enter a quiz category: ").lower().strip()
    if not category or category == 'exit':
        return
    
    filename = f"{category}.txt"
    questions = []

    while True:
        questn = input("Enter a question: ")
        if questn.lower() == 'exit':
            break