from random import randint

welcome_text="Угадайте число от 1 до 100"

number=randint(1,100)
print(welcome_text)

def main():
	while True:
		guess_1=int(input("Введите число:"))
		if guess_1<number:
			print("Ваше число меньше того,что задано.")
		if guess_1>number:
			print("Ваше число больше того,что задано.")
		if guess_1==number:
			break
	print("Отличная интуиция!Вы угадали число:")
		

main()
main()
main()
main()
main()
main()
main()
main()
main()