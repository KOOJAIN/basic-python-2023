# 모듈 사용
import math as m # 클래스로 안된 모듈
import code22_person as p # 우리가만든 클래스


print(m.pi)

print(m.tan(0))
print(m.ceil(3.8)) #무조건 올림 = ceil
print(2 ** 10)
print(m.pow(2, 10))

# 우리가 만든 모듈을 사용
me = p.Person('홍길순', 155, '여성')
print(me)


