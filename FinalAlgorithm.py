import sys
import time

def bruteForce(puzzle):
   puzzle = makeDeductions(puzzle)
   if puzzle == False:
      return ""
   if '.' not in puzzle: return puzzle
   i = findMin(puzzle)
   listy = moves[i][1]
   for char in listy:
      subPuz = puzzle[:]
      subPuz[i] = char
      bF = bruteForce(subPuz)
      if isinstance(bF,list):
         return bF
   
def findMin(puzzle):
   min = 10
   for i in moves:
      if moves[i][0] == 2 and puzzle[i] == ".":
         return i
      if moves[i][0] < min and puzzle[i] == ".":
         min = moves[i][0]
         pos = i
   return pos
   
def makeDeductions(puzzl):
   for i in range(len(puzzl)):
      if puzzl[i] == '.':
         mySet = set(table2[i])
         nums = ["1","2","3","4","5","6","7","8","9"]
         for j in range(len(mySet)):
            temp = mySet.pop()
            if puzzl[temp] in nums:
               nums.remove(puzzl[temp])
         length = len(nums)
         if length == 0:
            return False
         if length == 1:
            puzzl[i] = nums[0]    
         else:
            moves[i] = (length,nums)
   return puzzl

table = {0:[0,1,2,3,4,5,6,7,8],1:[9,10,11,12,13,14,15,16,17],2:[18,19,20,21,22,23,24,25,26],3:[27,28,29,30,31,32,33,34,35],
4:[36,37,38,39,40,41,42,43,44],5:[45,46,47,48,49,50,51,52,53],6:[54,55,56,57,58,59,60,61,62],7:[63,64,65,66,67,68,69,70,71],
8:[72,73,74,75,76,77,78,79,80],9:[0,9,18,27,36,45,54,63,72],10:[1,10,19,28,37,46,55,64,73],11:[2,11,20,29,38,47,56,65,74],
12:[3,12,21,30,39,48,57,66,75],13:[4,13,22,31,40,49,58,67,76],14:[5,14,23,32,41,50,59,68,77],15:[6,15,24,33,42,51,60,69,78],
16:[7,16,25,34,43,52,61,70,79],17:[8,17,26,35,44,53,62,71,80],18:[0,1,2,9,10,11,18,19,20],19:[3,4,5,12,13,14,21,22,23],
20:[6,7,8,15,16,17,24,25,26],21:[27,28,29,36,37,38,45,46,47],22:[30,31,32,39,40,41,48,49,50],23:[33,34,35,42,43,44,51,52,53],
24:[54,55,56,63,64,65,72,73,74],25:[57,58,59,66,67,68,75,76,77],26:[60,61,62,69,70,71,78,79,80]}

table2 = {}
for i in range(81):
   tabSet = set()
   for j in table:
      if i in table[j]:
         for x in table[j]:
            tabSet.add(x)
   table2[i] = tabSet

counttt = 0
start_time = time.time()
myFile = open("sudoku.txt", "r")
mylist = myFile.readlines()

counttt = 1
while counttt < 128:
   puzzly = mylist[counttt-1]
   start = time.time()
   print("Puzzle number: " + str(counttt))
   counttt +=1
   puzzl = list(str(puzzly))
   puzzl.remove("\n")
   moves = {}
   final = bruteForce(puzzl)
   print("Solution:")
   for i in range(0,9):
     print(final[i*9:i*9 + 9])
   print("The time it took was: " + str(time.time() - start) + " seconds")
print()
print("The time it took was: " + str(time.time() - start_time) + " seconds")