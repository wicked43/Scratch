def dirReduc(arr):
    new = []
    for i in range(len(arr)):
        if i == len(arr):
            new.append(arr[i])
        if arr[i] == "NORTH" and arr[i+1] != "SOUTH":
            new.append("NORTH")
        if arr[i] == "EAST" and arr[i+1] != "WEST":
            new.append("EAST")
        if arr[i] == "SOUTH" and arr[i+1] != "NORTH":
            new.append("SOUTH")
        if arr[i] == "WEST" and arr[i+1] != "EAST":
            new.append("WEST")
    return new
a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))
