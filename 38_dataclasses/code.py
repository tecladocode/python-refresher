from typing import List


class Student:
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")
bob.take_exam(90)
print(bob)

# -- as dataclass --

from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    grades: List[int] = field(
        default_factory=list
    )  # if we want to run a function, use default_factory and it will run the function to generate the default

    def take_exam(self, result):
        self.grades.append(result)


bob = Student("Bob")

bob.take_exam(90)
print(bob.grades)
print(bob)
