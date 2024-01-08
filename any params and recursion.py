def test(*args, **kwargs):
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(key, '=', value)


test(1, 2, 3, 'text', 3.1415, cat='Mяy!', dog='Гав!')


def factorial(n):
    if n == 1:
        return 1
    fac_nmin1 = factorial(n - 1)
    return n * fac_nmin1


n = int(input())
print(factorial(n))
