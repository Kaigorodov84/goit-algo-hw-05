def caching_fibonacci():
    cache = dict() # Створюємо  порожній словник cache

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache: return cache[n] #перевіpка чи (n)  є у кеші 
        cache[n] = fibonacci(n-1) + fibonacci(n-2)     #обчислення чисел Фібоначі
        return cache[n]
    return fibonacci
        
           
caching_fibonacci()

fib = caching_fibonacci()  # Отримуємо функцію fibonacci

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610