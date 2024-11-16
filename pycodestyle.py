#!/usr/bin/python3
"""
This module demonstrates a simple Python class with pycodestyle compliance.
The purpose of this module is to demonstrate basic Python structure and
PEP 8 formatting.
"""

from datetime import datetime


class Student:
    """
    A class that represents a student with a name and date of birth.

    Attributes:
        name (str): The name of the student.
        dob (datetime): The date of birth of the student.
    """

    def __init__(self, name, dob):
        """
        Initializes a new Student object with the given name and date of birth.

        Args:
            name (str): The name of the student.
            dob (datetime): The student's date of birth.
        """
        self.name = name
        self.dob = dob

    def get_age(self):
        """
        Calculates the current age of the student based on the date of birth.

        Returns:
            int: The age of the student in years.
        """
        today = datetime.today()
        age = today.year - self.dob.year

        if (today.month < self.dob.month or
                (today.month == self.dob.month and today.day < self.dob.day)):
            age -= 1

        return age

    def __str__(self):
        """
        Returns a string representation of the Student object.

        Returns:
            str: The string format of the Student's name and age.
        """
        return f"{self.name} is {self.get_age()} years old."


def main():
    """
    Main function that creates a Student instance and prints its details.
    """
    student_dob = datetime(2000, 5, 15)
    student = Student("John Doe", student_dob)

    print(student)


if __name__ == "__main__":
    main()
