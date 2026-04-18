class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pos_speed = zip(position, speed)
        pos_speed = sorted(pos_speed, reverse = True)
        # print(list(pos_speed))

        stack = []
        for pos, spd in pos_speed:
            time = (target - pos) / spd
            if not stack:
                stack.append(time)
            if time > stack[-1]:
                stack.append(time)
        return len(stack)


        
#         for pos in position


# 10 - 1 = 9 / 3 = 3 
# 10 - 4 = 6 / 2 = 3



# s = d / t 



#         10-4 = 6 / 2 = 3 
#         10-7 = 3 /1 = 3
#         10-1 = 9 / 2 = 4.5
#         10 - 0 = 10/1 = 10