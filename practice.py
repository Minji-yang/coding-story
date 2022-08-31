print("hello world")
station = " 신도림 "
print(station + "행 열차가 들어오고 있습니다")
print(1+1)  #2
print(3-2)
print(5*2)
print(6/2)
print(2**3)  #2^3=8
print(5%3)  # 나머지 구하기
print(10%3)
print(5//3) # 몫 구하기

print(10 > 4)
print(3 == 3) # true
print(4 == 2) # false
print(3 + 4 == 7) #true

print(1 != 3) # 앞 뒤가 같지 않다 이므로 true
print(not (1 == 3))
print(not(1 != 3))
print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))  # and와 같은 의미
print((3 > 0) or (3 > 5)) # 둘 중 하나만 true 여도 true
print((3 > 0)|(3 < 5)) # or과 같은 의미

print(2 + 3 * 4)
print((2 + 3)* 4)
number = 2 + 3 * 4  
print(number)     # 14
number = number + 2
print(number)   # 16 
number += 2  
print(number) #축약형으로  18 나옴
number *= 2   
print(number)   # 36
number -= 2 
print(number)
number /=2
print(number)
number %= 2 
print(number)  #나머지를 계산

print(abs(-5))
print(pow(4,2)) # 4^2
print(max(6,12))
print(min(5,12))
print(round(3.14))  # 반올림 3
print(round(3.99)) # 반올림 4

from math import *  # 매스 라이브러리를 이용하겠다
print(floor(4.99))   # 내림
print(ceil(3.14))    #올림
print(sqrt(16))     # 제곱근 4

from random import * # 랜덤 라이브러리를 이용하겠다
print(random())  # 0.0 이상 1.0 미만의 임의의 값을 생성
print(random()*10)  # 0.0 이상 10.0 미만의 임의의 값을 생성
print(int(random()*10))  # 0부터 10미만의 임의의 값을 생성
print(int(random()*10) + 1) # 1 부터 10 이하의 임의의 값을 생성

print(int(random() * 45 )+ 1)   # 1부터 45까지의 숫자 - 로또 번호 생성
print(int(random() * 45 )+ 1) 
print(int(random() * 45 )+ 1) 
print(int(random() * 45 )+ 1) 
print(int(random() * 45 )+ 1) 
print(int(random() * 45 )+ 1) 
print(int(random() * 45 )+ 1) 

print(randrange(1, 45))  # 1부터 45미만의  임의의 값을 생성
print(randrange(1, 46))  # 1부터 46미만의 임의의 값 생성

print(randint(1 , 45))   # 1부터 45이하의 임의의 값 생성

print(randint(1,28))

from random import *
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다")  #숫자이므로 str로 감싸주기

sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)


jumin = "990120-1234567"                  # 슬라이싱 하기   부분정보만 가져오기
print("성별 : " + jumin[7])         # 7번째 값만 가져오기 : 0부터 세기
print("연 :" + jumin[0:2])          # 0번째부터 2번째바로 앞 값까지   : 0값 1값
print("월 :" + jumin[2:4])
print("일 :" + jumin[4:6])
print("생년월일 : " + jumin[0:6])        # 0으로 시작할때는 생략해도됨 [:6]
print("뒤 7자리 : " + jumin[7:14])       # 끝까지 가져올때도 생략해도됨 [7:]
print("뒤 7자리 (뒤부터) : " + jumin[-7:-1])  #맨뒤는 -1부터 시작한다. 
print("뒤 7자리 (뒤부터) : " + jumin[-7:])  #-1이 끝까지라는 뜻이므로 생략가능

python = "Python is Amazing"
print(python.lower()) # 모두 소문자로 표시
print(python.upper()) # 모두 대문자로 표시
print(python[0].isupper()) # 파이썬 함수의 첫번째 문자열이 대문자인가 true false
print(len(python))  # 파이썬 함수의 길이
print(python.replace("Python","Java"))   # 문자열 찾아서 바꿔주기

index= python.index("n")   
print(index)                       #n이 몇번째에 위치했는지
print(python.index("n"))
index= python.index("n", index + 1)  #그 다음 n의 위치
print(index)

print(python.find("n"))   # n이 몇번째에 위치 했는지   / 포함되지 않은경우 -1 출력
print(python.find("Java"))
print(python.find("Java"))  # 인덱스는 포함되지 않은 경우 오류출력하고 끝나버림 / 그 뒤값도안나옴

print(python.count("n"))   # n이 몇번 등장하는지

print("a" + "b")  # 문자열 포맷  +나 , 이용 가능
print("a","b")  # ,는 띄어쓰기 포함
print("나는 %d살입니다." % 20)      # %뒤에 있는 값을 %뒤에 넣겠다 . d=정수의 의미
print("나는 %s을 좋아해요" % "파이썬")   # s=문자열의 의미  . 뒤에 큰따옴표로 감싸줘야함
print("Apple은 %c로 시작해요" %"A")     # c=character= 한 글자만 . 뒤에 큰따옴표로 감싸줘야함   
print("나는 %s살입니다" %20)  #s는 문자열 문자 정수 모두 커버가능


print(1+1)
time.sleep(1)
print(2+2)