def isFibonacci(number):
    if number == 0 or number == 1:
        return "O número %d pertence a sequência de Fibonacci" % number
    a = 0
    b = 1
    while b <= number:
        if b == number:
            return "O número %d pertence a sequência de Fibonacci" % number
        else:
            a, b = b, a + b
    return "O número %d não pertence a sequência de Fibonacci" % number


number = int(input("Digite um número: "))
print(isFibonacci(number))