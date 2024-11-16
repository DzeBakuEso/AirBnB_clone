#!/usr/bin/python3
"""
This module represents a student with name and date of birth.
It contains a method to calculate the age of the student.
"""

from datetime import datetime
import unittest


class Student:
    """
    A class representing a student.

    Attributes:
        name (str): The name of the student.
        dob (datetime): The date of birth of the student.
    """

    def __init__(self, name, dob):
        """
        Initializes a new Student object.

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

        if today.month < self.dob.month or (
           today.month == self.dob.month and today.day < self.dob.day):
            age -= 1

        return age

    def __str__(self):
        """
        Returns a string representation of the Student object.

        Returns:
            str: The string format of the Student's name and age.
        """
        return f"{self.name} is {self.get_age()} years old."
