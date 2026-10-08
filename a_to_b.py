#2. Від A до B
def print_a_b(a, b):
    print(a, end=' ')
    if a < b:
        print_a_b(a + 1, b)
    elif a > b:
        print_a_b(a - 1, b)

a, b = map(int, input("Введіть A і B через пробіл: ").split())
print_a_b(a, b)