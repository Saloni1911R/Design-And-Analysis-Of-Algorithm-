class Solution(object):

  def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
    """:type radius: int

    :type xCenter: int
    :type yCenter: int
    :type x1: int
    :type y1: int
    :type x2: int
    :type y2: int
    :rtype: bool
    """
    # Find the closest point on the rectangle to the circle center
    closest_x = max(x1, min(xCenter, x2))
    closest_y = max(y1, min(yCenter, y2))

    # Calculate the distance squared from the center to this closest point
    distance_x = xCenter - closest_x
    distance_y = yCenter - closest_y
    distance_squared = (distance_x**2) + (distance_y**2)

    # Return true if the distance is within the radius
    return distance_squared <= (radius**2)
