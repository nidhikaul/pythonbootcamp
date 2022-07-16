# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []

#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# average = (data["temp"].mean())

# max_temp = data['temp'].max()
# print(max_temp)

#Get data in row
# monday = (data[data.day == "Monday"])
# print(monday.condition)
# temp_c = int(monday.temp)
# temp_F = (temp_c * (9/5)+32)
# print(temp_F)

#Create a dataframe
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76,56,65]
# }

# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("new_data.csv")

#Max temp
# print(data[data.temp == data['temp'].max()])


import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_gray = len(data[data["Primary Fur Color"] == "Gray"])
print(color_gray)

color_black = len(data[data["Primary Fur Color"] == "Black"])
print(color_black)

color_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(color_cinnamon)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black" ],
    "Count": [color_gray, color_cinnamon, color_black]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel Count.csv")





