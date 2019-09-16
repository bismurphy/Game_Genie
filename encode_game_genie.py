address = int(input("Enter desired address: "),0)
data = int(input("Enter desired data: "),0)
compare = input("Enter desired compare (optional): ")

letter_dict = {0: 'A', 1: 'P', 2: 'Z', 3: 'L', 4: 'G', 5: 'I', 6: 'T', 7: 'Y', 8: 'E', 9: 'O', 10: 'X', 11: 'U', 12: 'K', 13: 'S', 14: 'V', 15: 'N'}
codestring = ""

codestring += letter_dict[((data    >> 4) & 0b00001000) | ((data >> 0) & 0b00000111)]
codestring += letter_dict[((address >> 4) & 0b00001000) | ((data >> 4) & 0b00000111)]
#Position #2 doesn't have its top bit defined anywhere. This allows for two choices. I choose the low one.
codestring += letter_dict[((address >> 4) & 0b00000111)]
codestring += letter_dict[((address >> 0) & 0b00001000) | ((address >> 12) & 0b00000111)]
codestring += letter_dict[((address >> 8) & 0b00001000) | ((address >> 0) & 0b00000111)]

if len(compare) == 0:
    codestring += letter_dict[((data >> 0) & 0b00001000) | ((address >> 8) & 0b00000111)]

else:
    compare = int(compare,0)
    codestring += letter_dict[((compare >> 0) & 0b00001000) | ((address >> 8) & 0b00000111)]
    codestring += letter_dict[((compare >> 4) & 0b00001000) | ((compare >> 0) & 0b00000111)]
    codestring += letter_dict[((data >> 0) & 0b00001000) | ((compare >> 4) & 0b00000111)]

print(codestring)
