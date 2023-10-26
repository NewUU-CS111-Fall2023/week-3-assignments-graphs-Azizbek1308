# * Author:
# * Date:
from task3 import transformation
print("Task3")
number = transformation()
x, y = map(int, input("Please enter the two numbers! For example: 2 162 \n").split(' '))
res1 = []
step1 = 0
number.transformation(x, y, res1, step1)