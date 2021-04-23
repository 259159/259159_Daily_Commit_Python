def change_pos(my_list):
    for i in range(0, len(my_list), 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

        return my_list


my_list = [0, 1, 2, 3, 4, 5]
print("List Before changing position :", my_list)
print("\n After changing the position is ", change_pos(my_list))
