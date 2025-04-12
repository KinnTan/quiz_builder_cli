# Quiz Builder CLI

## Overview
This script allows users to create a custom quiz by entering questions, answer choices, and selecting the correct answer. The quiz data is saved in a JSON file, ensuring that each quiz has a unique filename. The program continuously prompts the user for questions and answers until they choose to exit.

## Requirements
- Python 3.x
- No external libraries are required beyond Python's built-in libraries (such as `json`).

## Installation

**Option 1: Clone the Repository**

   ```bash
   git clone https://github.com/KinnTan/quiz_builder_cli.git
   cd quiz_builder_cli
   ```
**Option 2: Download From Release**
1. Go to the Releases page.
2. Download the latest `.zip` or `.tar.gz` release.
3. Extract the archive and navigate to the extracted folder in your terminal.

## Usage

1. Run the script by executing `python quiz_builder_cli.py` in the terminal.
2. Follow the prompts to enter quiz questions, choices, and the correct answer.
3. Type 'exit' when you are finished creating the quiz.
4. The quiz data will be saved to a JSON file, which will be automatically named to avoid conflicts with existing files.

Example interaction:
```
$ python quiz_builder_cli.py

     ██████╗ ██╗   ██╗██╗███████╗    ██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗      ██████╗██╗     ██╗
    ██╔═══██╗██║   ██║██║╚══███╔╝    ██╔══██╗██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗    ██╔════╝██║     ██║
    ██║   ██║██║   ██║██║  ███╔╝     ██████╔╝██║   ██║██║██║     ██║  ██║█████╗  ██████╔╝    ██║     ██║     ██║
    ██║▄▄ ██║██║   ██║██║ ███╔╝      ██╔══██╗██║   ██║██║██║     ██║  ██║██╔══╝  ██╔══██╗    ██║     ██║     ██║
    ╚██████╔╝╚██████╔╝██║███████╗    ██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██║  ██║    ╚██████╗███████╗██║
     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚═╝

Enter the question [type 'exit' to save and quit]:
5 + 1
Enter the choices
Choice A: 4
Choice B: 5
Choice C: 6
Choice D: 7
Which is the correct choice: c
Question stored successfully

Enter the question [type 'exit' to save and quit]:
exit
Saving quiz to quiz_data.json
Successfully saved quiz to quiz_data.json
```

## Notes
- The JSON file is saved in the same directory where the script is run.
- Each time you run the script, a new file will be created if one already exists.

## Potential Improvments
- Automatically create an output folder
- Allow user to choose a filename
- more UI/UX enhancments
