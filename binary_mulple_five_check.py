def binary_five_multiple_check(inp):
    decimal = 0
    dic_binary_decimal = {}
    binary=0
    while True:
        flag = True
        lis = ["2","3","4","5","6","7","8","9"]
        binary_str = str(binary)
        for j in binary_str:
            if j in lis:
                flag = False
                break
        if flag==True:
            dic_binary_decimal[binary_str]=decimal
            decimal+=1
        binary+=1
        if binary_str==inp:
            deci = dic_binary_decimal[binary_str]
            if deci%5==0:
                d = dic_binary_decimal[binary_str]
                print(f"binary number {inp} is a multiple of 5 and decimal value is {d}")
            else:   
                print(inp,"is not a multiple of 5 ,","decimal:",dic_binary_decimal[binary_str])
            break
decimal_y = 0
dic_binary_decimal_y = {}
binary_y=0
range_y = 1000000000000000
for binary_y in range(0,range_y):
    flag = True
    lis = ["2","3","4","5","6","7","8","9"]
    binary_str_y = str(binary_y)
    for j in binary_str_y:
        if j in lis:
            flag = False
            break
    if flag==True:
        binary_five_multiple_check(binary_str_y)