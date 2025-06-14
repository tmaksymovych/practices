list_of_lists = [[1,6],[2,13],[0,16]]
print("List of lists:", list_of_lists)

# single_list = list_of_lists[0] + list_of_lists[1] + list_of_lists[2]
# print(single_list)

for i in range(len(list_of_lists)):
    single_list = []
    single_list.append(i)
    print(single_list)
