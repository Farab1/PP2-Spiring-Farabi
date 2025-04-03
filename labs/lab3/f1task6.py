def reverse_words(sentence):
    words = sentence.split(" ")  
    reversed_words = words[::-1] 
    return " ".join(reversed_words)  

# Пример использования
sentence = input("\n введите : ")
result = reverse_words(sentence)
print("\n Результат:\n", result)