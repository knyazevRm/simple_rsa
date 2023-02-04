def sundarama_sieve(size=100):
    sc: set = set(range(1, size + 1))
    for i in range(1, int((((2 * size + 1) ** 0.5) - 1) / 2) + 1):
        for j in range(i, (size - 1) // (2 * i + 1) + 1):
            sc.discard(i + j + 2 * i * j)

    return [i * 2 + 1 for i in sc]


def generation_set_of_mutually_prime_numbers(argument):
    result_set_mutually_prime_numbers = set()
    for i in range(2, argument):
        if gcd(argument, i) == 1:
            result_set_mutually_prime_numbers.add(i)

    return list(result_set_mutually_prime_numbers)


def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


def is_prime(number):
    if number < 2:
        return False

    if number % 2 == 0:
        return number == 2

    d = 3
    while d * d <= number and number % d != 0:
        d += 2

    return d * d > number
