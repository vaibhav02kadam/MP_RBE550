import turtle as tr

tr.color('green', 'yellow')
star_points = 5
angle_rot = 180/star_points

tr.begin_fill()

for i in range(0, star_points):
    tr.forward(200)
    tr.right(180-angle_rot)

tr.end_fill()
tr.done()
