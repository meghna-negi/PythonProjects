def main() -> None:
    PLACEHOLDER = '[name]'
    #Opening the file with names of people
    with open("./Input/Names/invited_names.txt") as NameFile:
        names = NameFile.read()

    #Converting the content of file with names to list
    invited_list = names.split("\n")

    #Opening the file with template letter for reading it
    with open("./Input/Letters/starting_letter.docx",mode='r') as LetterTemplate:
        letter = LetterTemplate.read()

        #Replacing the name placeholder with the names on the list
        #Write the modified letter to a new loaction with name of person included in filename
        for name in invited_list:
            new_letter = letter.replace(PLACEHOLDER,name)
            with open(f"./Output/ReadyToSend/letter_for_{name}.docx",mode='w') as FinalLetter:
                FinalLetter.write(new_letter)

if __name__ == "__main__":
    main()