def main():
        # List comprehension
        # Add 2 per num in list
        numbers = [1, 2, 3, 4]
        new_numbers = [n + 2 for n in numbers]
        print(new_numbers)

        # Multiple each num in list by 2
        numbers_doubled = [num * 2 for num in range(1, 5)]
        print(numbers_doubled)


        names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

        # Make new list of short names only from names list
        short_names = [name for name in names if len(name) < 5]
        print(short_names)

        # Make new list of long names only from names list in all caps
        long_names = [name.upper() for name in names if len(name) > 5]
        print(long_names)

        # Square every number in list
        numbers_two = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        squared_numbers = [num**2 for num in numbers_two]
        print(squared_numbers)

        # Make a new list with only even numbers
        numbers_three = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        evens = [num for num in numbers_three if num % 2 == 0]
        print(evens)

        # Make list that contains ints from both file1.txt and file2.txt
        file_one_list = []
        file_two_list = []

        # Open file1.txt and strip each line, append each line as int to file_one_list
        with open('file1.txt', 'r') as file_one:
                for item in file_one:
                        stripped_item = item.strip()
                        file_one_list.append(int(stripped_item))

        # Open file2.txt and strip each line, append each line as int to file_two_list
        with open('file2.txt', 'r') as file_two:
                for item in file_two:
                        stripped_item = item.strip()
                        file_two_list.append(int(stripped_item))

        compared_lists = [num for num in file_one_list if num in file_two_list]
        print(compared_lists)

if __name__ == "__main__":
        main()
