class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xcount = 0
        ycount = 0


        if x < z:
            xcount = z - x
        else:
            xcount = x - z

        if y > z:
            ycount = y - z
        else:
            ycount = z - y
        
        if xcount < ycount :
            return 1
        if ycount < xcount:
            return 2
        else:
            return 0