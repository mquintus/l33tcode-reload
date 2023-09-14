origins = {}
        solutions = []
        tickets.sort()

        for orig, dest in tickets:
            if orig not in origins:
                origins[orig] = {}
            if dest not in origins[orig]:
                origins[orig][dest] = 0
            origins[orig][dest] += 1
        
        def solve(position, visited: List):
            if len(visited) == len(tickets):
                solutions.append([*visited, position])
                return True
            if position not in origins:
                return False

            for dst, tickets_left in origins[position].items():
                if tickets_left == 0:
                    continue
                
                origins[position][dst] -= 1
                success = solve(dst, [*visited, position])
                if success:
                    return True
                origins[position][dst] += 1
            return False

        success = solve("JFK", [])
        return solutions[0]


