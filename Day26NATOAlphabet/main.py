import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = data.to_dict()

# Convert csv to dictionary
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# Enter a word to generate a list of NATO phonetic words per user input
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
