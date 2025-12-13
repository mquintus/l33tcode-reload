# 3606 - Coupon Code Validator
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        sleeping = [-1] * numberOfUsers
        events.sort(key=lambda x: (int(x[1]), -1*ord(x[0][0])))
        for kind, timestamp, text in events:
            if kind == "OFFLINE":
                sleeping[int(text)] = int(timestamp) + 59
                continue
            
            for mention in text.split(" "):
                if mention == "ALL":
                    mentions = [i + 1 for i in mentions]
                    continue
                
                if mention == "HERE":
                    #print("HERE is mentioned while", sleeping)
                    for userid in range(numberOfUsers):
                        if sleeping[userid] < int(timestamp):
                            mentions[userid] += 1
                    continue

                userid = int(mention[2:])
                mentions[userid] += 1
                continue

        return mentions

