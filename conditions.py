def main():
    age = int(input(("Enter age: ")))
    print(type(age))
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")


if __name__ == "__main__":
    main()