# a = int(input())
# b = int(input())
# try:
#     a/b
# except ZeroDivisionError:
#     print("b = 0")
#     while b == 0:
#         b = int(input())
# # else:
# #     print(a/b)
# finally:
#     print(a/b)


grade = {
    "horra": [14, 67, 89, 0],
    "hanchick": [34, 67, 89, 23],
    "danas": [34, 73, 83, 62],
    "atrem": [0, 45, 83, 90]
}

# with open ("C:\OOP\practices\pr_11_06\pr_csv.csv", "r") as file:
#     data = [i[:-1] for i in  file.readlines()]
#     print(data)

# with open ("data.csv", "w") as file:
#     file.write("Name, Math, Ukr, Eng, Prog\n")
#     for name in grade:
#         string = f"{name},"
#         for i in grade[name]:
#             string += f"{i},"
#         string += "\n"
#         file.write(string)


with open ("data.csv" , 'r') as file:
    data = [i[:-1] for i in file.readlines()]
    data = [i.split(",") for i in data]
    n = len(data)
    for i in range(1, n):
        data[i] = [int(el) if el.isdigit() else el for el in data[i]]
    print(data)