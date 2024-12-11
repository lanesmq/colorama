#!pip install colorama
# Импортируем библиотеку
import colorama
from colorama import Fore, Back, Style
# Инициализация библиотеки (для корректной работы на Windows)
colorama.init()
# Интроспекция библиотеки
attributes = dir(colorama)
# Выводим основные атрибуты
print("Основные атрибуты и методы библиотеки colorama:")
print(attributes)
# Демонстрация ключевых возможностей:
# 1. Fore (цвет текста)
print(Fore.RED + "Пример текста красного цвета" + Style.RESET_ALL)
# 2. Back (цвет фона)
print(Back.GREEN + "Пример текста с зелёным фоном" + Style.RESET_ALL)
# 3. Style (стили текста)
print(Style.BRIGHT + "Пример текста с ярким стилем" + Style.RESET_ALL)
# Обратный сброс цветов и стилей
print("Сброс стиля текста к стандартному.")
# Завершение работы (не обязательно, но рекомендуется для Windows)
colorama.deinit()
