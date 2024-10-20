# 1106 - Parsing A Boolean Expression
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def parse(p1,depth):
            #print("  " *depth,p1, expression[p1])
            if expression[p1] == 't': return True, p1+1
            if expression[p1] == 'f': return False,p1+1
            value = None
            pm = p1+2
            while pm < len(expression):
                #print("  " *depth,expression[pm])
                if expression[pm] == ')':
                    #if value: print("  " *depth,"True")
                    #else: print("  " *depth,"False")
                    return value,pm+1
                if expression[pm] == ',':
                    subvalue, pm = parse(pm+1, depth+1)
                    if expression[p1] == '|': value |= subvalue
                    if expression[p1] == '&': value &= subvalue
                else:
                    value,pm = parse(pm, depth+1)
                    if expression[p1] == '!': value = not value
            return value, pm+1
        return parse(0, 0)[0]
