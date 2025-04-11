
def matrix_chain_order(p):
    """
    p: 행렬의 크기를 나타내는 배열 (길이가 n+1이면 행렬은 n개)
       A1: p[0] x p[1], A2: p[1] x p[2], ..., An: p[n-1] x p[n]
    반환: 최소 곱셈 횟수, 최적 괄호 순서
    """
    n = len(p) - 1  # 행렬 개수
    m = [[0] * n for _ in range(n)]  # 최소 곱셈 수 저장
    s = [[0] * n for _ in range(n)]  # 최적 분할 위치 저장

    # l은 체인 길이 (2부터 n까지)
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                # cost = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                print(f"💭 m[{i}][{k}] + m[{k + 1}][{j}] + {p[i]}*{p[k + 1]}*{p[j + 1]} = {q}")
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m[0][n - 1], build_optimal_parens(s, 0, n - 1)


def build_optimal_parens(s, i, j):
    """괄호 순서를 문자열로 재귀적으로 구성"""
    if i == j:
        return f"A{i + 1}"
    else:
        return f"({build_optimal_parens(s, i, s[i][j])} x {build_optimal_parens(s, s[i][j] + 1, j)})"