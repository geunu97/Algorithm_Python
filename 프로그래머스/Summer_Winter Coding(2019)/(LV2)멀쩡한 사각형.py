import math

def solution(w,h):
    return (w*h) - (w+h-math.gcd(w,h))
    




#이 문제는 위와 같이 최대공약수 사용하고, 공식을 외우면 된다

#수가 1억까지 범위기 때문에, 최대공약수 구할 때 위와 같이 유클리드로 최대공약수를 구해야한다