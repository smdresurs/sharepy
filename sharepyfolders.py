#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def menu():
    print('''

         ,,                                                          ,...       ,,        ,,
       `7MM                                 `7MM"""Mq.             .d' ""     `7MM      `7MM
         MM                                   MM   `MM.            dM`          MM        MM
,pP"Ybd  MMpMMMb.   ,6"Yb.  `7Mb,od8 .gP"Ya   MM   ,M9 `7M'   `MF'mMMmm,pW"Wq.  MM   ,M""bMM  .gP"Ya `7Mb,od8 ,pP"Ybd
8I   `"  MM    MM  8)   MM    MM' "',M'   Yb  MMmmdM9    VA   ,V   MM 6W'   `Wb MM ,AP    MM ,M'   Yb  MM' "' 8I   `"
`YMMMa.  MM    MM   ,pm9MM    MM    8M""""""  MM          VA ,V    MM 8M     M8 MM 8MI    MM 8M""""""  MM     `YMMMa.
L.   I8  MM    MM  8M   MM    MM    YM.    ,  MM           VVV     MM YA.   ,A9 MM `Mb    MM YM.    ,  MM     L.   I8
M9mmmP'.JMML  JMML.`Moo9^Yo..JMML.   `Mbmmd'.JMML.         ,V    .JMML.`Ybmd9'.JMML.`Wbmd"MML.`Mbmmd'.JMML.   M9mmmP'
                                                          ,V
                                                       OOb"

    ''')
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
    print("Для установки в систему скопировать  sudo cp sharepyfolders.py  /usr/bin/sharepyfolders.py && sudo chmod +x /usr/bin/sharepyfolders.py")
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
