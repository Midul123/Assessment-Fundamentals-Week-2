from datetime import date
"""

Next, let's create classes for each of our assessment types so we do OOP in a better way.

## 1. Types of Assessments

Create a class for

- `MultipleChoiceAssessment`
- `TechnicalAssessment`
- `PresentationAssessment`

Each of these classes should inherit from the `Assessment` class and have a `calculate_score()` method that returns a score for the assessment.Each of the Assessment types have different weightings depending on it's type:

- `MultipleChoiceAssessment` - 70%
- `TechnicalAssessment` - 100%
- `PresentationAssessment` - 60%

For example, if a `TechnicalAssessment` has a score of 80, the `calculate_score()` method should return 80. If a `MultipleChoiceAssessment` has a score of 80, the `calculate_score()` method should return 56.

## 2. Edge Cases and Errors

Ensure you check all of your edge cases and throw errors where appropriate.

Throw a `TypeError` if something is added the `assessments` list in the `Trainee` class that is not a subclass of an `Assessment` class.

## 3. Get Assessment of Type

Add a function to `Trainee` class called `get_assessment_of_type(self, type: str) -> list[Assessment]` 
that returns a list of all assessments of a given type. 
The type will be given as a string of either `multiple-choice`, `technical` or `presentation`.

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


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
