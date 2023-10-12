# 1095 - Find in Mountain Array
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        mountain_length = mountain_arr.length()
        # find_center 
        start = 0
        end = mountain_length - 1
        #
        #print('find top') ########################
        remember = -1
        while end >= start:
            mid = (end + start) // 2
            #print(mid) #########################
            value = mountain_arr.get(mid)
            if mid < end:
                #print("get value_next", mid+1, end) #####################
                value_next = mountain_arr.get(mid + 1)
            # maybe we got lucky and already found it?
            if mid != end and value_next > value:
                #print('value_next > value', value_next, value)
                if value == target: 
                    return mid
                if value_next == target: 
                    return mid + 1
                start = mid + 2
            else:
                if value == target: 
                    remember = mid
                if mid != end and value_next < value:
                    if value_next == target: 
                        remember = mid + 1
                end = mid - 1
        mountain_top = mid

        #search_left
        #print('search_left') ########################
        start = 0
        end = mountain_top - 1
        while end >= start:
            mid = (end + start) // 2
            #print(mid, value) #########################
            value = mountain_arr.get(mid)
            # maybe we got lucky and already found it?
            if value == target: 
                return mid
            elif value < target:
                start = mid + 1
            elif value > target:
                end = mid - 1

        if remember != -1:
            #print("Remember",remember)
            return remember
        #search_right
        #print('search_right') ########################
        start = mountain_top + 1
        end = mountain_length - 1
        while end >= start:
            mid = (end + start) // 2
            value = mountain_arr.get(mid)
            #print(mid, value) #########################
            # maybe we got lucky and already found it?
            if value == target: 
                return mid
            elif value > target:
                start = mid + 1
            elif value < target:
                end = mid - 1
        return -1
            

