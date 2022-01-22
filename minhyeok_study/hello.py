print("hello")




""" 1+1 구하기 """
a = int(input("1 + 1 = "))
if a == 2:
  print("정답입니다.")
else:
  print("틀렸습니다.") 



""" 숫자 값 받아서 더하기 """
first_num = int(input("첫 번째 숫자는 : "))
second_num = int(input("두 번째 숫자는 : "))
print(first_num ,"+", second_num, "=", first_num+second_num)




""" 함수 """
def add(a,b):
  return a+b

result = add(1,2)
print("함수 연습 ", result)


"""박성우의 병신짓"""
a,b = map(int,input("두개의 숫자를 입력하세요. (띄어쓰기로 구분) ").split())

print(a+b)