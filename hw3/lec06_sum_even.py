import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

def is_even(a):
    return a % 2 == 0

def simple_gui_input(text='값을 입력하세요'):
    user_input = simpledialog.askstring(title='6. 짝수의 합 구하기', prompt=text)
    try:
        return int(user_input)
    except ValueError:
        print('유효한 값을 입력하세요.')

def main():
    # a = int(input("숫자를 입력하세요."))
    start_nb = simple_gui_input('시작점을 입력하세요.')
    end_nb = simple_gui_input('끝점을 입력하세요.')
    evens = [x for x in range(start_nb, end_nb+1) if is_even(x)]
    sum_even = sum(evens)

    print(f"{start_nb}-{end_nb}까지 숫자 중 짝수의 합은 {sum_even}입니다.")

if __name__ == "__main__":
    main()
