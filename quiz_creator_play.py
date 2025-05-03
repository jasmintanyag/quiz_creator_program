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

# Define load questions
    # Initialize empty set to store questions
    # If file doesn't exist
        # Print error message
    # Open file, read each line
    # Append it to list
    # If not valid, print error message
    # Return

# Define list categories
    # List all the .txt file
    # Remove .txt from each file name
    # Return list of category names

# Define play quiz
    # Get the list of categories
    # If no category
        # Print error message
    # Print welcome message
    # Ask user to input name
    # If name is empty
        # Print error message
    # Print list of category
    # Ask user to choose category
    # If invalid
        # Print error message
    # Load questions  of the selected category
    # If no valid questions
        # Print error message

    # Randomize the questions
    # Set initial score to 0
    # Start the quiz

    # For every question
        # Put a divider
        # Print the question
        # Print all choices (A, B, C, D)
        # Ask user their answer
        # If correct
            # Play 'correct' sound and display 'correct' message
        # If wrong
            # Play 'wrong' sound and display 'wrong' message, then show the correct answer
    
    # After answering all questions
        # Print final score
        # Load all the existing scores
        # Add or update the score
        # Save the score, then print confirmation message

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
        print("\n----- Quizzierett -----")
        print("1. Play Quiz")
        print("2. Exit")
        choice = input("Select an option: ")

# If script is run directly
    # Call main menu