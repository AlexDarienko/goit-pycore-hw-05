
def caching_fibonacci():
    # Створити порожній словник для кешування обчислених значень чисел Фібоначчі
    cache = {}

    def fibonacci(n):
        # Якщо n <= 0, повернути 0
        if n <= 0:
            return 0
        # Якщо n == 1, повернути 1
        elif n == 1:
            return 1
        # Якщо n вже є в кеші, повернути збережене значення
        if n in cache:
            return cache[n]
        
        # В іншому випадку обчислити значення, зберегти в кеш і повернути результат
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    # Повернути функцію fibonacci як результат
    return fibonacci

# Отримуємо функцію fibonacci з кешуванням
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
print(fib(50))  # Виведе 12586269025
print(fib(100)) # Виведе 354224848179261915075
