# * Author:
# * Date:
from task3 import transformation
from task4 import Genome
print("Task3")
number = transformation()
x, y = map(int, input("Please enter the two numbers! For example: 2 162 \n").split(' '))
res1 = []
step1 = 0
number.transformation(x, y, res1, step1)
print("Task4")
obj=Genome()
obj.Genome(int(input("Please enter the number of genome fragments \n")),str(input("Please enter 1 descriptions of a fragment\n")))