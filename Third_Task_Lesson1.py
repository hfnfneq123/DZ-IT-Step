import random

secret_number = random.randint(1, 10)

print("Я загадав число від 1 до 10. Спробуй вгадати! У тебе 3 спроби.\n")

for attempt in range(1, 4):
    guess = int(input(f"Спроба №{attempt} Введи число: "))

    if guess == secret_number:
        print("Вітаю! Ти вгадав число!")
        break
    elif guess > secret_number:
        print("Менше!")
    else:
        print("Більше!")
else:
    print(f"На жаль, ти не вгадав. Це було число {secret_number}.")
