import tkinter as tk
from tkinter import simpledialog
from rich import print
#from rich.console import Console # 해당 방법은 적용이 안됨.
#console = Console()


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
    root = tk.Tk()
    label = tk.Label(root, font=["Georgia", 12, 'bold'])
    label.pack()

    if number % 2 == 0:
        if number % 10 in [2, 4, 5, 9]:
            #console.print(f"{number}는 짝수입니다.", style="bold red") # rich는 콘솔 출력에 안나타남.
            label.config(text = f"{number}는 짝수입니다.", fg="magenta") # tk창에 출력
        else:
            #print(f"{number}은 짝수입니다.")
            label.config(text = f"{number}은 짝수입니다.", fg="magenta")
    else:
        if number % 10 in [2, 4, 5, 9]:
            #print(f"{number}는 홀수입니다.")
            label.config(text = f"{number}는 홀수입니다.", fg="cyan")
        else:
            #print(f"{number}은 홀수입니다.")
            label.config(text = f"{number}은 홀수입니다.", fg="cyan")

    root.mainloop()

if __name__ == "__main__":
    main()
