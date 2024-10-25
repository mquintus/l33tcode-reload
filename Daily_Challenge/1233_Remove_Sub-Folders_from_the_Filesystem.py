# 1233 - Remove Sub-Folders from the Filesystem
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        shortestPrefixes = set()
        folder.sort()
        #print(folder)
        for path in folder:
            prefixes = path.split('/')[1:]
            for length in range(1, len(prefixes)):
                #print("Looking for",tuple(prefixes[:length]))
                if tuple(prefixes[:length]) in shortestPrefixes:
                    #print("Found",tuple(prefixes[:length]))
                    break
            else:
                #print("Adding", tuple(prefixes))
                shortestPrefixes.add(tuple(prefixes))
        return ["/" + "/".join(prefix) for prefix in shortestPrefixes]

