# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()

# table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Nidhi"])
# table.add_column("Type", ["Electric", "Water", "Fire"])

# table.align = "c"
# print(table)

def check_distinct(data_list):
 if len(data_list) == len(set(data_list)):
   
   return True
 else:
   return False;
print(check_distinct([1,6,5,8]))