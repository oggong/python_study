# 1. 다음 코드의 실행 결과를 쓰시오.
try:
    for i in range(1, 7):
        result = 7 // i
        print(result)
except ZeroDivisionError:
    print("Not divided by 0")
finally:
    print("종료되었습니다.")

# 2. 다음 코드를 실행했을 때, 가장 마지막에 출력되는 값은?

sentence = list("Hello Gachon")
while (len(sentence) + 1):
    try:
        print(sentence.pop(0))
    except Exception as e:
        print(e)
    break
