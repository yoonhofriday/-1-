from vpython import *
#GlowScript 3.1 VPython
# 공 만들기
ball = sphere(radius = 0.3)

v = 0 #0초 속도
a = 3 #가속도

# 물리 성질 초기화
ball.pos = vec(-2,0,0) #공의 초기 위치 ##m
ball.v = vec(v,0,0) #공의 초기 속도 ##m/s
ball.a = vec(a,0,0) #공의 가속도 ##m/s**2

# 시간 설정
t = 2 ##s
dt = 0.01 ##s

# 자취 그리기
attach_trail(ball, type = 'points', pps = 5) 

print(t + "초후 속도 = "+ (v+a*t) + "m/s") # V =V0 + a x t
print("변위 = " + (v*t + (a*t*t)/2) + "m/s") # S = (V0 x t) + (a x t x t) / 2)
print("평균속도 = " + ((v+a*t)+v)/2 + "m/s") #평균속도 = (V0 +v) / 2

# 시뮬레이션 루프
while t > 0:
    rate(1/dt)
    # 속도, 위치 업데이트
    ball.v = ball.v + ball.a*dt
    ball.pos = ball.pos + ball.v*dt 
    # 시간 업데이트
    t = t - dt