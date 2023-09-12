import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

def fact(num):
    result = 1
    for i in range(1, num+1):
        result = result*i
    return result

def simple_gui_input(text="값을 입력해주세요."):
    user_input = simpledialog.askstring(title="팩토리얼을 구해라!", prompt=text)
    try:
        return int(user_input)
    except ValueError:
        print('유효한 양의 정수를 입력해주세요.')
        return None

def main():
    number = simple_gui_input()
    print(f"{number}!은 {fact(number)}입니다.")


if __name__ == "__main__":
    main()
