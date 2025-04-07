filename = "quiz_data.txt"
filename_counter = 0

while True:
    try:
        file = open(filename, "x")
        break
    except FileExistsError:
        filename_counter += 1
        filename = f"quiz_data_{filename_counter}.txt"

question_data = []

print("""
 ██████╗ ██╗   ██╗██╗███████╗    ██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗      ██████╗██╗     ██╗
██╔═══██╗██║   ██║██║╚══███╔╝    ██╔══██╗██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗    ██╔════╝██║     ██║
██║   ██║██║   ██║██║  ███╔╝     ██████╔╝██║   ██║██║██║     ██║  ██║█████╗  ██████╔╝    ██║     ██║     ██║
██║▄▄ ██║██║   ██║██║ ███╔╝      ██╔══██╗██║   ██║██║██║     ██║  ██║██╔══╝  ██╔══██╗    ██║     ██║     ██║
╚██████╔╝╚██████╔╝██║███████╗    ██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██║  ██║    ╚██████╗███████╗██║
 ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚═╝
                                                                                                            
""")
while True:
    question = input("Enter the question (or type 'exit' to quit): ")
    if question.lower() == "exit" :
        break
    print("Enter the choices")
    choice_a = input("Choice a: ").lower()
    choice_b = input("Choice b: ").lower()
    choice_c = input("Choice c: ").lower()
    choice_d = input("Choice d: ").lower()

    while True:
        correct_choice = input("What is the correct choice: "). lower()
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
    print("Question added successfully")

print("exiting...")
print(f"Saving quiz to {filename}")

# Write the question_data only on exit
file.write(str(question_data))
file.close()

