import numpy as np

words_in_prohibition = np.array(["бля","блять","сука","еб","пон"])

def check_in_prohibition_words(text):
        return any(word.lower() in text.lower() for word in words_in_prohibition)
while True:
        text = input("введите сообщение:")
        result = check_in_prohibition_words(text)
        if result == True:
                print("вы сказали запрещённое слово!\nвам дано 30 секунд на раздумие над вашим поведеением!")
        else:
                print("всё нормально.")
