#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def menu():
    print ('''
 
    \033[1;33m 1)-> Установить необходимые пакеты [Обновление системы] (Linux only)\033[1;m 
    \033[1;36m 2)-> Расшарить HOME директорию по HTTP (Linux only) \033[1;m
    \033[1;35m 3)-> Расшарить директорию по HTTP с указанием адреса в ручную\033[1;m
    \033[1;32m 4)-> Расшарить директорию в которой запущен скрипт\033[1;m
    \033[1;91m 5)-> Показать справку\033[1;m
		''')
    print("Для выхода нажать CTRL+C")
    return print()

def get_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
    ip=s.getsockname()[0]
    s.close()
    return ip

    

    return 
def choise1():
    import os, sys, traceback
    cmd1 = os.system("apt-get update && apt-get upgrade -y && clear")
    cmd2 = os.system("echo '' && echo 'Система обновлена' && echo ''")
    return cmd1, cmd2

def choise2():
    import os, sys, traceback
    ipinfo = os.system("hostname -I")
    cmd = os.system("echo '' && echo 'Расшарено' && echo ''")
    share=os.system("python -m SimpleHTTPServer 8888")    
    return print()

def choise3():
    import os, sys, traceback
    dir=str(input("Вводим директорию расшаривания "))
    os.chdir(dir)
    print(os.listdir())
    print()
    ipinfo = os.system("hostname -I")
    print("По завершению нажать CTRL+C")
    cmd = os.system("echo '' && echo 'Расшарено' && echo ''")
    share=os.system("python -m SimpleHTTPServer 8888")    
    return print()

def choise4():
    import os, sys, traceback
    dir=os.getcwd()
    os.chdir(dir)
    print(os.listdir())
    print()
    ipinfo = os.system("hostname -I")
    print("По завершению нажать CTRL+C")
    cmd = os.system("echo '' && echo 'Расшарено' && echo ''")
    share=os.system("python -m SimpleHTTPServer 8888")    
    return print()

def choise5():
    print("Скрипт создает простой сервер для расшаривания каталога.Чтобы зайти в расшареный каталог нужно набрать в строке обозревателя http://ip адрес компа:8888")
    print("В конкретном случае "+"http://"+get_ip()+":8888")
    print("Для установки в систему скопировать в cp sharepy.py  /usr/bin/sharepy.py && chmod +x /usr/bin/sharepy.py")
    return print()



def main():
    while 1:
        menu()
        a=int(input("Ввести выбор от 1 до 5: "))
        if a==1:
            choise1()
        elif a==2:
            choise2()
        elif a==3:
            choise3()
        elif a==4:
            choise4()
        elif a==5:
            choise5()
        else :
            print ("Ошибка ввода") 

if __name__ == "__main__":
    main()