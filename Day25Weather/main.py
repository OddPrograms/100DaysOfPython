# with open("weather_data.csv") as weather_csv:
#     data = weather_csv.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as weather_csv:
#     data = csv.reader(weather_csv)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         else:
#             pass
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)
print()

temp_list = data["temp"].to_list()
print(len(temp_list))
print()

# temp_total = 0
# for item in temp_list:
#     temp_total += item
# average_temp = temp_total / len(temp_list)

# average_temp = sum(temp_list) / len(temp_list)
# print(round(average_temp, 2))

print(round(data["temp"].mean(), 2))
print(data["temp"].max())
print()

# Get Data in Columns
# print(data["condition"])
print(data.condition)
print()

# Get Data in Row Monday
print(data[data.day == "Monday"])
print()

# Get Row for Max Temp
print(data[data.temp == data.temp.max()])
print()

# Store Monday's info to monday variable
monday = data[data.day == "Monday"]

# Print Monday Temp in C and F
print(f"C: {int(monday.temp)} F: {int((monday.temp * 9/5) + 32)} ")

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

student_data = pandas.DataFrame(data_dict)
print(student_data)
student_data.to_csv("new_data.csv")