def printlist(my_list):
    if len(my_list) == 0:
        return
    print(my_list.pop(0))
    index = len(my_list) - 1
    if index < 0:
        print("Конец списка")
    printlist(my_list)


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
printlist(my_list)