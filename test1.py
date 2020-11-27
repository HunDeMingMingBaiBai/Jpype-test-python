import time

def run():
    for i in range(1000000):
        num = 11.1
        num = num + 1.1
        num = num - 1.1
        num = num * 1.1
        num = num * 0.9
    print('Hello World!')

def run1(count):
    N = count
    result = 0.0
    for i in range(1, N):
        x = i
        y = sin(i)
        x = (x - y) * (x - y)
        result = result + x
    return result

def sin(n):
    result = 0
    for i in range(1, 11):
        result = result + pow(-1, i + 1) * pow(n, 2*i - 1) / factorial(2*i - 1)
    return result

def pow(num, n):
    temp = 1.0 * num
    result = temp
    for i in range(1, n):
        result = result * temp
    return result

def factorial(n):
    result = 1.0
    for i in range(1, n+1):
        result = result * i
    return result

if __name__ == '__main__':
    for i in range(10):
        start = time.time()
        result = run1(100000)
        end = time.time()
        print('--- --- ---')
        print(result)
        print(end - start)
        print((end - start) * 1000)
        print('--- --- ---')
