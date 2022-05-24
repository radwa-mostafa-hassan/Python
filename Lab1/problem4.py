#! usr/bin/python3
from collections import Counter

file_name = input("Enter Name of File : ")
file_name = file_name+".txt"
my_list = []
f = open(file_name, "r")
data =f.read() 
my_list=data.split()
# print(my_list)
count = Counter(my_list)
result = count.most_common(1)
# print(result)

new_file = open("popular_words.txt","w")
for popular_words in result:
    new_file.write(popular_words + "\n")
f.close()