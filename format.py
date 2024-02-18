# Использование %
team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
team1_num, team2_num = int(input()), int(input())
print('В команде %s участников: %s !' % (team1_name, team1_num))
print('В команде %s участников: %s !' % (team2_name, team2_num))
print('Итого сегодня в командах участников %s и %s, а всего %s!' % (team1_num, team2_num, team1_num + team2_num))

# Использование format():
team1_score, team2_score = int(input()), int(input())
team1_time, team2_time = float(input()), float(input())
print('Команда {0} решила задач: {1} !'.format(team1_name, team1_score))
print('Команда {0} решила задач: {1} !'.format(team2_name, team2_score))
print('{0} решили задачи за {1} c !'.format(team1_name, team1_time))
print('{0} решили задачи за {1} c !'.format(team2_name, team2_time))

# Использование f-строк:
print(f'Команды решили {team1_score} и {team2_score}, а всего было решено {team1_score + team2_score} задач!')
time_total = team1_time + team2_time
score_total = team1_score + team2_score
print(f'Сегодня было решенно {score_total} задач, в среднем по {round(time_total / score_total, 2)} секунды на задачу!')

if team1_score > team2_score or team1_score == team2_score and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif team1_score < team2_score or team1_score == team2_score and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(f'Результат битвы: {result}')
