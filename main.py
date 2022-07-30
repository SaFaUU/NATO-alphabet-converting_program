import pandas

nato_read = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data = pandas.DataFrame(nato_read)


data_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}


while True:
    user_input = input("Enter a word: ").upper()
    try:
        phonetic_code = [data_dict[character] for character in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        print(phonetic_code)
