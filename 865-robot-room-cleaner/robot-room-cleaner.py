# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        #         up      right. down.   left
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


        visited = set()

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell = (0, 0), dir = 0):
            visited.add(cell)
            robot.clean()
            r, c = cell
            for i in range(4):
                new_dir = (dir + i) % 4
                new_r = r + dirs[new_dir][0]
                new_c = c + dirs[new_dir][1]
                new_cell = (new_r, new_c)

                if new_cell not in visited and robot.move():
                    backtrack(new_cell, new_dir)
                    go_back()
                robot.turnRight()
        backtrack()