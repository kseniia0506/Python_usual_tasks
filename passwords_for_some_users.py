#Цикл while. Существует четыре пользователя, у каждого пользователя есть логин и пароль. Запрашивать ввод логина и пароля пока не совпадут пара пользователь-пароль. Вывести приветствие пользователя с использованием логина.

user1='ilya@gmail.com'
password1='1231AA'
user2='ilya2@gmail.com'
password2='afec2'
user3='ilya3@gmail.com'
password3='Илья234'
user4='ilya4@gmail.com'
password4='Ujol234v'
a=input('Введите логин: ')
b=input('Введите пароль: ')
while not ((a==user1 and b==password1) or (a==user2 and b==password2) or (a==user3 and b==password3) or(a==user4 and b==password4)):
    print('Неверно, повторите попытку')
    a=input('Введите логин: ')
    b=input('Введите пароль: ')
print('Добро пожаловать, %s' %(a))
