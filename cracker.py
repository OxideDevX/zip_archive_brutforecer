import zipfile
print ( "Zip брутфорсер v 1.0.0. Создано OxideDevX.")
print ( "Данный софт предназначен для использования специалистами в области ИБ и форензики")

count = 1

with open('passlist.txt','rb') as text:
    for entry in text.readlines():
        password = entry.strip()
        try:
            with zipfile.ZipFile('unlockit.zip','r') as zf:
                zf.extractall(pwd=password)

                data = zf.namelist()[0]

                data_size = zf.getinfo(data).file_size

                print(__banner__,'''*****PASSWORD CRACKED*****\n******************************\n[+] Password found! ~ %s\n ~%s\n ~%s\n******************************''' 
                    % (password.decode('utf8'), data, data_size))
                break

        except:
            number = count
            print('[%s] [-] Trying... - %s' % (number,password.decode('utf8')),'[-] failed')
            count += 1
            pass
