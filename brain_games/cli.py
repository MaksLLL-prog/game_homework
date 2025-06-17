def welcome_user():
    print("Welcome to the Brain Games!")
    while True:
        name = input("May I have your name? ").strip()
        if name:  # Проверяем, что введено не пустое значение
            print(f"Hello, {name}!")
            return name
        print("Please enter your name!")