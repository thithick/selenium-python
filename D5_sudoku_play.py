# Python3 program to check whether
# given sudoku board is valid or not

# Checks whether there is any
# duplicate in current row or not
def notInRow(arr, row):

	# Set to store characters seen so far.
	st = set()

	for i in range(0, 9):

		# If already encountered before,
		# return false
		if arr[row][i] in st:
			return False

		# If it is not an empty cell, insert value
		# at the current cell in the set
		if arr[row][i] != '.':
			st.add(arr[row][i])

	return True

# Checks whether there is any
# duplicate in current column or not.
def notInCol(arr, col):

	st = set()

	for i in range(0, 9):

		# If already encountered before,
		# return false
		if arr[i][col] in st:
			return False

		# If it is not an empty cell, insert
		# value at the current cell in the set
		if arr[i][col] != '.':
			st.add(arr[i][col])

	return True

# Checks whether there is any duplicate
# in current 3x3 box or not.
def notInBox(arr, startRow, startCol):

	st = set()

	for row in range(0, 3):
		for col in range(0, 3):
			curr = arr[row + startRow][col + startCol]

			if curr in st:
				return False

			if curr != '.':
				st.add(curr)

	return True

# Checks whether current row and current
# column and current 3x3 box is valid or not
def isValid(arr, row, col):

	return (notInRow(arr, row) and notInCol(arr, col) and
			notInBox(arr, row - row % 3, col - col % 3))

def isValidConfig(arr):
	n=len(board)
	print(n)
	for i in range(0, n):
		for j in range(0, n):
			if not isValid(arr, i, j):
				return False

	return True

if __name__ == "__main__":

	board = [[ '5', '3', '.', '.', '7', '.', '.', '.', '.' ],
			[ '6', '.', '.', '1', '9', '5', '.', '.', '.' ],
			[ '.', '9', '8', '.', '.', '.', '.', '6', '.' ],
			[ '8', '.', '.', '.', '6', '.', '.', '.', '3' ],
			[ '4', '.', '.', '8', '.', '3', '.', '.', '1' ],
			[ '7', '.', '.', '.', '2', '.', '.', '.', '6' ],
			[ '.', '6', '.', '.', '.', '.', '2', '8', '.' ],
			[ '.', '.', '.', '4', '1', '9', '.', '.', '5' ],
			[ '.', '.', '.', '.', '8', '.', '.', '7', '9' ]]

	if isValidConfig(board):
		print("YES")
	else:
		print("NO")
