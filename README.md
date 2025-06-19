## Запуск проекта

### **Способ 1: Локальный запуск (рекомендуется)**
1. Установите зависимости:
   ```bash
   uv sync
   ```
2. Установите пакет:
   ```bash
   uv tool install --force dist/*.whl
   ```
3. Запустите игру:
   ```bash
   brain-games  # Основное меню
   brain-even   # Проверка на чётность
   ```

### **Способ 2: Через Docker**
1. Соберите образ:
   ```bash
   docker build -t brain-games .
   ```
2. Запустите контейнер:
   ```bash
   docker run -it brain-games
   ```

**Доступные игры**
| Команда         | Описание                  |
|-----------------|--------------------------|
| `brain-even`    | Проверка на чётность      |
| `brain-calc`    | Арифметические примеры    |
| `brain-gcd`     | Наибольший делитель       |
| `brain-prime`   | Простые числа             |


## Пример игры
[![asciicast](https://asciinema.org/a/XXXXXX.svg)](https://asciinema.org/a/XXXXXX)

## Калькулятор
[![asciicast](https://asciinema.org/a/XXXXXX.svg)](https://asciinema.org/a/XXXXXX)

## Наибольший общий делитель
[![asciicast](https://asciinema.org/a/XXXXXX.svg)](https://asciinema.org/a/XXXXXX)

## Арифметическая прогрессия
[![asciicast](https://asciinema.org/a/XXXXXX.svg)](https://asciinema.org/a/XXXXXX)

## Простое ли число?
[![asciicast](https://asciinema.org/a/XXXXXX.svg)](https://asciinema.org/a/XXXXXX)