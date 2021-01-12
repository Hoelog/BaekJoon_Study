"""
점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오. 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.
첫 줄에는 정수 x가 주어진다. (−1000 ≤ x ≤ 1000; x ≠ 0) 다음 줄에는 정수 y가 주어진다. (−1000 ≤ y ≤ 1000; y ≠ 0)
"""

num1 = int(input())
num2 = int(input())

if (num1 > 0 and num2 > 0):
    print("1")
elif (num1 < 0 and num2 > 0):
    print("2")
elif (num1 < 0 and num2 < 0):
    print("3")
else:
    print("4")
