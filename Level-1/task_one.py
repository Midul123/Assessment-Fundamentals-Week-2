from datetime import date
from datetime import datetime
'''
## 1. Trainee

You should have a `Trainee` class that has the following attributes:

- `name` - str
- `email` - str
- `date_of_birth` - `date` object
- `assessments` - list[Assessment]

It has methods to:

- `get_age() -> int` - returns the age of the trainee in years
- `add_assessment(assessment: Assessment) -> None` - adds an `Assessment` to the trainee's list of assessments
- `get_assessment(name: str) -> Assessment | None` - returns the `Assessment` object that has the name given
  - Return `None` if not found


## 2. Assessment

You should have an `Assessment` class that has the following attributes:

- `name` - str
- `type` - str
  - Can only be `multiple-choice`, `technical` or `presentation`. Throw a ValueError if not.
- score - float (0-100). Throw a ValueError if outside of this range.

## Note

Due to the way that that default arguments are stored in Python, you should not use mutable default arguments in your function signature. This means that **you should not use `[]` or `{}` as default arguments** in your functions as **this will break the tests.**


'''


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
        self.assessments.append(assessment)

    def get_assessment(self, name: str):
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None


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


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
