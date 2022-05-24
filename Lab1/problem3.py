#! usr/bin/python3
my_string = input("Enter your string : ")
front = []
back = []
if (len(my_string)%2==0):
    for i in range(len(my_string)):
        front = my_string[:int((len(my_string)/2))]
        back = my_string[int((len(my_string)/2)):]
else :
    for i in range(len(my_string)):
        front = my_string[:(int((len(my_string)/2)+1))]
        back = my_string[(int((len(my_string)/2)+1)):]

final_string="("+str(front)+"-front"+" + "+str(back)+"-front ) + ("+str(front)+"-back"+" + "+str(back)+"-back )"
print(final_string)