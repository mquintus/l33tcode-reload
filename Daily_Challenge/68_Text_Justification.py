class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        is_last_line = False

        i = 0
        curr_line_length = -1

        result = []
        current_line = []

        while i < len(words):
            next_word = words[i]
            additional_length = 1 + len(next_word)
            #print(next_word, curr_line_length + additional_length)

            if curr_line_length + additional_length > maxWidth:
                result.append(current_line) 
                current_line = []
                curr_line_length = -1
            else:
                curr_line_length += additional_length
                current_line.append(next_word)
                i += 1
        result.append(current_line) 

        result_strings = []
        for l, line in enumerate(result):
            # last line is left justified
            if l == len(result) - 1:
                result_strings.append(" ".join(line).ljust(maxWidth))
                continue
            # if only one word is in the line, right fill
            if len(line) == 1:
                result_strings.append("".join(line).ljust(maxWidth))
                continue

            gaps_per_line = len(line) - 1
            spaces_per_line = maxWidth - len("".join(line))
            spaces_per_gap = spaces_per_line // gaps_per_line
            vacant_spaces = spaces_per_line - spaces_per_gap * gaps_per_line

            v = 0
            result_string = ""
            for word in line[:-1]:
                result_string += word + " " * spaces_per_gap
                if v < vacant_spaces:
                    result_string += " "
                v += 1
            result_string += line[-1]
            result_strings.append(result_string)

        return result_strings

            
