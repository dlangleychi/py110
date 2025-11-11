'''
P: given three integer angles, return invalid or type of triangle
E: 60, 70, 50 -> 'acute'
D: none
A: test validity, then conditional on max angle
C: below
'''

TRIANGLE_ANGLE_SUM = 180
RIGHT_ANGLE = 90

def triangle(angle1, angle2, angle3):
    angle1, angle2, angle3 = sorted([angle1, angle2, angle3])
    if angle1 + angle2 + angle3 != TRIANGLE_ANGLE_SUM or angle1 <= 0:
        return 'invalid'
    if angle3 < RIGHT_ANGLE:
        return 'acute'
    elif angle3 == RIGHT_ANGLE:
        return 'right'
    else:
        return 'obtuse'
    
print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True