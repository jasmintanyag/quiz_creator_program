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

# Add some colors and emojis

import json
from colorama import init, Fore, Style



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

        options = {}
        for choice in ['a', 'b', 'c', 'd']:
            answers = input(f"Option {choice}: ")
            if answers.lower() == 'exit':
                return
            
            options[choice] = answers

        correct_ans = input("Enter the CORRECT answer (a, b, c, d): ").lower().strip()
        print(f"Received input: {correct_ans}") #debugging line
        while correct_ans not in ['a', 'b', 'c', 'd']:
            correct_ans = input("INVALID. Choose only from (a, b, c, d): ").lower().strip()

        print(f"You entered: {correct_ans}")

        questions.append({
            "questions": questn,
            "options": options,
            "correct": correct_ans})
        
        print("Question added!")
        
    with open(filename, "a") as f:
        for entry in questions:
            f.write(json.dumps(entry) + "\n")
    
    print(f"All questions are now saved in {filename} under the {category} category.")

if __name__ == "__main__":
    create_quiz_file()