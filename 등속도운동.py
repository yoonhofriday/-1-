from vpython import *
#GlowScript 3.1 VPython


# 공 만들기
ball = sphere(radius = 0.2) ##m

v = 1 # 속도

ball.pos = vec(-2,0,0) #공의 초기 위치 ##m
ball.v = vec(v,0,0) #공의 속도 = v  ##m/s 

# 시간 설정
t = 4 ##s
dt = 0.01 ##s


# 화살표 
attach_arrow(ball, "v", shaftwidth = 0.01, color = color.green) 

# 자취
attach_trail(ball, type = 'points', pps = 5) 

print("변위 = " + t*v + " m/s") 
print("평균속도 = " + v + " m/s")

# 시뮬레이션 루프 (rate 함수 이용)
while t > 0:
    rate(1/dt) 
    # 위치 업데이트 
    ball.pos = ball.pos + ball.v*dt 
    # 시간 업데이트
    t = t - dt
    
