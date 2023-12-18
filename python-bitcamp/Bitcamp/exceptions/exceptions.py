# def main_func():
#     print(f'your input is {get_input()}')
#
#
# def get_input():
#     while True:
#         try:
#             return  int(input("What is your number? "))
#         except ValueError:
#             print('Your number is not an integer! ')
#
#
# main_func()


my_list = []

while True:
    try:
        number = input('Write number ')
        my_list.append(number)
    except EOFError:
        print(my_list)
        break
