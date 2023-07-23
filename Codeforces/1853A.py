# codeforces solution 1853A.py

def solve(arr, arr_len):
    min_diff = 1e9
    for i in range(arr_len-1):
        if arr[i+1]-arr[i] < min_diff:
            min_diff = arr[i+1]-arr[i]

    if min_diff >= 0:
        return min_diff//2 + 1

    return 0


if __name__ == "__main__":
    # take inputs
    test_cases = int(input())

    # loop for test cases
    for i in range(test_cases):
        arr_len = int(input())
        arr = list(map(int, input().split()))

        # call the function for each test case
        ans = solve(arr, arr_len)
        print(ans)
