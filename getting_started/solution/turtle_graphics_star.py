import turtle as tr

tr.color('green', 'orange')
tr.begin_fill()
triangle_count = 0
search_count = 0
leg_count = 0

while True:
    tr.forward(200)  #Moves turtle forward 

    if leg_count < 2:
        tr.right(120)  #Turns turtle clockwise
        leg_count += 1

    if abs(tr.pos()) < 1 and leg_count == 2:
        leg_count = 0
        triangle_count += 1
        
    if abs(tr.pos()) < 1 and triangle_count == 3:
        triangle_count = 0
      
        if abs(tr.pos()) < 1 and search_count < 3:
            tr.right(30)
            search_count += 1

    if search_count == 3:
        break


tr.end_fill()
tr.done()