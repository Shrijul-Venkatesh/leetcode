class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0      # position we write to
        read = 0       # position we read from
        n = len(chars)

        while read < n:
            char = chars[read]
            count = 0

            # Count consecutive occurrences of chars[read]
            while read < n and chars[read] == char:
                read += 1
                count += 1

            # Write the character
            chars[write] = char
            write += 1

            # Write the count if > 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
