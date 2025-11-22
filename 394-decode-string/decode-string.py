class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ""

        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)   # build multi-digit number
            elif ch == '[':
                # push current context onto stack
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif ch == ']':
                # pop and expand
                prev_str, k = stack.pop()
                curr_str = prev_str + curr_str * k
            else:
                curr_str += ch   # normal letter

        return curr_str
