def averageCalculation(numList):
    sum_profit = 0
    divider = 0
    for number in numList:
        sum_profit += number
        divider += 1    
    end_profit = sum_profit/divider
    return end_profit

_finish = False

while _finish is False:
    try:
        _input_number = str(input("Enter number: "))
        _number_list = list(map(int, _input_number.split(" ")))
        _end_profit = averageCalculation(_number_list)
        print(f"{_end_profit}")
        _finish = True
    except ValueError:
        print("Please input only number!")