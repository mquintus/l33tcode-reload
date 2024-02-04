# 76 - Minimum Window Substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""

        letter_counts = Counter(t)
        letter_found = 0

        start_pointer = 0
        end_pointer = 1
        min_length = 10**5 + 2
        solution = ""
        
        def process_new_letter(pointer, letter_found):
            el = s[pointer]
            if el in letter_counts.keys():
                # Part 2: We've found a first match
                if letter_counts[el] > 0:
                    letter_found += 1
                letter_counts[el] -= 1
                #print("Adding", el +',', 'total letters:', letter_found, letter_counts)
            return letter_found
        
        def process_remove_letter(pointer, letter_found):
            if pointer == -1:
                return 0
            el = s[pointer]
            if el in letter_counts.keys():
                # Part 2: We've found a first match
                if letter_counts[el] >= 0:
                    letter_found -= 1
                letter_counts[el] += 1

                #print('removing', el, 'now:')
                #print(letter_counts, letter_found)

            #print(letter_counts, letter_found)
            #print('removed', el)
            return letter_found
        
        # Part 1: We don't have any matching character.
        # We move forward.
        while s[start_pointer] not in letter_counts.keys():
            start_pointer += 1
            if start_pointer == len(s):
                break
            if end_pointer <= start_pointer:
                end_pointer = start_pointer + 1
        if start_pointer == len(s):
            return ""
        #print(s[start_pointer:end_pointer])
        letter_found = process_new_letter(start_pointer, letter_found)


        while start_pointer < len(s):
            # Part 3: We keep looking for further matches.
            while letter_found < len(t) and end_pointer < len(s):
                #print("ep, lf", end_pointer, letter_found)
                letter_found = process_new_letter(end_pointer, letter_found)
                #print(letter_counts)
                end_pointer += 1
            #print(s[start_pointer:end_pointer])
            #print("ep, lf", end_pointer, letter_found)
            #print(letter_counts)

            # Part 4: All letters have been found!
            if letter_found == len(t):
                #print('!!!!!!!!!!!!!')
                length = end_pointer - start_pointer
                if length < min_length:
                    solution = s[start_pointer:end_pointer]
                    #print(start_pointer, end_pointer, solution)
                    #print(letter_found, letter_counts)
                    min_length = length

            letter_found = process_remove_letter(start_pointer, letter_found)
            start_pointer += 1
   
        return solution
