file = open("quiz_data.txt", "a")
question_data = []

while True:
    question = input("Enter the question you want to add (or type 'exit' to quit): ")
    if question.lower() == "exit" :
        break
    choice_a = input("Enter a choice for a: ").lower()
    choice_b = input("Enter a choice for b: ").lower()
    choice_c = input("Enter a choice for c: ").lower()
    choice_d = input("Enter a choice for d: ").lower()

    while True:
        correct_choice = input("Enter the correct choice: "). lower()
        if correct_choice not in ["a", "b", "c", "d"]:
            print("Invalid choice")
        else:
            break

    question_data.append({
                "question":question,
                "a":choice_a,
                "b":choice_b,
                "c":choice_c,
                "d":choice_d,
                "correct_answer":correct_choice
                })

# Write the question_data only on exit
file.write(str(question_data))

