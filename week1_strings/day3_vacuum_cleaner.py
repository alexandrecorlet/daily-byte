# This question is asked by Amazon. Given a string representing the sequence of moves a robot 
# vacuum makes, return whether or not it will return to its original position. The string will 
# only contain L, R, U, and D characters, representing left, right, up, and down respectively.
# (c) Alexandre Corlet


# Time Complexity: O(n) | Space Complexity: O(1)
# where n is the size of the string
def returned_to_origin(moves):
    """ Given a string representing the sequence of moves
    of a robot, this function checks if the robot has
    returned to its original position (0,0)
    """
    x = y = 0
    for move in moves:
        # move horizontally => x-axis
        if move == "L":
            x -= 1
        elif move == "R":
            x += 1
        # move vertically => y-axis
        if move == "U":
            y += 1
        elif move == "D":
            y -= 1
    # Check if (x, y) point is the origin
    return (x, y) == (0, 0)

        


def main():
    # Test cases 
    assert returned_to_origin("LR")
    assert not returned_to_origin("URURD")
    assert returned_to_origin("RUULLDRD")
    print("OK: passed all test cases!")


if __name__ == "__main__":
    main()

