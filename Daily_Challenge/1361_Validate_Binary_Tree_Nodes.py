# 1361 - Validate Binary Tree Nodes
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # What are the edge cases?
        # Loops
        # Reunifications
        # Disconnects
        
        # Only things that can be handled with a "visited" array

        # Question: Is 0 always the root node?
        # I can think of an approach where it doesn't matter

        visited = [False for _ in range(n)]
        parent = [-1 for _ in range(n)]

        for parentId, child in enumerate(leftChild):
            if child != -1:
                # No child can have two parents
                if parent[child] != -1:
                    print('# No child can have two parents')
                    return False
                parent[child] = parentId
        for parentId, child in enumerate(rightChild):
            if child != -1:
                # No child can have two parents
                if parent[child] != -1:
                    print('# No child can have two parents')
                    return False
                parent[child] = parentId
        
        root = -1
        for child, parentId in enumerate(parent):
            if parentId == -1:
                root = child
                #print('root', root)
                break
        if root == -1:
            print("No root node found")
            return False

        def check_downwards(i):
            visited[i] = True
            good = True
            children = [leftChild[i], rightChild[i]]
            for childId in children:
                # Check one: No child
                if childId == -1:
                    continue
                if childId == i:
                    # Immediate loop at i
                    print("Immediate loop at", i)
                    return False
                # check two: not already visited
                if visited[childId]:
                    print("already visited", childId)
                    return False
                visited[childId] = True
                if not check_downwards(childId):
                    return False
            return True
        
        success = check_downwards(root)
        if success:
            for i in range(n):
                if not visited[i]:
                    print("not visited", i)
                    return False

        return True
