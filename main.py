# Generates a unique filename if the default one exists
def unique_filename():
    filename = "quiz_data.txt"
    file_counter = 0
    while True:
        try:
            open(filename, "x")
            break
        except FileExistsError:
            file_counter += 1
            filename = f"quiz_data_{file_counter}.txt"
    return filename

# Saves the quiz data to a txt file
def save_data(question_data):
    filename = unique_filename()
    file = open(filename, "w")
    print("exiting...")
    print(f"Saving quiz to {filename}")
    file.write(str(question_data))
    file.close()

# Writes the data to the txt file
def write_data(question_data, question, choices, correct_choice):
    question_data.append({
                "question":question,
                "choices":choices,
                "correct_answer":correct_choice
                })
    print("Question added successfully")

    return question_data

# Prompts the user for a question
def get_question():
    while True:
        question = input("Enter the question (or type 'exit' to quit): ")
        if question.lower() == "exit" :
            return None
        elif question == "":
            print("Please enter a question")
            continue
        return question

# Prompts the user for the choices
def get_choices():
    choices = {}
    while True:
        print("Enter the choices")
        for option in ["a", "b", "c", "d"]:
            choices[option] = input(f"Choice {option}: ")
        return choices

# Prompts the user for the correct choice
def get_correct_choice():
    while True:
        correct_choice = input("What is the correct choice: ").lower()
        if correct_choice not in ["a", "b", "c", "d"]:
            print("Invalid choice")
        else:
            break
        return correct_choice

def main():
    question_data = []
    # Logo
    print("""
     ██████╗ ██╗   ██╗██╗███████╗    ██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗      ██████╗██╗     ██╗
    ██╔═══██╗██║   ██║██║╚══███╔╝    ██╔══██╗██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗    ██╔════╝██║     ██║
    ██║   ██║██║   ██║██║  ███╔╝     ██████╔╝██║   ██║██║██║     ██║  ██║█████╗  ██████╔╝    ██║     ██║     ██║
    ██║▄▄ ██║██║   ██║██║ ███╔╝      ██╔══██╗██║   ██║██║██║     ██║  ██║██╔══╝  ██╔══██╗    ██║     ██║     ██║
    ╚██████╔╝╚██████╔╝██║███████╗    ██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██║  ██║    ╚██████╗███████╗██║
     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚═╝

    """)
    while True:
        question = get_question()
        if question is None:
            break
        else:
            choices = get_choices()
            correct_choice = get_correct_choice()
            write_data(question_data, question, choices, correct_choice)
    # Saves the data to a txt file
    save_data(question_data)

if __name__ == "__main__":
    main()