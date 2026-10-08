def is_power_of_two(n):
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    return is_power_of_two(n // 2)

print("YES" if is_power_of_two(int(input())) else "NO")