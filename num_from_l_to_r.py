#6
def digits_forward(n):
    if n > 0:
        digits_forward(n // 10)
        print(n % 10, end=' ')

digits_forward(int(input()))