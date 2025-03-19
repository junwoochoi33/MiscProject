import sys
from collections import defaultdict

def coding_test_01():

    """
    문제 이름: 명언 검색

    문제 설명:
    주어진 명언 목록에서 특정 단어가 포함된 명언들을 찾아 출력하는 프로그램을 작성하시오.
    각 명언은 하나의 문자열로 제공되며, 이 문자열은 여러 개의 단어로 이루어져 있습니다.
    주어진 키워드(검색할 단어)를 포함하는 명언들을 출력하는 프로그램을 작성해야 합니다.
    명언에서 단어는 공백을 기준으로 구분되며, 대소문자를 구분하지 않습니다.
    키워드를 포함하는 명언이 없으면 "키워드 'ㅇㅇㅇ'을 포함하는 명언이 없습니다."를 출력합니다. (ㅇㅇㅇ은 키워드)

    조건:
    keyword는 대소문자를 구분하지 않으며, 단어의 앞뒤 공백은 무시합니다.
    quotes에 있는 각 명언은 공백을 기준으로 단어들이 구분됩니다.
    명언은 입력된 순서대로 출력되어야 합니다.

    입력 설명:
    첫 번째 줄에는 두 개의 숫자가 주어지며, 첫 번째 숫자는 명언의 개수, 두 번째 숫자는 검색어의 개수를 나타냅니다.
    이후 정해진 개수만큼의 명언과 검색어가 주어집니다.

    입력 예시1:
    5 2
    자신의 마음을 비우고, 새로운 것을 받아들여라. - 라오쯔
    자신의 능력을 믿어라. - 나폴레옹 힐
    자신의 선택을 존중하라. - 롭 위머
    어떤 일을 시작할 때 가장 중요한 것은 그것을 끝까지 이어가는 것이다. - 윈스턴 처칠
    자신을 믿어라. 그게 시작이다. - 존 웨인
    자신의
    믿어라.

    출력 예시1:
    자신의 마음을 비우고, 새로운 것을 받아들여라. - 라오쯔
    자신의 능력을 믿어라. - 나폴레옹 힐
    자신의 선택을 존중하라. - 롭 위머
    자신의 능력을 믿어라. - 나폴레옹 힐
    자신을 믿어라. 그게 시작이다. - 존 웨인

    입력 예시2:
    5 1
    자신의 마음을 비우고, 새로운 것을 받아들여라. - 라오쯔
    자신의 능력을 믿어라. - 나폴레옹 힐
    자신의 선택을 존중하라. - 롭 위머
    어떤 일을 시작할 때 가장 중요한 것은 그것을 끝까지 이어가는 것이다. - 윈스턴 처칠
    자신을 믿어라. 그게 시작이다. - 존 웨인
    와이즈넛

    출력 예시2:
    키워드 '와이즈넛'을 포함하는 명언이 없습니다.
    """

    input = sys.stdin.readline
    n, m = map(int, input().split())
    quotes = list()
    index = defaultdict(set)

    for docid in range(n):
        quote = input().strip()
        quotes.append(quote)
        for token in quote.split():
            token = token.lower()
            index[token].add(docid)

    keywords = [input().strip() for _ in range(m)]

    for keyword in keywords:
        key = keyword.lower()
        if key in index:
            for docid in index[key]:
                print(quotes[docid])
        else:
            print(f"키워드 '{keyword}'를 포함하는 명언이 없습니다.")



