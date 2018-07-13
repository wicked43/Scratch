def data_reverse(data):
    new = []
    for i in range(len(data)-8, -1, -8):
        new.extend(data[i:i+8])
    return new

data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
print(data_reverse(data1))