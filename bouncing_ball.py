def bouncingBall(h, bounce, window):
    x = 0
    if h <= 0 or bounce <= 0 or bounce >=1 or window >= h:
        return -1
    while h > window:
        x += 1
        h *= bounce
        if h > window: x += 1
    return x

print(bouncingBall(3,1,1.5))
