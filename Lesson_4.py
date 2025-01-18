
def is_palindrome(word):
    return word == word[::-1]
while True:


    word = input("Введите слово: ").lower()

    if is_palindrome(word):
        print(f"Слово '{word}' является палиндромом!")
    else:
        print(f"Слово '{word}' не является палиндромом.")