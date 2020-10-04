my_list = [7, 5, 3, 3, 2]
print(my_list)
number = int(input('Введите число : '))
for el in range(len(my_list)):
    if my_list[el] == number:
        my_list.insert(el + 1, number)
        break
    elif my_list[0] < number:
        my_list.insert(0, number)
        break
    elif my_list[-1] > number:
        my_list.append(number)
        break
    elif my_list[el] > number > my_list[el + 1]:
        my_list.insert(el + 1, number)
        break

print(my_list)