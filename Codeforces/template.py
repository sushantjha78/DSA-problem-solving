# codeforces solution template

def solve(arr, arr_len):
    # write your code here
    pass












if __name__ == "__main__":
    #take inputs
    test_cases = int(input())

    #loop for test cases
    for i in range(test_cases):
        arr_len = int(input())
        arr = list(map(int, input().split()))

        # call the function for each test case
        ans = solve(arr, arr_len)
        print(ans)

    ########## for testing locally ##########
    #     # take inputs from file input.txt
    # f = open('./input.txt', 'r')
    # test_cases = int(f.readline())

    # # loop for test cases
    # for i in range(test_cases):
    #     arr_len = int(f.readline())
    #     arr = list(map(int, f.readline().split()))

    #     # call the function for each test case
    #     ans = solve(arr, arr_len)
    #     print(ans)