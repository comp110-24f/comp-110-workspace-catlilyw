def number_info(num: int) -> int:
    if num < 10:
        print("small number")
    else:
        if num % 2 == 0:
            print("even number")
        else:
            print("odd number")
    return num


number_info(num=11)
print(number_info(num=4))
