num_init=int(input('введите целое положительное число:'))
greatest_dig=0
num=num_init
while num>0:
    digit=num%10
    if digit>greatest_dig:
        greatest_dig=digit
        if greatest_dig==9:
            break
    num=num//10
print(f'наибольшая цифра в числе {num_init} равна {greatest_dig}')
