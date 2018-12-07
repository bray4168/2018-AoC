def solve():
    match2 = 0
    match3 = 0

    with open("../test_data.txt", "r") as test_data:
        for string in test_data:
            did_match_2 = 0
            did_match_3 = 0

            for each in string:
                count = string.count(each)
                if count == 2:
                    did_match_2 = 1
                elif count == 3:
                    did_match_3 = 1
                    
            match2 += did_match_2
            match3 += did_match_3

    solution = match2 * match3
    print(solution)


if __name__ == "__main__":
    solve()