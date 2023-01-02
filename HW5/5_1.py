# Напишите программу, удаляющую из текста все слова, содержащие "абв"

text = 'Зимбабвийский самозабвенный абвер приказал долго жить'
print(f"Полный текст: {text}")

def delete_letters(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = delete_letters(text)
print(f"Сокращенный текст: {text}")