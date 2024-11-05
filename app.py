import keyboard
from dotenv import load_dotenv
from ai.gemini import GeminiQuizSolver
from kahoot_browser.browser import KahootBrowser
from input.url_chooser import URLChooser

# Loading the environment variables in .env file
load_dotenv()

quiz_solver = GeminiQuizSolver()
url = URLChooser.choose_url()

browser = KahootBrowser()
browser.go_to_quiz(url)


def print_divider(char: str = "-", size: int = 40) -> None:
    print(char * size)


def print_intructions() -> None:
    print("Instructions:")
    print(
        "- Press [Ctrl + Shift + Z] when the question appears with all the alternatives to solve it."
    )
    print("- Press [Ctrl + C] or [Ctrl + Z] to quit.")
    print_divider()


def solve_quiz():
    try:
        questions_and_alternatives = browser.get_question_and_alternatives()
        print(f"Question and alternatives:\n\n{questions_and_alternatives}\n")
        guess = quiz_solver.solve_quiz(questions_and_alternatives)
        guess_text = questions_and_alternatives.splitlines()[guess]
        print(f"AI guessed alternative: {guess_text}")
        print(f"Clicking the alternative: {guess_text}")
        browser.click_correct_alternative(guess)
        print_divider()
    except Exception as e:
        print("Can't solve the question :'(")
        print(f"Error: {e}")
        print_divider()


try:
    print_intructions()
    keyboard.add_hotkey("ctrl+shift+z", solve_quiz)

    # Keep the program running
    keyboard.wait()
except KeyboardInterrupt:
    print("I hope you became the Kahoot God!")
    browser.close()
