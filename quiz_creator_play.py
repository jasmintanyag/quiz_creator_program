# Import needed libraries
import json
import os
import random
import time
from colorama import init, Fore, Style
import pygame

# Initialize colorama and pygame
init(autoreset=True)
pygame.mixer.init()

# Define play sound
    # Load music file
    # Play music file

def play_sound(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

# Set score file -> "scores.json"
# Define load scores
    # If score file exist
        # Open file and load data then return dictionary
    # Else
        # Return empty dictionary

SCORE_FILE = "scores.json"
def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as score_file:
            return json.load(score_file)
    return {}

# Define save scores
    # Open the file in write mode
    # Write the scores to json

def save_scores(scores):
    with open(SCORE_FILE, "w") as score_file:
        json.dump(scores, score_file, indent=5)

# Define countdown
    # Play the starting sound
    # For each second
        # Print countdown message
    # When countdown ends
        # Overwrite the countdown w/ spaces to clear the line

def countdown(seconds=3):
    sound = pygame.mixer.Sound("start_quiz.wav")
    sound.play()
    for remaining_seconds in range(seconds, 0, -1):
        print(f"{Fore.YELLOW}⏳ The quiz will start in {remaining_seconds}...", end="\r")
        time.sleep(0.5)
    print(" " * 30, end="\r")

# Define load questions
    # Initialize empty set to store questions
    # If file doesn't exist
        # Print error message
    # Open file, read each line
    # Append it to list
    # If not valid, print error message
    # Return

def load_questions(category):
    filename = f"{category}.txt"
    questions = []
    if not os.path.exists(filename):
        print(f"{Fore.RED}❌ The file '{filename}' is not found.")
        return questions
    with open(filename, "r") as file:
        for line in file:
            try:
                questions.append(json.loads(line.strip()))
            except json.JSONDecodeError:
                print(f"{Fore.RED}❌ Invalid line")
    return questions

# Define list categories
    # List all the .txt file
    # Remove .txt from each file name
    # Return list of category names

def list_categories():
    return [filename[:-4] for filename in os.listdir() if filename.endswith(".txt")]

# Define play quiz
    # Get the list of categories
    # If no category
        # Print error message

def play_quiz():
    categories = list_categories()
    if not categories:
        print(f"{Fore.RED}❌ No categories found.")
        return
    
    # Print welcome message
    # Ask user to input name
    # If name is empty
        # Print error message
            
    print(f"{Fore.CYAN}🎮 Welcome to Quizzierett!🎮")
    players_name = input("Enter your name: ")
    if not players_name:
        print(f"{Fore.RED}❌ The name should not be empty.")
        return
    
    # Print list of category
    # Ask user to choose category
    # If invalid
        # Print error message
        
    print("\nThe Categories are:")
    for index, catgry in enumerate(categories, 1):
        print(f"{index}.{catgry}")
    try:
        catgry_index = int(input("Choose a category (number only): ")) -1
        selected_category = categories[catgry_index]
    except (IndexError, ValueError):
        print(f"{Fore.RED}❌ Invalid choice!")
        return
    
    # Load questions of the selected category
    # If no valid questions
        # Print error message

    questions = load_questions(selected_category)
    if not questions:
        print(f"{Fore.RED}❌ No valid questions in this category.")
        return
    
    # Randomize the questions
    # Set initial score to 0
    # Call the countdown before the quiz starts

    random.shuffle(questions)
    score = 0
    countdown()

    # For every question
        # Put a divider
        # Print the question
        # Print all choices (A, B, C, D)

    for question_file in questions:
        print(f"\n" + "~" * 50)
        print(f"{Fore.MAGENTA}{question_file['questions']}")
        for key, val in question_file["options"].items():
            print(f"{key.upper()}: {val}")

        # Ask user their answer
        # If correct
            # Play 'correct' sound and display 'correct' message
        # If wrong
            # Play 'wrong' sound and display 'wrong' message, then show the correct answer

        users_answer = input("Your answer is: ")
        if users_answer.lower() == question_file["correct"]:
            play_sound("correct.wav")
            print(f"{Fore.GREEN}✅ Your answer is CORRECT!")
            score += 1
        else:
            play_sound("wrong.wav")
            print(f"{Fore.RED}❌ WRONG! The correct answer is {question_file['correct'].upper()}")
    
    # After answering all questions
        # Print final score
        # Load all the existing scores
        # Add or update the score
        # Save the score, then print confirmation message

    print(f"{Fore.YELLOW}🎉 CONGRATULATIONS! You completed the quiz! \nYour score is: {score}/{len(questions)}")

    scores = load_scores()
    scores[players_name] = score
    save_scores(scores)

    print(f"{Fore.CYAN}🏆 Your score has been saved under the name '{players_name}.")

# Define main menu
    # Create loop
        # Print the header
        # Show options [1. Play Quiz, 2. Exit]
        # Ask user input
        # If 1, call play quiz
        # If 2, print goodbye message
        # Else, print error message

def main_menu():
    while True:
        print(f"\n{Fore.YELLOW}----- Quizzierett -----")
        print("1. Play Quiz")
        print("2. Exit")
        choice = input(f"{Fore.MAGENTA}Select an option: ")
        if choice == "1":
            play_quiz()
        elif choice == "2":
            print(f"{Fore.CYAN}Exiting..... Goodbye!👋")
            break
        else:
            print(f"{Fore.RED}❌ Invalid input!")

# If script is run directly
    # Call main menu

if __name__ == "__main__":
    main_menu()

# Add some colors and emojis