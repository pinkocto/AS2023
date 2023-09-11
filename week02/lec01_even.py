import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

def simple_gui_input(text="정수를 입력하세요."):
    user_input = simpledialog.askstring(title='1. 짝수/홀수 판별기', prompt = text)
    try:
        return int(user_input)
    except ValueError:
        print("유효한 정수를 입력하세요.")
        return None

def main():
    # a = int(input("숫자를 입력하세요."))
    number = simple_gui_input()
    if number % 2 == 0:
        if number % 10 in [2, 4, 5, 9]:
            print(f"{number}는 짝수입니다.")
        else:
            print(f"{number}은 짝수입니다.")
    else:
        if number % 10 in [2, 4, 5, 9]:
            print(f"{number}는 홀수입니다.")
        else:
            print(f"{number}은 홀수입니다.")

if __name__ == "__main__":
    main()
