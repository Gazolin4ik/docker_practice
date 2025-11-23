import time
import sys

# Отключаем буферизацию вывода
sys.stdout.flush()

print("Приложение запущено!")

counter = 0
while True:
    counter += 1
    print(f"Работаю... счетчик: {counter}")
    sys.stdout.flush()  # Принудительно сбрасываем буфер
    time.sleep(3)