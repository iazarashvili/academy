# 1 davaleba

# num = int(input('შეიყვანეთ რიცხვი '))
#
# if num % 2 == 0:
#     print('this number is even')
# else:
#     print('This number is odd')

# 2 davaleba
#
# word = 'giorgi middledeveloper aslanishvili aristall smallboy and is aris middledeveloper'
#
# repair_words = ['middle', 'small', 'tall']
#
# if True:
#     for text in repair_words:
#         if text in word:
#             print(text)
#             break
#         else:
#             print('not search')

# 3 davaleba

def calculator(first_num, operator, second_num):
    if operator == '+':
        return first_num + second_num
    if operator == '-':
        return first_num - second_num
    if operator == '/':
        return first_num / second_num
    if operator == '*':
        return first_num * second_num


first_num = float(input('შეიყვანეთ პირველი რიცხვი '))
operator = input('შეიყვანეთ მოქმედება ')
second_num = float(input('შეიყვანეთ მეორე რიცხვი '))

sum = calculator(first_num, operator, second_num)
print(sum)







