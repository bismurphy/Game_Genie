code_string = input("Enter Game Genie code: ")

letter_dict = {'A':0x0, 'P':0x1, 'Z':0x2, 'L':0x3, 'G':0x4, 'I':0x5, 'T':0x6, 'Y':0x7, 'E':0x8, 'O':0x9, 'X':0xA, 'U':0xB, 'K':0xC, 'S':0xD, 'V':0xE, 'N':0xF}

code = []
for c in code_string:
        code += [letter_dict[c]]
#Address is 2 bytes. First bit is set to 1.
address = 0x8000 + \
    ((code[3] & 0b00000111) << 12) \
    | ((code[4] & 0b00001000) << 8)\
    | ((code[5] & 0b00000111) << 8)\
    | ((code[1] & 0b00001000) << 4)\
    | ((code[2] & 0b00000111) << 4)\
    |  (code[3] & 0b00001000)      \
    |  (code[4] & 0b00000111)      \
    
data = \
    ((code[0] & 0b00001000) << 4)\
  | ((code[1] & 0b00000111) << 4)\
  | (code[-1] & 0b00001000)      \
  | (code[0] & 0b00000111)         

if len(code) == 8:
    compare = \
    ((code[6] & 0b00001000) << 4)\
  | ((code[7] & 0b00000111) << 4)\
  | (code[5] & 0b00001000)       \
  | (code[6] & 0b00000111)       
    print(hex(compare))
print("Address: " + hex(address))
print("Data: " + hex(data))
