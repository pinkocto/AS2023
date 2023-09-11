import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def simple_gui_input(text='값을 입력하세요.'):
    user_input = simpledialog.askstring(title='3. 소수판별기', prompt=text)
    try:
        return int(user_input)
    except ValueError:
        print('유효한 값을 입력해주세요.')
        return None


def main():
    num = simple_gui_input()
    if is_prime(num):
        print(f"{num}은/는 소수입니다.")
    else:
        print(f"{num}은/는 소수가 아닙니다.")


if __name__ == "__main__":
    main()
