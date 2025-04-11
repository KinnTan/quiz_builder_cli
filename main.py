import json
import time

def loading_animation():
    spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    counter = 0

    while True:
        print(f"\r{spinner[counter]}", end="")
        time.sleep(0.1)
        counter += 1
        if counter >= len(spinner):
            counter = 0

# Generates a unique filename if the default one exists
def unique_filename():
    # Set default filename
    filename = "quiz_data.json"
    file_counter = 0

    # Try to create a file with the default name
    while True:
        try:
            open(filename, "x") # Attempt to create the file
            break # If successful, exit the loop
        except FileExistsError:
            # If the file exists, increment the counter and try a new name
            file_counter += 1
            filename = f"quiz_data_{file_counter}.json"
    return filename # Return the final unique filename

# Saves the quiz data to a json file
def save_data(quiz_data):
    # Generate a unique filename
    filename = unique_filename()

    # Open the file for writing
    file = open(filename, "w")

    # Notify the user
    print("exiting...")
    print(f"Saving quiz to {filename}")

    # Write the quiz data to the file in json formatting
    file.write(str(json.dumps(quiz_data, indent=4)))

    # Close the file
    file.close()

# Writes the data to the initialized list
def write_data(quiz_data, question, choices, correct_choice):
    # Store the question and choices in a dictionary
    (quiz_data.append
    ({
                "question":question,
                "choices":choices,
                "correct_answer":correct_choice
    }))
    # Confirm that the question has been added
    print("Question added successfully")
    return quiz_data  # Return the updated data

# Prompts the user for a question
def get_question():
    while True:
        # Ask the user for a question
        question = input("Enter the question (or type 'exit' to quit): ")

        # If the user types "exit", stop asking and return None
        if question.lower() == "exit" :
            return None

        # If the user enters nothing, prompt again
        elif question == "":
            print("Please enter a question")
            continue
        return question # Return the valid question

# Prompts the user for the choices
def get_choices():
    choices = {}

    # Ask the user to enter choices for A, B, C, and D
    while True:
        print("Enter the choices")
        for option in ["a", "b", "c", "d"]:
            choices[option] = input(f"Choice {option}: ")
        return choices # Return the dictionary of choices

# Prompts the user for the correct choice
def get_correct_choice():
    while True:

        # Ask the user to select the correct answer
        correct_choice = input("Which is the correct choice: ").lower()

        # Validate the input
        if correct_choice not in ["a", "b", "c", "d"]:
            print("Invalid choice")  # Tell the user the choice is invalid if it is incorrect
            continue # Prompts the user for the correct choice again
        else:
            break # If valid, exit the loop
    return correct_choice # Return the correct answer

def main():
    quiz_data = [] # Initialize an empty list to store quiz data

    # Display the Logo
    print("""
     ██████╗ ██╗   ██╗██╗███████╗    ██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗      ██████╗██╗     ██╗
    ██╔═══██╗██║   ██║██║╚══███╔╝    ██╔══██╗██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗    ██╔════╝██║     ██║
    ██║   ██║██║   ██║██║  ███╔╝     ██████╔╝██║   ██║██║██║     ██║  ██║█████╗  ██████╔╝    ██║     ██║     ██║
    ██║▄▄ ██║██║   ██║██║ ███╔╝      ██╔══██╗██║   ██║██║██║     ██║  ██║██╔══╝  ██╔══██╗    ██║     ██║     ██║
    ╚██████╔╝╚██████╔╝██║███████╗    ██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██║  ██║    ╚██████╗███████╗██║
     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚═╝

    """)

    while True:
        question = get_question() # Get a new question from the user

        # If the user wants to exit, break the loop
        if question is None:
            break
        else:
            choices = get_choices() # Get the possible answers
            correct_choice = get_correct_choice() # Get the correct answer from the user
            write_data(quiz_data, question, choices, correct_choice) # Store the question and answer choices

    # Saves the data to a json file
    save_data(quiz_data)

if __name__ == "__main__":
    main()