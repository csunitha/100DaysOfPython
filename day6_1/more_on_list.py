''' day 6 '''

#List comprehension
#filter all grades for a movie posted by users of age 18 or below
'''
class Grade:
    name='',
    age=0
    def __init__(self, name, age):
        self.name=name
        self.age=age


grades = [Grade('Peter',28), Grade('John',18), Grade('Joe',15)]
'''
# WRONG
under_18_grades = []
for grade in grades:
  if grade.age <= 18:
    under_18_grades.append(grade)

#right

under_18_grades = [grade for grade in grades if grade.age > 18]

