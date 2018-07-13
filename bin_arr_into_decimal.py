def binary_array_to_number(arr):
    new_arr = []
    for i in arr:
        new_arr.append(i)

    output = int("".join(str(x) for x in new_arr),2)
    return output
st_arr = [1,0,1,1]
print(binary_array_to_number(st_arr))
