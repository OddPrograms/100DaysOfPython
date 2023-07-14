#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def main():
    with open("./Input/Names/invited_names.txt") as names_file:
        names = names_file.readlines()
    print(names)

    with open("./Input/Letters/starting_letter.txt") as letter_file:
        letter_file = letter_file.read()
        for name in names:
            stripped_name = name.strip()
            named_letter = letter_file.replace("[name]", stripped_name)
            with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
                completed_letter.write(named_letter)

if __name__ == "__main__":
    main()
