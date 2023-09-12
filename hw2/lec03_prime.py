def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():
    num = 3
    if is_prime(num):
        print(f"{num}은/는 소수입니다.")
    else:
        print(f"{num}은/는 소수가 아닙니다.")


if __name__ == "__main__":
    main()
