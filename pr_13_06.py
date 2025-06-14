
import pickle

# grade = {
#     "horra": [14, 67, 89, 0],
#     "hanchick": [34, 67, 89, 23],
#     "danas": [34, 73, 83, 62],
#     "atrem": [0, 45, 83, 90]
# }

with open("data.in", "rb") as file:
    students = pickle.load(file)
print(students)
# with open ("data.csv" , 'r') as file:
#     data = [i[:-1] for i in file.readlines()]
#     data = [i.split(",") for i in data]
#     n = len(data)
#     for i in range(1, n):
#         data[i] = [int(el) if el.isdigit() else el for el in data[i]]
#     print(data)                             
