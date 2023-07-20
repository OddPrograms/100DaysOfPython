import random
import pandas

# Dictionary Comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

def main():
    names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

    # Loop through list to generate new dictionary.
    students_scores = {student:random.randint(1, 100) for student in names}
    print(f"{students_scores}\n")

    # Loop through dictionary to generate new dictionary
    passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
    print(f"{passed_students}\n")

    #
    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

    sentence_letter_dict = {word:len(word) for word in sentence.split()}
    print(f"{sentence_letter_dict}\n")

    weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
    }

    weather_f = {day:(temperature * 9/5) + 32 for (day, temperature) in weather_c.items()}
    print(f"{weather_f}\n")


    student_dict = {
        "student": ["Angela", "James", "Lily"],
        "score": [56, 76, 98]
    }

    # Looping through dictionaries:
    # for (key, value) in student_dict.items():
    #     print(value)

    student_data_frame = pandas.DataFrame(student_dict)
    print(f"{student_data_frame}\n")

    # Loop through DataFrame
    # for (key, value) in student_data_frame.items():
    #     print(value)

    # Loop through rows of DataFrame instead of columns
    for (index, row) in student_data_frame.iterrows():
        print(row.student)
        if row.student == "Angela":
            print(row.score)

if __name__ == "__main__":
    main()
