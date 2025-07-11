"""
TASK ONE

"""
# pylint: disable=too-few-public-methods


from datetime import date


class Trainee:
    """CLASS FOR TRAINEE"""

    def __init__(self, name: str, email: str, date_of_birth: date):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = []

    def get_age(self):
        """METHOD TO GET AGE"""
        today = date.today()
        return today.year - self.date_of_birth.year

    def add_assessment(self, assessment):
        """METHOD TO ADD ASSESSMENT"""
        self.assessments.append(assessment)

    def get_assessment(self, name: str):
        """METHOD TO GET ASSESSMENT"""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None


class Assessment:
    """CLASS FOR ASSESSMENT"""

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
