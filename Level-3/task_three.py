
from datetime import date
"""
Finally, let's create a `Marking` class that will help us to mark assessments.

## 1. Marking

In `task_three.py` you'll find the beginnings of a `Marking` class. Update it to have the following:

- `__init__(self, quiz: Quiz)`
  - This method should take a `Quiz` object and store it in a private variable called `_quiz`.
- `mark(self) -> int`
  - This method should return the total score for the assessment as a percentage, rounded to zero decimal places (i.e. an `int`).
  - Each correct answer is worth a single point
  - This function must **not** throw any errors
- `generate_assessment(self) -> Assessment`
  - This should return an instance of an `Assessment` of the correct subclass with the correct name and score.
    - e.g. If the quiz is a `multiple-choice` then this should return a `MultipleChoiceAssessment`. 
    If it is a `technical` quiz then this should return a `TechnicalAssessment` etc

A quiz can contain any number of questions from 0 to 100.

## Note

Due to the way that that default arguments are stored in Python, you should not use mutable default arguments in your function signature. This means that **you should not use `[]` or `{}` as default arguments** in your functions as **this will break the tests.**


"""


class Trainee:
    def __init__(self, name: str, email: str, date_of_birth: date):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = []

    def get_age(self):
        today = date.today()
        return today.year - self.date_of_birth.year

    def add_assessment(self, assessment):
        if not isinstance(assessment, Assessment):
            raise TypeError("Invalid type of assessment")
        self.assessments.append(assessment)

    def get_assessment(self, name: str):
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None

    def get_assessment_of_type(self, type: str) -> list:
        count = []
        for assessment in self.assessments:
            if assessment.type == type:
                count.append(assessment)
        return count


class Assessment:
    def __init__(self, name: str, type: str, score: float):
        types = ["multiple-choice", "technical", "presentation"]
        self.name = name
        if type not in types:
            raise ValueError("Invalid type of assessments")
        self.type = type
        if score < 0 or score > 100:
            raise ValueError("Outside 0-100 range")
        self.score = score


class MultipleChoiceAssessment(Assessment):
    def __init__(self, name: str, score: int):
        type = "multiple-choice"
        super().__init__(name, type, score)

    def calculate_score(self):
        return self.score*0.70


class TechnicalAssessment(Assessment):
    def __init__(self, name: str, score: int):
        type = "technical"
        super().__init__(name, type, score)

    def calculate_score(self):
        return self.score


class PresentationAssessment(Assessment):
    def __init__(self, name: str, score: int):
        type = "presentation"
        super().__init__(name, type, score)

    def calculate_score(self):
        return self.score*0.60


class Question:

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:

    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:

    def __init__(self, quiz: Quiz) -> None:
        self._quiz = quiz

    def mark(self):
        total = 0
        if len(self._quiz.questions) == 0:
            return total
        for question in self._quiz.questions:
            if question.chosen_answer == question.correct_answer:
                total += 1
        return (total/len(self._quiz.questions)) * 100

    def generate_assessment(self) -> Assessment:
        if self._quiz.type == "multiple-choice":
            assessment = MultipleChoiceAssessment(self._quiz.name, self.mark())
        if self._quiz.type == "technical":
            assessment = TechnicalAssessment(self._quiz.name, self.mark())
        if self._quiz.type == "presentation":
            assessment = PresentationAssessment(self._quiz.name, self.mark())

        return assessment


if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code
