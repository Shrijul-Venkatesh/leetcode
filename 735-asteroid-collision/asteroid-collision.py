class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # process collisions
            while stack and stack[-1] > 0 and a < 0:
                # Compare sizes
                if stack[-1] < -a:      # stack asteroid is smaller → it explodes
                    stack.pop()
                    continue           # continue checking further collisions
                elif stack[-1] == -a:  # equal size → both explode
                    stack.pop()
                break                   # in both equal or larger case, current asteroid dies
            else:
                # If no break occurred, asteroid survives
                stack.append(a)

        return stack
