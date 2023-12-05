"""
Угадайте что?
Задание опять бред!
Это все что я смог придумать...
"""

import shutil


def Solution(copyfrom_dir, copyto_dir):
    try:
        shutil.copy2(copyfrom_dir, copyto_dir)
        print("SUCCESSFULLY COPIED FILE", copyfrom_dir)
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Have no access to file", copyfrom_dir)
    except Exception as e:
        print("unknown error. more info down below")
        print(e)


Solution("copyme.txt", "copy_copyme.txt")
