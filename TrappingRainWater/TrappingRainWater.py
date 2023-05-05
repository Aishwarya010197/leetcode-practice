def TrappingRainWater(height):
    if not height:
        return 0
    
    n = len(height)
    left, right = 0, n-1
    max_left, max_right = height[0], height[n-1]
    water = 0
    
    while left <= right:
        if max_left <= max_right:
            water += max_left - height[left]
            max_left = max(max_left, height[left])
            left += 1
        else:
            water += max_right - height[right]
            max_right = max(max_right, height[right])
            right -= 1
    
    return water
