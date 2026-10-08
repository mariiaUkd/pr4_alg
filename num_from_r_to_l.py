#5
def digits_reverse(n):
    if n > 0:
        print(n % 10, end=' ')
        digits_reverse(n // 10)

digits_reverse(int(input()))