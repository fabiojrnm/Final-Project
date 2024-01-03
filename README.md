
# Super Quiz

Welcome to the Super Quiz! Test your knowledge with this quiz program.


## Overview

The Super Quiz allows users to choose a quiz level and answer a series of questions. The program provides feedback on each answer and calculates the user's final score.
There is no requirements to run this program.

Project structure:
- **project.py**
- **test_project.py**
- **README.md**
- **requirements.txt**


## Video Demo
For a quick demo of how the Super Quiz works, check out this [YouTube video](https://youtu.be/ofq0F0h6rQo).

## Usage

To play the Super Quiz, follow these steps:

1. Run the Python script: `project.py`
2. Choose a quiz level:

    - type "1" for Easy, where you will have three questions to answer;

    - type "2" for Medium, where you will have 5 questions to answer;

    - type "3" for Hard, where it's 7 questions to answer;

    - type "exit" if you want to quit the quiz.

3. Answer the questions presented by entering the number corresponding to your answer. Invalid answer will count as incorrect. 
4. If your answer is right, the program will print out "Correct!" and give the user 1 point.
If the answer is wrong, will print out "Wrong! The correct answer is: " with the correct answer to the question.

4. During the quiz, you can exit by just typing 'exit' as your answer.
5. After answering all the questions, you will get your final score.
For example, if you choose Easy and 2 of the 3 questions are correct, will print out like this:
"Your score is 2/3"
"Your final grade is 67%"
6. After the final score, will prompt the user to see if the user want to play again. Accepting only "yes" or "no" as answer.
If the user type "yes", the quiz will start again, where the user can choose again the level of the quiz.
If type "no", the program will end there.



## Functioning

The project.py contains 7 functions including the main function.

- **`main()`:** This function has a while true loop, where it calls `play_quiz()` function and checks if the `play_again()` function is true. In that case, is going to call `play_quiz()` again.
- **`play_again()`:** This function is called at the end of the quiz. Where we prompt the user if they want to play again. Returning True or False.
- **`play_quiz()`:** This function calls all the other functions, that make the quiz run and at the end prints the final score of the quiz.
- **`quiz_level(user_level)`:** This function prompts the user to choose the level of the quiz, where it checks if the input from the user is one of the levels or exit to quit the quiz. If it's not one of those, the program will prompt the user again, to get a correct input. Then, returns the value, so we know what level to load. 
- **`questions_level(level_chosen)`:** This function job is to load the questions, takes one argument, `level_chosen` and just compare too the options we have, after that, just load the pack of questions and return it. 
- **`start_quiz(quiz_questions)`:** This function gets one argument `quiz_questions` and is job is to print out one question and the possible answers at the time, then prompt the user for is answer. After get the user input, it checks if the input is a valid one. if it's the correct answer and add 1 point to the score. If it's a wrong asnwer, it will display the correct answer. 
In the case that the input from the user is invalid, the program will prompt that and move to the next question. 
At the end the for loop, will return the score.
- **`score_quiz(score, total_questions)`:** This function takes two arguments and is job is just to display the final score of the quiz. It's the `score` that we get from the quiz and `total_questions` that is the number of the questions that we had in the quiz. 
With that, will calculate the percentage of the score and display it too.



## Author

Fábio Jerónimo

