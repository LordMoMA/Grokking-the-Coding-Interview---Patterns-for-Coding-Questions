# find if there are three numbers in three lists that add up to 12
def find_twelve(num_list1, num_list2, num_list3):
    for num1 in num_list1:
        for num2 in num_list2:
            for num3 in num_list3:
                if num1 + num2 + num3 == 12:
                    return num1, num2, num3
