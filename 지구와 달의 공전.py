from vpython import *
#GlowScript 3.1 VPython

# 지구, 달 만들기
Earth = sphere(pos = vec(0,0,0), radius = 6400000, texture = textures.earth)
Moon = sphere(pos = vec(385000e3,0,0), radius = 1737000, make_trail = True)

sf = 8 #크기 조정
Earth.radius = sf*Earth.radius
Moon.radius = sf*Moon.radius

G = 6.67e-11 #만유인력상수
Earth.mass = 5.972e24 #지구 질량
Moon.mass = 7.347e22 #달 질량
Earth.v = vec(0,0,0) #지구 초기 속도
Moon.v = vec(0,1022,0) #달 초기 속도
 
Earth.v = -Moon.v*Moon.mass/Earth.mass #궤도가 위로 올라가지 않게 하기위함(이줄제거시 달의초기속도때문에 궤도가 위로 올라감)


# 시간 설정
t = 0
dt = 60

while True:
    rate(1000)

    # 만유인력
    r = Moon.pos - Earth.pos
    Moon.f = -G*Earth.mass*Moon.mass/mag(r)**2*norm(r)
    Earth.f = -Moon.f #뉴턴 제 3 법칙 적용(작용 반작용)

    # 속도, 위치 업데이트
    Moon.v = Moon.v + Moon.f/Moon.mass*dt
    Earth.v = Earth.v + Earth.f/Earth.mass*dt
    Moon.pos = Moon.pos + Moon.v*dt
    Earth.pos = Earth.pos + Earth.v*dt

    # 시간 업데이트
    t = t + dt
    