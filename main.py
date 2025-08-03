import time

questions = {'Сколько планет в Солнечной системе?':8,
             'Столица Франции?':'Париж'}
score = 0

for k, a in questions.items():
    start_time = time.time()
    uans = input(k + '')
    end_time = time.time()
    if round(end_time - start_time, 1)>5:
        print('Вы не успели')
        uans = 'wrong'
    print(f'Время ответа:{round(end_time - start_time, 1)}с.')
    if uans.lower() == a.lower():
        print('Правильно')
        score += 1
    else:
        print('Неверно')

print(f'Ваш результат:{score}')
