import pandas as pd

def main() -> None:
    #Reading the nato phonetic csv and obtaining a dictionary with letter and code
    words_df = pd.read_csv('nato_phonetic_alphabet.csv')
    Nato_dict = {row.letter:row.code for (index,row) in words_df.iterrows()}
    
    while(True):
        #Getting name from user and getting codes for the letters present in name
        try:
            name = input("Enter the name:\n").upper()
            Nato_list = [Nato_dict[letter] for letter in name]
            print(Nato_list)
            break
        except KeyError:
            print("Sorry, only letters in the alphabet please.")


if __name__ == "__main__":
    main()