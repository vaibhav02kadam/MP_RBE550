import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.collections as coll

from PIL import Image, ImageDraw


wid = 1
hei = 1
nrows = 10
ncols = 10
inbetween = 0.1
my_dpi = 100


xx = np.arange(0, ncols, (wid+inbetween))
yy = np.arange(0, nrows, (hei+inbetween))

image = Image.new(mode="RGB", size=(1500, 1500), color="white")

fig = plt.figure(figsize=(150, 150))
ax = plt.subplot(111, aspect='equal')


fig, ax = plt.subplots(1)
# ax.imshow(image)

# pat = []
# for xi in xx:
#     for yi in yy:
#         sq = patches.Rectangle((xi, yi), wid, hei, fill=True, facecolor="b")
#         ax.add_patch(sq)

# ax.axis([0,ncols+1,0,nrows+1])
# pat.append(sq)


plt.axis('off')
plt.savefig('test.png', dpi=my_dpi)
plt.show()
