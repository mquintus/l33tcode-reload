# 1488 - Avoid Flood in The City
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dry_days = list()
        rain_over_city = {}
        
        result = [-1] * len(rains)
        for i, r in enumerate(rains):
            if r == 0:
                dry_days.append(i)
                continue
            #print("Day ",i,"it's raining over",r)
            #print("dry_days:",dry_days)
            if r not in rain_over_city.keys():
                rain_over_city[r] = i
            elif r in rain_over_city.keys():
                when_to_dry_index = bisect.bisect_left(dry_days, rain_over_city[r])
          #      if rain_over_city[r] == len(dry_days): 
          #          print("The day that it rains over city",r,"is", rain_over_city[r], "which equals then length of dry_days", dry_days) 
                if when_to_dry_index == len(dry_days): 
                    return []
                
                #print("The index of day to dry ",when_to_dry_index," city",r,"but it rained at", rain_over_city[r], "and now it's raining again",i),  
                when_to_dry = dry_days[when_to_dry_index]
                #print("Drying city",r,"at",when_to_dry)
                result[when_to_dry] = r
                rain_over_city[r] = i
                del dry_days[when_to_dry_index]
        for i in range(len(result)):
            if result[i] == -1 and rains[i] == 0:
                result[i] = 1
        return result
