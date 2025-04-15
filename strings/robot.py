""" 
Given a string representing the sequence of moves a robot vacuum makes, 
return whether or not it will return to its original position. 
The string will only contain L, R, U, and D characters, 
representing left, right, up, and down respectively.

Example:
"LR", return true
"URURD", return false
"RUULLDRD", return true

Solution: consider a 2D cartesian plane with coordinates (x, y). Also consider
the start position of the robot to be (0, 0). Then, for each
character of the s (that represents the movements of the robot), we do the following:

if s[i] = "U", then add 1 to the y-coord of the robot
if s[i] = "D", then subtract 1 from the y--coord of the robot
if s[i] = "R", then add 1 to the x-coord of the robot
if s[i] = "L", then subtract 1 from the x-coord of the robot.

Finally, the robot returned to its original position if after processing all the characters
of the string s he is back to coord (0, 0). :)
"""

# time complexity: O(n), where n is the size of the string 
# space complexity: O(1)
def process_movements(movements):
    
    x, y = (0, 0)
    for movement in movements:
        if movement == "D":
            y -= 1
        elif movement == "U":
            y += 1
        elif movement == "R":
            x += 1
        else:
            x -= 1

    return x == 0 and y == 0

def main():
    movements = input()
    print(process_movements(movements))


if __name__ == "__main__":
    main()

