with open("./Input/Letters/starting_letter.txt") as letters_file:
    letter =  letters_file.read()

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

for name in names:
    name = name.strip()
    personalized_letter = letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.docx",mode="w") as letter_file:
        letter_file.write(personalized_letter)
