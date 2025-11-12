def draw_digit(digit, row, col):
    if digit == 0:
        return (row in [0, 4]) or (col in [0, 4])
    elif digit == 1:
        return col == 2 or (row == 4 and col in [0,1,2,3,4])
    elif digit == 2:
        return (row in [0, 2, 4]) or (row == 1 and col == 4) or (row == 3 and col == 0)
    elif digit == 3:
        return (row in [0, 2, 4]) or (col == 4)
    elif digit == 4:
        return (row < 2 and col == 0) or (col == 4) or (row == 2)
    elif digit == 5:
        return (row in [0, 2, 4]) or (row == 1 and col == 0) or (row == 3 and col == 4)
    elif digit == 6:
        return (row in [0, 2, 4]) or (col == 0) or (row == 3 and col == 4)
    elif digit == 7:
        return (row == 0) or (col == 4)
    elif digit == 8:
        return (row in [0, 2, 4]) or (col in [0, 4])
    elif digit == 9:
        return (row in [0, 2]) or (col == 4) or (row < 2 and col == 0)
    else:
        return False

num = input("Enter a number: ")

rows, cols = 5, 5

for r in range(rows):
    for digit in num:
        d = int(digit)
        for c in range(cols):
            if draw_digit(d, r, c):
                print(digit, end="")
            else:
                print(" ", end="")
        print("  ", end="")
    print()
