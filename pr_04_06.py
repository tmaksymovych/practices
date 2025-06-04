# numbers = [5, 8, 9, 5, 6, 0, 3]
# b = [nums for nums in numbers if nums % 2 != 0]
# print(b)

# table = {number :[number*multiplier for multiplier in range(1, 11)]for number in range(1, 11)}
# print(table)

# names = ["Bob", "Jack", "Nick", "Oleg", "Yevheniy"]
# grades = [[50, 78, 90, 45],
#          [56, 56, 34, 89],
#          [43, 67, 99, 34],
#          [23, 67, 49, 90],
#          [45, 74, 83, 78]
#          ]
# students = {names[grade] :grades[grade] for grade in range(5)}
# print(students)


from random import randint


n_2 = ["iryna", 'taras', "nick", "oleh", "mary"]
students = {name :[randint(60, 80) for a in range(5)] for  name in n_2 }
print(students)