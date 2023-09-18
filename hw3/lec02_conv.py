import tkinter as tk
from tkinter import simpledialog
# from rich.console import Console
from rich import print


ROOT = tk.Tk()
ROOT.withdraw()

def f2c(temp_f):
    return (temp_f - 32) * 5/9


def simple_gui_input(text="화씨온도를 입력해주세요."):
    user_input = simpledialog.askstring(title='2. 온도변환기', prompt=text)
    try:
        return int(user_input)
    except ValueError:
        print('유효한 숫자를 입력해주세요.')
        return None


def main():
    temp_f = simple_gui_input()
    # 두 줄
    temp_c = f2c(temp_f)
    print(f"{temp_f}F [bold red]=>[/bold red] {temp_c}℃")

    # 한 줄
    print(f"{temp_f}F [bold magenta]=>[/bold magenta] {f2c(temp_f)}℃")


if __name__ == "__main__":
    main()
