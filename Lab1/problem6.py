#! usr/bin/python3
string = input("Enter Your String : ")
char = input("Enter your character : ")
index = []
my_list= list(string)
for i in range(len(my_list)):
    if my_list[i] == char:
        index.append(i+1)
print(f"indices of character are {index}")