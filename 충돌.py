from vpython import *
#GlowScript 3.1 VPython

# ball, foot 만들기
ball = sphere(radius = 0.2) 
foot = sphere(radius = 0.4, pos = vec(1,0,0), color =color.red)

v1 = 1 #속도
v2 = -2
# 물리 성질 & 상수 초기화
ball.v = vec(v1,0,0) #ball의 초기속도
foot.v = vec(v2,0,0) #foot의 초기속도
ball.m = 2 #ball의 질량
foot.m = 4 #foot의 질량
ball.f = vec(0,0,0) #ball의 초기 알짜힘
foot.f = vec(0,0,0) #foot의 초기 알짜힘
e  = 1 #반발계수 
tot_energy = 0.5*ball.m*mag(ball.v)**2+0.5*foot.m*mag(foot.v)**2 

# 시간 설정
t = 0
dt = 0.03

# 화면 설정
scene.autoscale = True
scene.range = 5

# 충돌 처리 함수 
def collision(b, f, e):
    dist = mag(b.pos - f.pos)
    tot_m = b.m + f.m 
    # 충돌 시 두 물체의 속도 변경
    if dist < b.radius + f.radius: 
        v1 = ((b.m-e*f.m)*b.v + (1+e)*f.m*f.v) / tot_m
        v2 = ((f.m-e*b.m)*f.v + (1+e)*b.m*b.v) / tot_m
        b.v = v1
        f.v = v2
        return True
    else:
        return False

# 시뮬레이션 루프
while t < 3:
    rate(30)
    # 충돌 처리 (collision 함수 이용)
    colcheck = collision(ball,foot, e) 
    if colcheck == True:
        print("1m/s의 속도로 축구공을 바 로차서 8m/s 속도로 되돌려 보냈다")
        print("충격량은 운동량의 변화량과 같다\n")
        print("발이 축구공에 가한 충격량의 크기는 몇 N.s?인가?")
        print(("I = del_p = m x del_v = ") + ball.m + ("kg x (") + ball.v.x + " - " + v1 + ") =" + ((ball.v.x-v1)*ball.m) + " N.s ")
    # 속도, 위치 업데이트 (Euler – Cramer Method)
    ball.v = ball.v + ball.f/ball.m*dt 
    foot.v = foot.v + foot.f/foot.m*dt
    ball.pos = ball.pos + ball.v*dt
    foot.pos = foot.pos + foot.v*dt
    

    
    # 두 공의 총 에너지     
    tot_energy = 0.5*ball.m*mag(ball.v)**2+0.5*foot.m*mag(foot.v)**2
    # 시간 업데이트
    t = t + dt

