# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1800, 900)

point_0 = sd.get_point(600, 5)

def branch(point, angle, length, delta):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle - delta
    next_length = length * .75
    delta -= 5
    branch(point=next_point, angle=next_angle, length=next_length, delta=delta)
    branch(point=next_point,angle=next_angle,length=next_length,delta=-delta)


branch(point=point_0, angle=90, length=150, delta=30)

#
# for delta in range(0, 51, 10):
#     branch(point=point_0, angle=90, length=150, delta=delta)
# for delta in range(-50, 1, 10):
#     branch(point=point_0, angle=90, length=150, delta=delta)


sd.pause()