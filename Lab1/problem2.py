#! usr/bin/pyhton3
def single_element():
    my_list = [1, 2, 2, 3, 2,1,1,3]
    final_list = []
    for i in my_list:
        if i not in final_list:
            final_list.append(i)
    print(final_list)
single_element()