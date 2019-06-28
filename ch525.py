"""
5.25 LAB*: Program: Drawing a half arrow
This program outputs a downwards facing arrow composed of a rectangle and a right triangle. The arrow dimensions are defined by user specified arrow base height, arrow base width, and arrow head width.

(1) Modify the given program to use a loop to output an arrow base of height arrow_base_height. (1 pt)



(2) Modify the given program to use a loop to output an arrow base of width arrow_base_width. (1 pt)



(3) Modify the given program to use a loop to output an arrow head of width arrow_head_width. (2 pts)



(4) Modify the given program to only accept an arrow head width that is larger than the arrow base width. Use a loop to continue prompting the user for an arrow head width until the value is larger than the arrow base width. (1 pt)

while arrow_head_width <= arrow_base_width:
    arrow_head_width = int(input('Enter arrow head width:\n'))
"""


arrow_base_height = int(input('Enter arrow base height:\n'))

arrow_base_width = int(input('Enter arrow base width:\n'))

arrow_head_width = int(input('Enter arrow head width:\n'))

while arrow_head_width <= arrow_base_width:
    arrow_head_width = int(input('Enter arrow head width:\n'))

print('')
# Draw arrow base (height = 3, width = 2)
for i in range(arrow_base_height):
    print("*" * arrow_base_width)

# Draw arrow head (width = 4)

while arrow_head_width > 0:
    print("*" * arrow_head_width)
    arrow_head_width -= 1
