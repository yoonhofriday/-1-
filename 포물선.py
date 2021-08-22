from vpython import *
#GlowScript 3.1 VPython
# 공, 바닥 만들기
ball = sphere(radius = 0.2)
ground =box(pos = vec(0,-4,0), size = vec(15,-0.01,5)) 

g = 9.8 #중력가속도
ball.pos = vec(-3,-2,0) #공의 초기 위치 ##m
ball.v = vec(2,15,0) #공의 초기 속도 ##m/s 
ball.a = vec(0,-g,0) #공의 가속도 ##m/s**2


# 시간 설정
t = 0 ##s
dt = 0.01##s


# 화살표 부착
#attach_arrow(ball, "v", shaftwidth = 0.1, color = color.green) 


#일정한 간격으로 점찍기
attach_trail(ball, type = 'points', pps = 10) 

print("던진방향 = " + ball.v)
print("중력가속도 = " + g+ " m/s")

# 시뮬레이션 루프 (공이 바닥에 닿을 때까지)
while ball.pos.y > ground.pos.y:
    rate(1/dt)
    # 속도, 위치 업데이트
    ball.v = ball.v + ball.a*dt 
    ball.pos = ball.pos + ball.v*dt 
    # 시간 업데이트
    t = t + dt 
