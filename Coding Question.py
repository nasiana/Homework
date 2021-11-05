"""
Nasian Ahmed
Coding Question
"""

# my_numbers = [5, 6, 9, 3, -2, 7, -4, 5]
# my_sum = 12

my_numbers = [5, 6, 9, 3, -2, 7, -4, 5]
my_sum = 12
result = []

def Two_Number_Sum(my_numbers):
    for i in range(len(my_numbers)):
        for j in range(len(my_numbers)):
            if my_numbers[i] + my_numbers[j] == my_sum and i != j:
                if not [(my_numbers[i]), (my_numbers[j])] in result:
                    result.append([(my_numbers[i]), (my_numbers[j])])
    return result

print(Two_Number_Sum(my_numbers))

def Sum_Unique():
    result = Two_Number_Sum(my_numbers)
    unique_result = {x for l in result for x in l}
    unique_result_list = list(unique_result)
    unique_result_formatted = []
    i = 0
    while i < len(unique_result):
        unique_result_formatted.append([unique_result_list[i], unique_result_list[i+1]])
        i += 2
    return unique_result_formatted

print(Sum_Unique())

