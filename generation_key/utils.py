import random
import math_module.math as math


def generation_param_p_and_q():
    return random.choices(math.sundarama_sieve(), k=2)


def get_random_d(argument):
    return random.choice(math.generation_set_of_mutually_prime_numbers(argument))


def get_random_e(n, d, argument):
    set_of_e = set()
    i = 2
    while i < n:
        if (i * d) % argument == 1:
            set_of_e.add(i)
        i += 1

    set_of_e.discard(d)
    #delete_prime_number_from_set(set_of_e)
    if len(set_of_e) == 0:
        raise AssertionError("cannot find 'e' with d={} and F={}".format(d, argument))

    return random.choice(list(set_of_e))


def write_text_to_file(path_to_file, text):
    with open(path_to_file, "w") as file:
        file.write(f"{text}")


def get_text_from_file(path_to_file):
    with open(path_to_file, "r") as file:
        return file.read()


def text_to_list_of_number(text):
    return [ord(symbol) for symbol in text]


def list_of_number_to_text(list_of_number):
    result = ""
    for elem in list_of_number:
        result += chr(elem)

    return result


def delete_prime_number_from_set(set_of_numbers):
    for elem in set(set_of_numbers):
        if math.is_prime(elem):
            set_of_numbers.remove(elem)