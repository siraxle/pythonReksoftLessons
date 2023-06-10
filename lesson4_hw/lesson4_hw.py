# Количество слов
def get_amount_of_worlds():
    s = input("Enter your string:")
    amount = s.count(' ') + 1
    print(amount)


get_amount_of_worlds()


# Нижний регистр
def get_lower_case_letters_amount():
    s = input("Enter your string:")
    tmp = s.lower()
    res = 0
    for i in range(0, len(s)):
        if s[i].isdigit() == False:
            if s[i] == tmp[i]:
                res = res + 1
    print(res)

get_lower_case_letters_amount()

# Шифр Цезаря
key = int(input('Enter key: '))
string = input('Enter string: ')
res = ''
for i in range(0, len(string)):
    res = res + chr(ord(string[i]) - key)
print(res)

# Windows OS
path = input("Enter path: ")
words = path.split('\\')
for s in range(0, len(words)):
    print(words[s])
