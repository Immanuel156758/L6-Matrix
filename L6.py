matrixA = [[1,2], [3,4]]
matrixB = [[5,6], [7,8]]
matrixC = [[0,0],[0,0]]
matrixD = [[0,0],[0,0]]
for i in range(0,2,1):
	for j in range(0,2,1):
		matrixC[i][j] = matrixA[i][j] + matrixB[i][j]
		matrixD[i][j] = matrixA[i][j] - matrixB[i][j]

		
print(matrixC)
print(matrixD)














"""r = int(input("How many rows do you want?"))
c = int(input("How many columns do you want?"))
matrix = []

for i in range(r):
	temp = []
	for j in range(c):
		l = int(input("What number do you want?"))
		temp.append(l)
	matrix.append(temp)
	
	
for i in range(r):
	print("\n")
	for j in range(c):
		print(matrix[i][j], end =" ")
"""









"""matrix = [[1,2,3,4,5],[6,7,8,9,0],[3,4,5,6,7],[0,2,4,6,8],[1,3,5,7,9]] 

for i in range(r):
	print("\n")
	for j in range(c):
		print(matrix[i][j], end =" ")
		"""