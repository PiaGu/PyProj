#Egen uppgift


def my_function_sum_list(numbers_to_sum):
    total=0
    for i in numbers_to_sum:
        total = total +i
        print(total)
        print(f"Just nu är summan: {total}")
    return total

#skapa en lista
numbers = [1, 2, 3, 4, 3]
total_sum = my_function_sum_list(numbers)
print(f"Den totala summan blir: {total_sum}")