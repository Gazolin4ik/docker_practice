import time

print("Запущен бесконечный цикл для поддержания работы контейнера...")

try:
    while True:
        timr.sleep(1)
except KeyboardInterrupt:
    print("\nПолучен сигнал прерывания, завершение работы...")