# from turtle import Turtle, Screen
#
# pippo = Turtle()
# pippo.shape("turtle")
# pippo.color("gold1")
# pippo.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
(table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur"]),
 table.add_column("Type", ["Electric", "Water", "Fire", "Grass"]))
table.align = "l"
print(table)