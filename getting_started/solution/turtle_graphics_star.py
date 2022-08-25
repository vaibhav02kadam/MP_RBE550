import turtle as tr
tr.color('green', 'orange')
tr.begin_fill()
while True:
    tr.forward(200)
    tr.left(170)
    if abs(tr.pos()) < 1:
        break
tr.end_fill()
tr.done()