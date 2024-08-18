import matplotlib

# Without Tkinter window, program is unable to display anything
# I believe this fix is not needed if Linux has GUI
matplotlib.use('TkAgg')

from vector_drawing import *

# Drawing a dinosaur
#
# dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
#     (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
#     (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
# ]

# draw(
#     Points(*dino_vectors),
#     Polygon(*dino_vectors)
# )

# Drawing a parabola
# draw(
#     Points(*[(x, x**2) for x in range(-10, 11)]),
#     grid=(1,10),
#     nice_aspect_ratio=False
# )

draw (
    Points((2,2), (-1,3)),
    Segment((2,2), (-1,3), color=red)
)