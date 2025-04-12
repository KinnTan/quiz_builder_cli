# Quiz Builder CLI

## Overview
This script allows users to create a custom quiz by entering questions, answer choices, and selecting the correct answer. The quiz data is saved in a JSON file, ensuring that each quiz has a unique filename. The program continuously prompts the user for questions and answers until they choose to exit.

## Requirements
- Python 3.x
- No external libraries are required beyond Python's built-in libraries (such as `json`).

## Usage

1. Run the script by executing `python <script_name>.py` in the terminal.
2. Follow the prompts to enter quiz questions, choices, and the correct answer.
3. Type 'exit' when you are finished creating the quiz.
4. The quiz data will be saved to a JSON file, which will be automatically named to avoid conflicts with existing files.

Example interaction:
```
Enter the question (or type 'exit' to quit): What is 2 + 2?
Enter the choices
Choice a: 3
Choice b: 4
Choice c: 5
Choice d: 6
Which is the correct choice: b
Question added successfully

Enter the question (or type 'exit' to quit): exit
exiting...
Saving quiz to quiz_data.json
```

## Notes
- The JSON file is saved in the same directory where the script is run.
- Each time you run the script, a new file will be created if one already exists.

## Potential Improvments  <sup><sup><sub>if I can do it before deadline</sub></sup></sup>
- Create an output folder
- Allow user to choose a filename
- UI/UX enhancment - partially done
