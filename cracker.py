# подключаю библиотеку для работі с архивами
import zipfile
print ( "Zip брутфорсер v 1.0.0. Создано OxideDevX.")
print ( "Данный софт предназначен для использования специалистами в области ИБ и форензики")
print ( "Использование данного ПО в противозаконных целях запрещаеться! Автор не несет отвественность за любые негативные действия которые могут возникнуть при использовании данного ПО")

count = 1
# беру пароли с файла passlist.txt и просто их перебираю
with open('passlist.txt','rb') as text:
    for entry in text.readlines():
        password = entry.strip()
        try:
            with zipfile.ZipFile('lock.zip','r') as zf:
                zf.extractall(pwd=password)

                data = zf.namelist()[0]

                data_size = zf.getinfo(data).file_size
# если подбор пароля успешен, то выводим на экран сообщение об успехе и останавливаем работу скрипта
                print(__banner__,'''*****PASSWORD CRACKED*****\n******************************\n[+] Password found! ~ %s\n ~%s\n ~%s\n******************************''' 
                    % (password.decode('utf8'), data, data_size))
                break

        except:
            number = count
            print('[%s] [-] Trying... - %s' % (number,password.decode('utf8')),'[-] failed')
            count += 1
            pass
