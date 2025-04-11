
def longest_common_subsequence(X, Y):
    """
    X, Y: 두 문자열
    반환: LCS의 길이와 실제 공통 부분 문자열
    """
    m, n = len(X), len(Y)
    # dp[i][j]: X의 앞 i글자와 Y의 앞 j글자의 LCS 길이
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # DP 테이블 채우기
    print("📘 DP 테이블 채우기:")
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                print(f"  - X[{i - 1}] == Y[{j - 1}] ({X[i - 1]}): dp[{i}][{j}] = {dp[i][j]}")
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                print(f"  - X[{i - 1}] != Y[{j - 1}] ({X[i - 1]} vs {Y[j - 1]}): dp[{i}][{j}] = {dp[i][j]}")

    # LCS 길이는 dp[m][n]
    lcs_length = dp[m][n]

    # 🔄 LCS 경로 추적
    print("\n🔍 LCS 경로 추적:")
    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs.append(X[i-1])
            print(f"  - Match: {X[i - 1]} (i={i}, j={j})")
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]: # 위쪽 값이 왼쪽 값보다 크거나 같으면
            i -= 1 # 위쪽으로 이동
        else:
            j -= 1 # 왼쪽으로 이동

    lcs.reverse()  # 거꾸로 넣었으니 뒤집기

    return lcs_length, ''.join(lcs)

