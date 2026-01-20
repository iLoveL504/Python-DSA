import pandas as pd
import sys
import re

url = "https://raw.githubusercontent.com/codebasics/data-structures-algorithms-python/refs/heads/master/data_structures/4_HashTable_2_Collisions/Solution/nyc_weather.csv"

df = pd.read_csv(url)
# print(df.head())

arr = df['temperature(F)'].tolist()

temp_dict = dict(zip(df['date'], df['temperature(F)']))

# What was the average temperature in first week of Jan
print(sum(arr)/len(arr))

# What was the maximum temperature in first 10 days of Jan
print(max(arr))

print(temp_dict)
# What was the temperature on Jan 9
print(temp_dict['Jan 9'])
# What was the temperature on Jan4
print(temp_dict['Jan 4'])

# poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You 
# have to read this file in python and print every word and its count as show 
# below. Think about the best data structure that you can use to solve this problem and 
# figure out why you selected that specific data structure.
word_count = {}
with open('poem.txt', 'r') as file:
    
    lines = file.readlines()
    print(lines)
    for line in lines:
        tokens = line.replace(',', ' ').replace('\n', ' ').replace('.', ' ').replace('\"', ' ').split(' ')
   
        print(tokens)