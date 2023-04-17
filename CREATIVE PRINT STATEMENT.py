import pyfiglet as pyg
from termcolor import colored

res1=pyg.figlet_format("Hi, my name is Andrea Ragaas.\nI wanted to be a", font= "term")
print(colored((res1), "blue"))

res2=pyg.figlet_format("Software Engineer", font= "speed")
print(colored((res2), "green"))
