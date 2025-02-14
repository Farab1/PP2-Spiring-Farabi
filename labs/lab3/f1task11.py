def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]


word_or_phrase = input("Введите слово или фразу: ")
if is_palindrome(word_or_phrase):
    print("Это палиндром")
else:
    print("Это не палиндром")