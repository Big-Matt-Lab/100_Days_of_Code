# with open("weather_data.csv") as weather_data:
#     weather = weather_data.readlines()
# print(weather)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if int(row[1].isnumeric()):
#             temperatures.append(int(row[1]))
#         print(temperatures)

import pandas as pd


# data = pd.read_csv("weather_data.csv")

# # temp_list = data['temp'].to_list()
# # temp_items = len(temp_list)
# # avg_temp = sum(temp_list) / temp_items
# # print(f"The average temperature was {avg_temp:.1f} C.")
# # print(f"The high temperature was {data['temp'].max()} C.")
# monday = data[data.day == 'Monday']
# monday_temp = monday.temp[0]
# temp_in_F = monday_temp * 9 / 5 + 32
# print(f"Mondays temperature was {temp_in_F} F.")

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)
# print(data.students[0])

data = pd.read_csv("squirrel_data.csv")


gray_count = (data["Primary Fur Color"] == "Gray").sum()
black_count = (data["Primary Fur Color"] == "Black").sum()
cinnamon_count = (data["Primary Fur Color"] == "Cinnamon").sum()

fur_color_dict = {
    'fur colors': ['gray', 'black', 'cinnamon'],
    'counts': [gray_count, black_count, cinnamon_count]
    }

color_count = pd.DataFrame(fur_color_dict)
color_count.to_csv("squirrel_colors.csv",index = False)

