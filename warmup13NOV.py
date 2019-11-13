import json 
import pandas as pd 
from pprint import pprint 

x = {
    "Floor": 6,
    "Instructors": [
        {"name": "Ryan", "favoriteLanguages": ["python", "clojure"]},
        {"name": "Maggie", "favoriteLanguages": ["python", "R", "java"]},
        {"name": "David", "favoriteLanguages": ["python", "matlab"]},
        {"name": "Zach", "favoriteLanguages": ["python", "bash"]}
    ],
    "Location": "Blanco",
    "Students": [
        {"name": "Sally", "examGrades": [62, 85, 80]},
        {"name": "Jane", "examGrades": [88, 79, 67]},
        {"name": "Suzie", "examGrades": [94, 74, 95]},
        {"name": "Billy", "examGrades": [98, 96, 88]},
        {"name": "Ada", "examGrades": [77, 92, 98]},
        {"name": "John", "examGrades": [79, 76, 93]},
        {"name": "Thomas", "examGrades": [82, 64, 81]},
        {"name": "Marie", "examGrades": [93, 63, 90]},
        {"name": "Albert", "examGrades": [92, 62, 87]},
        {"name": "Richard", "examGrades": [69, 80, 94]},
        {"name": "Isaac", "examGrades": [92, 99, 93]},
        {"name": "Alan", "examGrades": [92, 62, 72]}
    ],
    "isActive": True
}

#1
# Copy the data below and save it as bayes.json

with open('bayes.json', 'w') as json_file:
    json.dump(x, json_file)
#2
#Import the json module and use the json.load function to read the bayes.json file you created.

with open('./bayes.json') as f:
    bayes = json.load(f)
#bayes is a dictionary

#

# Write the code necessary to answer the following questions:

#     Print out a message that gives the location of the class using the location and the floor properties.
def show_location():
    print(f"The class is on the {Floor}th floor in the {bayes['Location']} classroom.")


#     If the class is active, print a message that says so.
def is_active():
    if bayes['isActive'] == True:
        print("Bayes is active.")

#     Print out the number of students and number of instructors.
def count_students_and_instructors():
    instructors = [i['name'] for i in bayes['Instructors']]
    students = [i['name'] for i in bayes['Students']]
    print (f"There are {len(instructors)} students and {len(students)} instrutors.")

#     Print out the name of the instructor that has the most favorite languages.
filler=0
def most_languages():
    instructors = bayes['Instructors']
    for i in instructors:
        if filler < len(i['favoriteLanguages']):
            filler = len(i['favoriteLanguages'])
            name = i['name']
    return name

#the winner!
def most_favorites():
    instructors = bayes['Instructors']
    return max(instructors, key=lambda instructor: len(instructor['favoriteLanguages']))

#     Import pandas and create a dataframe from the student data. What do you notice?

# students = bayes['Students']
# pd