def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def main():
    list_prime = [x for x in range(1, 101) if is_prime(x)]
    print(f"1-100까지 중 소수는 {list_prime}입니다.")
    print(f"1-100까지 중 소수의 갯수는 {len(list_prime)}입니다.")


if __name__ == "__main__":
    main()
