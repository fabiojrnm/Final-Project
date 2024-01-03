
"""Questions in lists of dictionaries
    Where we can costumize as we want"""


level1_questions = [
    {
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "CO2", "O2"],
        "answer": "H2O",
    },
    {
        "question": "What's the capital of Spain?",
        "options": ["London", "Madrid", "Berlin"],
        "answer": "Madrid",
    },
    {
        "question": "Which country gifted the Statue of Liberty to the US?",
        "options": ["Germany", "England", "France"],
        "answer": "France",
    },
]

level2_questions = [
    {
        "question": "Which European country has the longest coastline?",
        "options": ["Italy", "Greece", "Norway"],
        "answer": "Norway",
    },
    {
        "question": "What was the name of the Greek god of war?",
        "options": ["Ares", "Apollo", "Zeus"],
        "answer": "Ares",
    },
    {
        "question": "In which part of your body would you find the cruciate ligament?",
        "options": ["Knee", "Elbow", "Foot"],
        "answer": "Knee",
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso"],
        "answer": "Leonardo da Vinci",
    },
    {
        "question": "In which year did the Berlin Wall fall?",
        "options": ["1989", "1991", "1979"],
        "answer": "1989",
    },
]

level3_questions = [
    {
        "question": "What is the driest desert in the world?",
        "options": ["Sahara Desert", "Atacama Desert", "Gobi Desert"],
        "answer": "Atacama Desert",
    },
    {
        "question": " In which year did the first modern Olympic Games take place?",
        "options": ["1886", "1906", "1896"],
        "answer": "1896", 
    },
    {
        "question": "Which element has the highest melting point?",
        "options": ["Tungsten", "Titanium", "Platinum"],
        "answer": "Tungsten",
    },
    {
        "question": "In what year did the French Revolution begin?",
        "options": ["1789", "1776", "1804"],
        "answer": "1789",
    },
    {
        "question": "Which element has the chemical symbol 'Au'?",
        "options": ["Silver", "Gold", "Platinum"],
        "answer": "Gold",
    },
    {
        "question": "In which year did Usain Bolt set the world record for the 100m sprint?",
        "options": ["2009", "2012", "2016"],
        "answer": "2009",
    },
    {
        "question": "Which element has the highest atomic number?",
        "options": ["Uranium", "Plutonium", "Oganesson"],
        "answer": "Oganesson",
    },
]


def main():
    """Main function to start the quiz"""

    print("Welcome to the Super Quiz!\n")
    while True:
        play_quiz()
        if play_again() is True:
            print("\nLet's go for another round!\n\nChoose the level")
        else:
            print("\nSee you next time \nGoodbye")
            exit()


def play_again():
    """Prompt the user if they want to play again"""

    while True:
        answer = input("\n\nDo you wanna play again? (yes/no) \n").lower().strip()
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("\nInvalid answer, please enter 'yes' or 'no'.")


def play_quiz():
    user_level = ""

    # user chooses the level of the quiz
    level_chosen = quiz_level(user_level)

    # load the questions of the level
    quiz_questions = questions_level(level_chosen)

    # the number of questions
    total_questions = len(quiz_questions)

    # the quiz starts
    score = start_quiz(quiz_questions)

    # display the score of the quiz
    score_quiz(score, total_questions)


def quiz_level():
    """Prompts the user to choose the level of the quiz.
    Returning the value of the user_level """

    while True:
        try:
            print("1- Easy  2- Medium  3- Hard  (Type exit to quit)")
            level = input("What level do you wanna play? ").lower().strip()
            if level == "exit":
                print("\nSee you next time, Goodbye")
                exit()

            if level == "1":
                print("You choose Easy")
                user_level = "1"
                break
            elif level == "2":
                print("You choose Medium")
                user_level = "2"
                break
            elif level == "3":
                print("You choose Hard")
                user_level = "3"
                break
            else:
                print("\nWrong option, choose between 1, 2 or 3!\n")

        except KeyboardInterrupt:
            print("\nTo quit the quiz, type exit !\n")
    return user_level


def questions_level(level_chosen):
    """Get the pack of questions chosen by the user"""

    if level_chosen == "1":
        return level1_questions
    elif level_chosen == "2":
        return level2_questions
    elif level_chosen == "3":
        return level3_questions


def start_quiz(quiz_questions):
    """Give the questions of the quiz and prompts the user for the answers."""

    score = 0

    for question in quiz_questions:
        print("\nQuestion:", question["question"])
        for idx, option in enumerate(question["options"], start=1):
            print(f"{idx}. {option}")

        user_answer = input("Enter the number corresponding to your answer: ").lower().strip()


        # Users exit option during the quiz
        if user_answer == "exit":
            print("\nYou exit The Super Quiz!\nSee you next time, Goodbye")
            exit()

        if user_answer.isdigit() and 1 <= int(user_answer) <= len(question["options"]):
            user_answer_index = int(user_answer) - 1
            if question["options"][user_answer_index] == question["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {question['answer']}")
        else:
            print("Invalid answer, next question.")

    return score


def score_quiz(score, total_questions):
    """Prints out the final score of the user"""

    print(f"\nYour score is {score}/{total_questions}")
    fraction = score / total_questions
    grade = fraction * 100
    print(f"Your final grade is {round(grade)}%")


if __name__ == "__main__":
    main()
