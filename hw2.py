def exchange(n):
    a = n // 500
    b = (n - 500 * a) // 100 
    c = (n - (500 * a + 100 * b)) // 50
    d = (n - (500 * a + 100 * b + 50 * c)) // 10
    return a, b, c, d
def get_integer(n):
    a, b, c, d = exchange(n)
    print('500원 동전의 개수:', a)
    print('100원 동전의 개수:', b)
    print('50원 동전의 개수:', c)
    print('10원 동전의 개수:', d)
n = int(input("동전으로 교환하고자 하는 금액은? "))
get_integer(n)