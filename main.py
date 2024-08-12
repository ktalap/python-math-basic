import matplotlib

# Without Tkinter window, program is unable to display anything
# I believe this fix is not needed if Linux has GUI
matplotlib.use('TkAgg')

from vector_drawing import *

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

draw(
    Points(*dino_vectors),
    Segment((6,4), (3,1))
)