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
    user_input = simpledialog.askstring(title='4. 소수는 몇 개?', prompt=text)
    try:
        return int(user_input)
    except ValueError:
        print('유효한 숫자를 입력해주세요.')
        return None


def main():
    start_nb = simple_gui_input('시작점을 입력하세요.')
    end_nb = simple_gui_input('끝점을 입력하세요.')
    list_prime = [x for x in range(start_nb, end_nb+1) if is_prime(x)]
    print(f"{start_nb}-{end_nb}까지 중 소수는 {list_prime}입니다.")
    print(f"{start_nb}-{end_nb}까지 중 소수의 갯수는 {len(list_prime)}입니다.")


if __name__ == "__main__":
    main()
