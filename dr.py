import simple_draw as sd

sd.resolution = (1200, 600)




def buble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2, color=sd.random_color())



for x in range(100):
    point = sd.random_point()
    buble(point, 5)
sd.pause()