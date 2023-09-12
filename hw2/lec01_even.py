def main():
    # a = int(input("숫자를 입력하세요."))
    number = 3
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
