#! usr/bin/python3
string = input("Enter Your String : ")
vowels =['a','e', 'i' ,'o']
result = []
my_list = list(string)
for i in range(len(my_list)):
    for z in range(len(vowels)):
        if vowels[z] in my_list:
            my_list.remove(vowels[z])
print(my_list)
