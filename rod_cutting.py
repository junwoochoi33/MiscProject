
def rod_cutting(prices, n):
    """
    prices: 각 길이별 가격 리스트 (prices[i] = 길이 i+1의 가격)
    n: 자르려는 막대의 전체 길이
    """
    dp = [0] * (n+1) # 최대 수익 저장
    cuts = [0] * (n+1) # 최적 자르기 길이 저장

    # dp[0] = 0 (길이 0인 막대의 수익은 0)

    # 길이 1부터 n까지 막대를 자르며 최대 수익 계산
    for i in range(1, n+1):
        max_val = float('-inf')
        print(f"\n🔹 막대 길이 {i}일 때 가능한 자르기:")

        for j in range(i):
            # j는 자르는 길이-1 (즉, 실제 자르는 길이는 j+1)
            # prices[j] + dp[i-(j+1)]:
            # 자른 조각 가격 + 남은 길이의 최대 수익
            current_val = prices[j] + dp[i-(j+1)]
            print(f"  - 길이 {j + 1} 자르면: 가격({prices[j]}) + 남은 길이 {i - (j + 1)} 최대 수익({dp[i - (j + 1)]}) = {current_val}")

            if current_val > max_val:
                max_val = current_val
                cuts[i] = j + 1  # 가장 좋은 자르기 길이 저장
                print(f"    ✅ 현재 최적 선택: 자르기 길이 {cuts[i]} (수익 {max_val})")

        dp[i] = max_val # 길이 i일 때 최대 수익 저장
        print(f"➡️ 최종 선택: 길이 {i}일 때 최대 수익 = {dp[i]}, 자르기 = {cuts[i]}")

    print(f"\ndp: {dp}")
    print(f"cuts: {cuts}")

    # 경로 추적: 어떤 길이로 잘랐는지 추적
    cut_path = []
    length = n
    print("\n🧩 자르기 경로 추적:")
    while length > 0:
        cut_path.append(cuts[length])
        print(f"  - {cuts[length]} 길이로 자르고 남은 길이 {length - cuts[length]}")
        length -= cuts[length]

    return dp[n], cut_path

# if __name__ == '__main__':
#     prices = [1, 5, 8, 9, 10, 17, 17, 20]  # 길이 1~8 가격
#     n = 8
#     max_profit, cut_path = rod_cutting(prices, n)
#
#     print(f"최대 수익: {max_profit}")
#     print(f"자른 길이 경로: {cut_path}")