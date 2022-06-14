# This file is for 202_PA4.py

class Student:
    def __init__(self, number, numCourses, firstName, lastName, gpa):
        self.number = number
        self.numCourses = numCourses
        self.firstName = firstName
        self.lastName = lastName
        self.gpa = gpa
        self.schedule = []

    def print(self):
        print(self.firstName + " " + self.lastName)

    def printSchedule(self):
        pass

    def addCourse(self, course):
        pass

class Course:
    def __init__(self, prefix, number, name):
        self.prefix = prefix
        self.number = number
        self.name = name

    def print(self):
        print(self.prefix + self.number + ": " + self.name )