# studypython2023
부경대 IOT 파이썬 학습 리포지토리

## 1일차
1. 기본구성
     - Git/Github 설치 및 연동
    - Visual Studio code 설치 및 연동
    - Python 설치
2. 파이썬 기본
    - 콘솔출력
    - 주석

```python
# desc : 콘솔출력 - 주석 
print('Hello, Python!!') # 콘솔출력 함수
```

## 2일차
1. 파이썬 기본
    - 변수
    - 자료형
    - 연산자

```python
# 변수
val = 1

# 자료형
print(type(val)) # <class 'int'>

# 문자열 포맷팅
print("I'm so happy {0} to you, {1}!!".format(2, 'Hey'))
# 최신식 문자열 포맷팅
preword = 3
sayHello = 'Hey'
print(f"I'm so happy {preword} to you, {sayHello}!!")

pi = 3.141592
print(f'파이는 {pi}입니다.')        # 파이는 3.141592입니다.
print(f'파이는 {pi:0.2f}입니다.')   # 파이는 3.14입니다.
print(f'파이는 {pi:10.3f}입니다.')  # 파이는          3.142입니다.
```

## 3일차
1. 파이썬 기본
    - 흐름제어  
        - if
        - for
        - while
    - 구구단 프로그램
    - 함수


## 4일차
1. 파이썬  기본
    - 가상환경
    - 객체지향 OOP
    - 패키지, 모듈
    
## 5일차
1. 파이썬 기본
    - 패키지 계속
    - 입출력 다시  
    - 예외처리

## 6일차
1. 파이썬 기본
    - 콘솔출력 보충
    - 객체지향 다시
        - 객체지향 특징
        - 상속, 다중 상속

2. 파이썬 응용
    - 주소록 프로그램 [소스](https://github.com/KOOJAIN/studypython2023/edit/main/README.md)

![실행화면](https://github.com/KOOJAIN/studypython2023/blob/main/images/address.app.png?raw=true)
실행화면

## 7일차
1. 파이썬 응용
    - 주피터 노트북 사용법
        - 노트북 생성
    - 리스트 연산 추가
    - 자료구조 추가
    - 라이브러리 사용법
        - folium (지도 라이브러리)

## 8일차
1. 파이썬 응용
    - 라이브러리 사용법
        - urllib.request
    - 웹크롤링용 라이브러리 [소스] (https://github.com/KOOJAIN/studypython2023/blob/main/Day08/code44_web_crawling.ipynb)
        - 기상청 오늘의 날씨 크롤링
        - 데이터포털 OpenAPI 크롤링
        - BeautifulSoup 크롤링
        ![image](https://user-images.githubusercontent.com/123913898/217467573-3593672e-1a8e-4776-bda8-69271acb80c3.png)


        

## 9일차
1. 파이썬 응용
    - GUI 개발(PyQt)
    - 자료구조 추가
