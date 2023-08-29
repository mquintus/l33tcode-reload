class Solution:
    def bestClosingTime(self, customers: str) -> int:
        local_penalty = 0
        n = len(customers)
        for i in range(n):
            if customers[i] == 'Y':
                local_penalty += 1

        min_penalty = local_penalty
        min_p_pos = 0
        for i in range(n):
            if customers[i] == 'Y':
                local_penalty -= 1
            else:
                local_penalty += 1

            if local_penalty < min_penalty:
                min_penalty = local_penalty
                min_p_pos = i + 1

        return min_p_pos 
