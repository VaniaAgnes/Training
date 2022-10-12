matrix_1= eval(input("Put the matrix numbers :"))

f_list = []

for i in range(len(matrix_1[0])):
    w_list = []
    for y in matrix_1:
        w_list.append(y[i])
    f_list.append(w_list)
print(f"Result: {f_list}")