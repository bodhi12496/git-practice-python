from src.calculator import add, multiply, subtract


def main() -> None:
    first_number = 10
    second_number = 5

    print("Addition:", add(first_number, second_number))
    print("Subtraction:", subtract(first_number, second_number))
    print("Multiplication:", multiply(first_number, second_number))


if __name__ == "__main__":
    main()