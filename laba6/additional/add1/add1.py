"""
Как пример .exe файла взял инсталлер jdk
Пушить сюда я его не стал, выберите ЛЮБОЙ свой .exe файл
"""


def Solution():
    try:
        with open('./jdk-21_windows-x64_bin.exe', 'rb') as file:
            prefix = file.read(2)
            return prefix == b'MZ'
    except:
        print("An unknown error occurred")
        return 0


print(Solution())
