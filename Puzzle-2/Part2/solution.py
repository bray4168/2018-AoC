def read_test_data():
    strings = []

    with open("../test_data.txt", "r") as test_data:
        for string in test_data:
            strings.append(string)

    return strings

def solve():
    test_data = read_test_data()

    for label in test_data:

    print(solution)


if __name__ == "__main__":
    solve()