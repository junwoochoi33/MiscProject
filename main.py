from longest_common_sequence import longest_common_subsequence

if __name__ == '__main__':
    X = "ABCBDAB"
    Y = "BDCABA"

    length, lcs = longest_common_subsequence(X, Y)

    print(f"\n✅ LCS 길이: {length}")
    print(f"✅ 공통 부분 수열: {lcs}")