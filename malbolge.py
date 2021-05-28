tri = lambda a: [a//(3**(9-x))%3 for x in range(10)]

def crz(a, b):
    table = [
        [1, 0, 0],
        [1, 0, 2],
        [2, 2, 1]
    ]
    digits_c = [table[db][da] for da, db in zip(tri(a), tri(b))]
    result = sum(digits_c[x]*(3**(9-x))for x in range(10))
    return result

rotate = lambda i: i//3+(i%3)*(3**9)

def mal(code):
    encipherment = {0: 57, 19: 108, 38: 113, 57: 91, 76: 79, 1: 109, 20: 125, 39: 116, 58: 37, 77: 65, 2: 60, 21: 82, 40: 121, 59: 92, 78: 49, 3: 46, 22: 69, 41: 102, 60: 51, 79: 67, 4: 84, 23: 111, 42: 114, 61: 100, 80: 66, 5: 86, 24: 107, 43: 36, 62: 76, 81: 54, 6: 97, 25: 78, 44: 40, 63: 43, 82: 118, 7: 99, 26: 58, 45: 119, 64: 81, 83: 94, 8: 96, 27: 35, 46: 101, 65: 59, 84: 61, 9: 117, 28: 63, 47: 52, 66: 62, 85: 73, 10: 89, 29: 71, 48: 123, 67: 85, 86: 95, 11: 42, 30: 34, 49: 87, 68: 33, 87: 48, 12: 77, 31: 105, 50: 80, 69: 112, 88: 47, 13: 75, 32: 64, 51: 41, 70: 74, 89: 56, 14: 39, 33: 53, 52: 72, 71: 83, 90: 124, 15: 88, 34: 122, 53: 45, 72: 55, 91: 106, 16: 126, 35: 93, 54: 90, 73: 50, 92: 115, 17: 120, 36: 38, 55: 110, 74: 70, 93: 98, 18: 68, 37: 103, 56: 44, 75: 104}
    memory = [0]*(3**10)
    for cell, data in enumerate(code):
        memory[cell] = ord(data)
    for cell in range(cell+1, 3**10):
        memory[cell] = crz(memory[cell-1], memory[cell-2])
    c = 0
    a = 0
    d = 0
    while 1:
        if not 33 <= memory[c] <= 126:
            break
        instruction = (memory[c]+c)%94
        if instruction == 4:
            c = memory[d]
        elif instruction == 5:
            print(end=chr(a%256))
        elif instruction == 23:
            a = ord(input())
        elif instruction == 39:
            memory[d] = a = rotate(memory[d])
        elif instruction == 40:
            d = memory[d]
        elif instruction == 62:
            memory[d] = a = crz(a, memory[d])
        elif instruction == 68:
            pass
        elif instruction == 81:
            break
        if 33 <= memory[c] <= 126:
            memory[c] %= 94
            memory[c] = encipherment[memory[c]]
        c = (c+1)%(3**10)
        d = (d+1)%(3**10)
assert crz(11355, 1131) == 20650
assert rotate(1823) == 39973
mal('''(=<`#9]~6ZY327Uv4-QsqpMn&+Ij"'E%e{Ab~w=_:]Kw%o44Uqp0/Q?xNvL:`H%c#DD2^WV>gY;dts76qKJImZkj''')