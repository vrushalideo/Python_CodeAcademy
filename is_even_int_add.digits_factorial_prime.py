def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def is_int(x):
    if int(x) - float(x) != 0:
        return False
    else:
        return True


def digit_sum(n):
    m = str(n)
    sum = 0
    for i in m:
        digit = n%10
        n = n//10 
        sum += digit
    return sum

def factorial(x):
    count = 1
    total = 1
    while count <= x:
        total *= count
        count += 1
    return total

def is_prime(x):
    y = True
    if x <=1:
        return False
    elif x == 2:
        return True
    n = x
    while n > 1:
        if x % n == 0:
            if n != x:
                y = False
        n = n - 1
    if y == False:
        return False
    else:
        return True


