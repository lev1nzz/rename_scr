import sys
import os
import signal
import time
from signature import hacker_signature_compact


def signal_handler(signum, frame):
    print('Программа завершается...')
    sys.exit(0)
    

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)


def rename_files(directory, old_text, new_text):
    """
    Docstring for rename_files
    Переименновывает файлы в указанной директории.
    
    :param directory: Путь к папке 
    :param old_text: текст для замены
    :param new_text: новый текст
    """
    
    for filename in os.listdir(directory):
        if old_text in filename:
            new_name = filename.replace(old_text, new_text)
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            
            os.rename(old_path, new_path)
            print(f'Переименован: {filename} -> {new_name}')
            
def main():
    try:
        while True:
            print("\n")
            hacker_signature_compact()
            print("\n")
            
            directory= input('Введите путь: ')
            old_text = input('Введите старое название: ')
            new_text = input('Введите новое название: ')
            
            rename_files(directory, old_text, new_text)
            time.sleep(0.3)
    except KeyboardInterrupt:
        print('Прерванно пользователем')
    finally:
        print('Очистка ресурсов...')
    

if __name__ == '__main__':
    main()