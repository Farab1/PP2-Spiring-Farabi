def filter_prime(a):
    primel = []
    for x in a:
        if x > 1:
            is_prime = True
            for z in range(2, int(x ** 0.5) + 1):
                if x % z == 0:
                    is_prime = False
                    break
            if is_prime:
                primel.append(x)
    return primel


user_input = input()
num_list = list(map(int, user_input.split()))

print("PRIME numbers:", filter_prime(num_list))
