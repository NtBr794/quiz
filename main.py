questions = {'Сколько планет в Солнечной системе?':8,
             'Столица Франции?':'Париж'}
score = 0

for k, a in questions.items():
    uans = input(k + '')
    if uans.lower() == a.lower():
        print('Правильно')
        score += 1
    else:
        print('Неверно')

print(f'Ваш результат:{score}')
