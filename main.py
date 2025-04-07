
while True:
    question = input("Enter the question you want to add: ")

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

