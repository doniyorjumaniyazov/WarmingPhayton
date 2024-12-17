from random import randint

def guess(min_lim: int = 0, max_lim: int = 150, count: int = 5) -> bool:
   # """Игра: Угадай число. Пользователь пытается угадать случайное число за ограниченное количество попыток."""
    number = randint(min_lim, max_lim)  # Генерируем случайное число
    #print(f"Я загадал число от {min_lim} до {max_lim}. У вас {count} попыток угадать!")

    for _ in range(count):
        
            answer = int(input("Введите ваше число: "))
            if answer == number:
                print("Поздравляю, вы угадали!")
                return True
            elif answer > number:
                print(f"Меньше {answer}!")
            else:
                print(f"Больше {answer}!")
        
    print(f"Вы проиграли! Загаданное число было {number}.")
    return False

if __name__ == '__main__':
    guess()
