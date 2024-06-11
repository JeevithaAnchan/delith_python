print(("* " * 5 + "\n") * 5)

def triangle(n):
    for i in range(n, 0, -1):
        print(" " * (n - i), end="")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

n = 5
triangle(n)

def cross(n):
    for i in range(n):
        for j in range(n):
            # we are checking if i and j have same vaules
            # or if i added with j gives same value as n-1
            if i == j or i + j == n - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

cross(3)