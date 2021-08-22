from vpython import *
#GlowScript 3.1 VPython

ceiling = box(size=vec(10,0.1,10))
ball = sphere(pos=vec(15,-15,0),texture = textures.metal, make_trail = True)
rod = cylinder(axis=ball.pos,color = color.blue, radius = 0.1)

scene.center = vec(0,ball.pos.y,0)
scene.range = 20

ball.v = vec(0,0,0)
ball.w = 0*vec(0,0,1)
ball.m = 1 #질량
ball.I = ball.m*mag(ball.pos-ceiling.pos)**2


g = vec(0,-9.8,0) #중력
t = 0 #시간
dt = 0.01

while True:
    rate(1/dt)
    
    ball.f = ball.m*g
    ball.torque = cross(ball.pos - ceiling.pos, ball.f)
    
    ball.w = ball.w + ball.torque/ball.I*dt
    ball.dtheta = mag(ball.w)*dt
    ball.rotate(angle = ball.dtheta,axis = norm(ball.w), origin=ceiling.pos)
    rod.axis = ball.pos
    t = t + dt