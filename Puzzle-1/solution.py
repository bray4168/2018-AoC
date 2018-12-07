

def solve():
    frequencies = [0]
    frequency = 0
    run = 1
    while run:
        with open("test_data.txt", "r") as test_data:
            for each in test_data:
                frequency += int(each)
                if frequency in frequencies:
                    print(frequency)
                    run = 0
                    exit()
                else:
                    frequencies.append(frequency)


if __name__ == "__main__":
    solve()