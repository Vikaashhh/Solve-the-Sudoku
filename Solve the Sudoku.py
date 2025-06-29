class Solution:
    def solveSudoku(self, mat):
        # Har row, column aur box ke liye ek set banate hain jisme already placed numbers honge
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Pehle se jo numbers diye gaye hain unhe rows, cols aur boxes mein daal dete hain
        for r in range(9):
            for c in range(9):
                num = mat[r][c]
                if num != 0:
                    rows[r].add(num)
                    cols[c].add(num)
                    box_index = (r // 3) * 3 + (c // 3)
                    boxes[box_index].add(num)

        # Backtracking function jo puzzle ko solve karta hai
        def solve():
            for r in range(9):
                for c in range(9):
                    # Agar cell empty hai (0), to try karenge 1 se 9 tak ke numbers
                    if mat[r][c] == 0:
                        for num in range(1, 10):
                            box_index = (r // 3) * 3 + (c // 3)

                            # Check karte hain ki number already to nahi hai row, column ya box mein
                            if num not in rows[r] and num not in cols[c] and num not in boxes[box_index]:
                                # Number place karte hain
                                mat[r][c] = num
                                rows[r].add(num)
                                cols[c].add(num)
                                boxes[box_index].add(num)

                                # Recursively solve karte hain agar valid hai
                                if solve():
                                    return True

                                # Agar valid nahi nikla to backtrack karte hain
                                mat[r][c] = 0
                                rows[r].remove(num)
                                cols[c].remove(num)
                                boxes[box_index].remove(num)

                        # Agar 1 se 9 koi bhi number nahi chala to false return karenge
                        return False
            # Agar pura board fill ho gaya bina kisi conflict ke
            return True

        # Solve function call karte hain
        solve()
