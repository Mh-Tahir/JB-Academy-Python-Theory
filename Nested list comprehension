student_list = []
for class_group in school:
    for student in class_group:
        student_list.append(student)
# Equal to:
student_list = [student for class_group in school for student in class_group]

'''matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]'''
matrix = [] 
for i in range(2):   
    # create empty row (a sublist inside our list)
    matrix.append([])  
    for j in range(5): 
        matrix[i].append(j)
# Equal to:
matrix = [[j for j in range(5)] for i in range(2)]

# [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]]
my_list = [[x for x in range(1, 3)] for _i in range(5)]

# Saves the winners to a list and calculates the total number of victories
n = int(input())
b = [a[0] for a in [input().split() for x in range(n)] if a[1] == 'win']
print(b)
print(len(b))

# Selects students with the grade A and prints their names in a list
students = [["Will", "B"], ["Kate", "B"], ["Max", "A"], ["Elsa", "C"], ["Alex", "B"], ["Chris", "A"]]
print([a[0] for a in students if a[1] == "A"])
