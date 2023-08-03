# # FileNotFound
# with open("a_file.txt) as file:
#       file.read()

# # Tries to attempt the following code, depending on outcome moves to next stage
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key_one"])
# # Throws error when file not found
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# # Throws error when key not found and saves to error_message
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# # Occurs if no errors thrown
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed.")
#     raise TypeError("This is an error I made up.")

# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")
#
#
# bmi = weight / height ** 2
# print(bmi)


# # KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# # IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# # TypeError
# text = "abc"
# print(text + 5)

fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    fruit = fruits[index]
    print(fruit + "Pie")

try:
    make_pie(4)
except IndexError:
    print("Fruit Pie")
else:
    print(fruit + "Pie")


facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)