def triangle(row):
    column_arr = []
    for num in range(row-1):
        column = (2 * num) + 1
        column_arr.append(column)
        column_reverse = column_arr[::-1]
    for unit in column_reverse:
        print(unit * "*")
    
triangle(6)