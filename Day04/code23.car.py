import os
import code

# 자동차 클래스 

class car:
    __number = '54라 9538'

    def get_number(self) -> str:
        return self.__number
    
    # 클래스 외부에선 변경x, 맴버함수로는 변경o    
    def set_number(self, number):
        self.__number = number

    def __init__(self, number = '54라 9538') -> None:     
        self.__number = number
        print('__init__')

    def __str__(self) -> str:
        return f'차번호는 {self.__number}'

yourcar = car('88호 7486')
print(yourcar)
yourcar.__number = '54라 9999' #외부에서는 맴버변수에 접근불가
print(yourcar)
print('클래스 내부함수 사용!')
yourcar.set_number('55오 5555')
print(yourcar)

mycar = car()
print(mycar)
print(f'제차는, 람보르기니고, 번호가 {mycar.get_number()}에요.')


mycar.__number = '123사 5678'
print(mycar.get_number())


