# Simulate a smart vaccuum cleaner that cleans a room size of nxn. The agent can move up, down, left and right.
# Calculate the overall performance.

import random
import time

# size of room n
n = 5

# randomising the room and its content
room = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        room[i][j] = random.randint(0, 1)


# function cleans data at given position (x,y) and prints it
def clean(i, j):
    room[i][j] = 0
    print("Room cleaned at {0}{1}.".format(i, j))


# function displays what is in the room
def display_rooms():
    for i in range(n):
        for j in range(n):
            print(str(room[i][j]), end=" ")
        print()


# function cleans the room. --> and returns number of cleaned rooms
def clean_rooms():
    row = 0
    col = 0
    counter = 0
    while row < n:
        if room[row][col] == 1:
            clean(row, col)
            counter += 1
        col += 1
        if col % n == 0:
            col = 0
            row += 1
    return counter


print("The room when dirty:")
display_rooms()

start = time.time()
counter = clean_rooms()
end = time.time()

print("\nThe room after cleaning:")
display_rooms()

performance = (counter/(n*n))*100
print("\nPerformance:", performance)
print("\nTotal number of rooms:{0} \nRooms cleaned: {1}".format(n*n, counter))
print("\nTime Taken:", abs(end-start))
