def factorial(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return answer

def factorialr(n):
    if n == 0:
        return 1
    fac = factorialr(n - 1)
    answer = fac * n
    return answer


# print(factorial(9))



print(factorialr(9))