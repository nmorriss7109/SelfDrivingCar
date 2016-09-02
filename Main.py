import numpy as np

position = [0, -1]
direction = [1, 0]

drivingCourse1=np.ndarray((12,9))
drivingCourse1=np.array([[0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,3,1,1,1,1,0],[0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,2,1,1,1,4,0],[0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0]])

def move(position, direction, instruction):
	if instruction == 'f':
		print "Moving forward..."
		position[0] += direction[0]
		position[1] += direction[1]
	elif instruction == 'r':
		print "turning right..."
		direction = turn(direction, 'r')
	elif instruction == 'l':
		print "turning left..."
		direction = turn(direction, 'l')


	return position, direction

def turn(direction, way):
	#deppending on 'way' (l or r), direction is changed
	if way == 'r':
		if direction[0] == 1:
			direction[0] = 0
			direction[1] = -1
		elif direction[0] == -1:
			direction[0] = 0
			direction[1] = 1
		elif direction[1] == 1:
			direction[1] = 0
			direction[0] = 1
		else:
			direction[1] = 0
			direction[0] = -1
	elif way == 'l':
		if direction[0] == 1:
			direction[0] = 0
			direction[1] = 1
		elif direction[0] == -1:
			direction[0] = 0
			direction[1] = -1
		elif direction[1] == 1:
			direction[1] = 0
			direction[0] = -1
		elif direction[1] == -1:
			direction[1] = 0
			direction[0] = 1
	#returns new direction		
	return direction

while 1:
	aheadX = position[0] + direction[0]
	aheadY = position[1] + direction[1]

	if drivingCourse1[aheadY][aheadX] == 1:
		position, direction = move(position, direction, 'f')

	elif drivingCourse1[aheadY][aheadX] == 2 or drivingCourse1[aheadY][aheadX] == 3:
		if drivingCourse1[aheadY][aheadX] == 3:
			print "Arriving at red light..."
			print "Stopping..."
			print "Light turned green!"
		position, direction = move(position, direction, 'f')

		if direction[0] == 1:
			if drivingCourse1[aheadY - 1][aheadX] == 1:
				position, direction = move(position, direction, 'r')

		elif direction[1] == -1:
			if drivingCourse1[aheadY][aheadX + 1] == 1:
				position, direction = move(position, direction, 'l')
			elif drivingCourse1[aheadY][aheadX - 1] == 1:
				position, direction = move(position, direction, 'r')



		"""
		for i in range(aheadX, len(drivingCourse1[aheadY])):
			if drivingCourse1[aheadY][i] == 2 or drivingCourse1[aheadY][i] == 3 or drivingCourse1[aheadY][i] == 4:
				position, direction = move(position, direction, 'r')

		for i in range(aheadX):
			if drivingCourse1[aheadY][i] == 2 or drivingCourse1[aheadY][i] == 3 or drivingCourse1[aheadY][i] == 4:
				position, direction = move(position, direction, 'l')

		for i in range(aheadY, len(drivingCourse1)):
			if drivingCourse1[aheadX][i] == 2 or drivingCourse1[aheadX][i] == 3 or drivingCourse1[aheadX][i] == 4:
				position, direction = move(position, direction, 'f')
		"""
	elif drivingCourse1[aheadY][aheadX] == 4:
		print "Moving forward..."
		print "finished!"
		break
