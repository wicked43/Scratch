def alphabet_position(text):
    text = text.lower()
    text = text.replace(" ", "")
    txt = []
    for i in range(0, len(text)-1):
        if text[i].isalpha() == True:
            txt.append(str(ord(text[i]) - 97))
    return " ".join(txt)

alphabet_position("The sunset sets at twelve o' clock.")