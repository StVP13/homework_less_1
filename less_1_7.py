while True:
    days = 1
    start_km = float(input('укажите исходное расстояние в первый день тренировок (км):'))
    target_km = float(input('укажите цель ваших тренировок (км):'))
    if start_km <= 0 or target_km < 0:
        print('показатель расстояния должен быть больше нуля. Начальная дистанция !=0.')
    else:
        while start_km < target_km:
            start_km += (start_km * 10) / 100
            days += 1
        print(f'ваша цель будет достигнута через {days} дней')
        break
