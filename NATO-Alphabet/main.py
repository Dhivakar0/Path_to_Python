import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')

df_dict = {row.letter:row.code for index,row in df.iterrows()}

def generate():
    user_word = input("Enter the word: ").upper()
    try:
        phonetic_code = [df_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry! Only Alphabets please...")
        generate()
    else:
        print(phonetic_code)

generate()
