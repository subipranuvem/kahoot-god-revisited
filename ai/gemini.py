import google.generativeai as genai
import os
from ai.env_var_keys import EnvironmentVarKey


class GeminiQuizSolver:
    def __init__(self):
        genai.configure(api_key=os.environ[EnvironmentVarKey.GEMINI_API_KEY])
        model = "gemini-1.5-flash"
        env_model = os.environ[EnvironmentVarKey.GEMINI_MODEL]
        if env_model != "":
            model = env_model
        print(f"ai model loaded: {model}")
        self._model = genai.GenerativeModel(model)

    def solve_quiz(self, question_and_alternatives: str) -> int:
        res = self._model.generate_content(
            f"""
            You are a helpful assistant specialized in answering multiple-choice questions who only responds with the button number corresponding to the most likely answer do not respond with words only a integer.
            You'll do this even if the question involves content you can't analyze, such as videos or images. 
            If you cannot answer the question, you'll respond with an educated guess.
            Remember only respond with an integer between 1 and 4 that corresponds to the answer.
            The question an the alternatives is:
            {question_and_alternatives}
            """
        )
        guess = int(res.text)
        if guess > 4 or guess < 0:
            raise ValueError("guess is not between [0-4]")
        return guess
