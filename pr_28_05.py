# a = list(map(int, input().split()))
# print(len(a))



def select(grades: list, passgrade = 60) -> list:
    """
    функція шось робить
    """
    result = []
    for el in grades:
        if el >= passgrade:
            result.append(el)
    return result
    


gradebook = {"yehal": [34,34,67,89,52],
             "horra": [34,78,234,100],
             "asdafd":[23,6,7,8]}


print(select(gradebook["horra"], 30))

for key in gradebook:
    el_l_60 = select(gradebook)
    print(f"{key}:", *el_l_60, f" {el_l_60}.average : {sum(el_l_60)/len(el_l_60)}")



# for key in gradebook:
#     print(key, gradebook[key])

# for i in gradebook.values():
#     print(i)



