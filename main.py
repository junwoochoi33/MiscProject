from maxtrix_chain_multiplication import matrix_chain_order

if __name__ == '__main__':
    # A1: 10x30, A2: 30x5, A3: 5x60
    p = [10, 30, 5, 60]

    min_cost, parens = matrix_chain_order(p)

    print(f"\n✅ 최소 곱셈 수: {min_cost}")
    print(f"✅ 최적 괄호 순서: {parens}")