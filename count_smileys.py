def count_smileys(arr):
    count = 0
    eyes = [":", ";"]
    noses = ["-", "~", ""]
    mouths = [")", "D"]
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                cmplt = eye + nose + mouth
                count += arr.count(cmplt)
    return count
print(count_smileys([':D',':~)',';~D',':)']))