def solution(wallpaper):
    answer = []
    
    nums_x = []
    nums_y =[]
    for i in range (len(wallpaper)):
        if ('#' in wallpaper[i]):
            nums_x.append(i)
            for j in range (len(wallpaper[i])):
                if wallpaper[i][j] == '#':
                    nums_y.append(j)

    top_x = min(nums_x)
    bottom_x = max(nums_x) + 1
    left_y = min(nums_y)
    right_y = max(nums_y) + 1

    answer = [top_x, left_y, bottom_x, right_y]
    
    return answer