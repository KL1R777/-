import random 


lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)

guesses = 0
is_running = True

print("Python Угадай число")
print(f"Выберите число в диапозоне от {lowest_num} до {highest_num}")

while is_running:
    
    guess = input("Введите число: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        
        if guess < lowest_num or guess > highest_num:
            print("Число выходит за диапозон")
            print(f"Пожалуйста выберите число от {lowest_num} до {highest_num}")
        elif guess > answer:
            print("Оно меньше! Попробуйте снова!")
        elif guess < answer:
            print("Оно больше! Попробуйте снова!")
        else:
            print(f"Правильно! Ответ: {answer}")
            print(f"Количество попыток: {guesses}")
            play_again = input("Хочешь сыграть еще? (Y/N):")
            
            if play_again.upper() == "N":
                print("Пока! Хорошо поиграли!")
                is_running = False
    else:
        print("Invalid guess - Ошибка")
        print(f"Пожалуйста выберите число от {lowest_num} до {highest_num}")
    
  
    
        
        
    







