import pandas as pd

def main() -> None:
    #Reading the csv file
    squirrel_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

    #Counting the squirrels with different furs
    gray_squirrel = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
    cinnamon_squirrel = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])
    black_squirrel = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])

    #Creating dictionary to create new dataframe
    data_dict ={
        'Fur Color':['Gray', 'Cinnamon', 'Black'],
        'Count':[gray_squirrel, cinnamon_squirrel, black_squirrel]
    }

    #Converting dict to dataframe and dataframe to csv
    data = pd.DataFrame(data_dict)
    data.to_csv("FurColorCount.csv")

if __name__ == "__main__":
    main()