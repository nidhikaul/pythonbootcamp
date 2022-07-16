student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}


#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # print(key,value)
#     pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(index,row)
    # print(row.score)
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


word = input("Enter a word:").upper()
try:
    output_list = [phonetic_dict[letter] for letter in word]
except KeyError:
    print("Please enter alphabets only")
    word = input("Enter a word: ").upper()
else:
    print(output_list)

