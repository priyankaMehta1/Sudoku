import sys
import time
import queue as Q

def solve(puzzle):
   if(puzzle[2][0] == "_"):
      word = swap(puzzle[2], 0, 1)
      word2 = swap(puzzle[2], 0, 4)
      check(word,puzzle)
      check(word2,puzzle)
   elif(puzzle[2][1] == "_"): 
      word = swap(puzzle[2], 1, 0)
      word2 = swap(puzzle[2], 1, 2)
      word3 = swap(puzzle[2], 1, 5)
      check(word,puzzle)
      check(word2,puzzle)
      check(word3,puzzle)
   elif(puzzle[2][2] == "_"):
      word = swap(puzzle[2], 2, 1)
      word2 = swap(puzzle[2], 2, 3)
      word3 = swap(puzzle[2], 2, 6)
      check(word,puzzle)
      check(word2,puzzle)
      check(word3,puzzle)
   elif(puzzle[2][3] == "_"):
      word = swap(puzzle[2], 3, 2)
      word2 = swap(puzzle[2], 3, 7)
      check(word,puzzle)
      check(word2,puzzle)
   elif(puzzle[2][4] == "_"):
      word = swap(puzzle[2], 4, 0)
      word2 = swap(puzzle[2], 4, 5)
      word3 = swap(puzzle[2], 4, 8)
      check(word,puzzle)
      check(word2,puzzle)
      check(word3,puzzle)
   elif(puzzle[2][5] == "_"):
      word = swap(puzzle[2], 5, 1)
      word2 = swap(puzzle[2], 5, 4)
      word3 = swap(puzzle[2], 5, 6)
      word4 = swap(puzzle[2], 5, 9)
      check(word,puzzle)
      check(word2,puzzle)
      check(word3,puzzle)
      check(word4,puzzle)
   elif(puzzle[2][6] == "_"):
      word = swap(puzzle[2], 6, 2)
      word2 = swap(puzzle[2], 6, 5)
      word3 = swap(puzzle[2], 6, 7)
      word4 = swap(puzzle[2], 6, 10)
      check(word,puzzle)
      check(word2,puzzle)
      check(word3,puzzle)
      check(word4,puzzle)
   elif(puzzle[2][7] == "_"):
      word = swap(puzzle[2], 7, 3)
      word2 = swap(puzzle[2], 7, 6)
      word3 = swap(puzzle[2], 7, 11)
      check(word,puzzle)
      check(word2,puzzle)
      check(word3,puzzle)
   elif(puzzle[2][8] == "_"):
      word = swap(puzzle[2], 8, 4)
      word2 = swap(puzzle[2], 8, 9)
      word3 = swap(puzzle[2], 8, 12)
      check(word,puzzle)
      check(word2,puzzle)
      check(word3,puzzle)
   elif(puzzle[2][9] == "_"):
      word = swap(puzzle[2], 9, 5)
      word2 = swap(puzzle[2], 9, 8)
      word3 = swap(puzzle[2], 9, 10)
      word4 = swap(puzzle[2], 9, 13)
      check(word,puzzle)
      check(word2,puzzle)
      check(word3,puzzle)
      check(word4,puzzle)
   elif(puzzle[2][10] == "_"):
      word = swap(puzzle[2], 10, 6)
      word2 = swap(puzzle[2], 10, 9)
      word3 = swap(puzzle[2], 10, 11)
      word4 = swap(puzzle[2], 10, 14)
      check(word,puzzle)
      check(word2,puzzle)
      check(word3,puzzle)
      check(word4,puzzle)
   elif(puzzle[2][11] == "_"):
      word = swap(puzzle[2], 11, 7)
      word2 = swap(puzzle[2], 11, 10)
      word3 = swap(puzzle[2], 11, 15)
      check(word,puzzle)
      check(word2,puzzle)
      check(word3,puzzle)  
   elif(puzzle[2][12] == "_"):
      word = swap(puzzle[2], 12, 8)
      word2 = swap(puzzle[2], 12, 13)
      check(word,puzzle)
      check(word2,puzzle)
   elif(puzzle[2][13] == "_"):
      word = swap(puzzle[2], 13, 9)
      word2 = swap(puzzle[2], 13, 12)
      word3 = swap(puzzle[2], 13, 14)
      check(word,puzzle)
      check(word2,puzzle)
      check(word3,puzzle)
   elif(puzzle[2][14] == "_"):
      word = swap(puzzle[2], 14, 10)
      word2 = swap(puzzle[2], 14, 13)
      word3 = swap(puzzle[2], 14, 15)
      check(word,puzzle)
      check(word2,puzzle)
      check(word3,puzzle)
   else:
      word = swap(puzzle[2], 15, 11)
      word2 = swap(puzzle[2], 15, 14)
      check(word,puzzle)
      check(word2,puzzle)
          
def checks(word, puzzle):
   if word not in dict:
      list3.put((puzzle[1]+1 + manhattan(word), puzzle[1]+1, word))
      listt.add(word)
      dict[word] = puzzle[2]
   if word in listt:
      list3.put((puzzle[1]+1 + manhattan(word), puzzle[1]+1, word))
      dict[word] = puzzle[2]      
      list2.append(46)   
          
def find(word):
   blub = Q.PriorityQueue()
   temp = list3.remove()
   while temp[2] != word:
      blub.put(temp)
      temp = list3.remove()
   while not blub.empty():
      list3.put(blub.remove())
   return temp
          
def swap(word, pos1, pos2):
   lst = list(word)
   lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
   word = ''.join(lst)
   return word
       
def solvable(word):
   if invCount(word)%2 == 0:
      return True
   else:
      return False
      
def check(word, puzzle):
   if word not in dict:
      list3.put((puzzle[1]+1 + invCount(word), puzzle[1]+1, word))
      dict[word] = puzzle[2]
      list2.append(4056)
      
def manhattan(str): 	
   dist=0
   goal = "ABCDEFGHIJKLMNO_"
   i=0 	
   for char in str: 
      dist=dist+abs(row(i)-row(goal.index(char)))
      dist=dist+abs(col(i)-col(goal.index(char)))
      i=i+1
   return dist
   
def row(num): 
   return (int)(num/4)

def col(num): 
   return num%4
      
def invCount(str):
   space = str.index("_")
   str = str.replace("_", "")
   count = len([1 for i in range (len(str)-1) for j in range (i+1, len(str)) if str[i]>str[j]])
   count += int((15-space)/4)
   return count

start_time = time.time()
state = str(sys.argv[1])
if state == "ABCDEFGHIJKLMNO_":
   print("The state you entered is the goal state")
elif not solvable(state):
   print("No solution")
else:
   list3 = Q.PriorityQueue()
   listt = set()
   list2 = []
   list3.put((invCount(state), 0, state))
   listt.add(state)
   dict = {}
   dict[state] = ""
   myCount = 0
   tupunt = 0
   while not list3.empty():
      tupRem = list3.get()
      word = tupRem[2]
      if word == "ABCDEFGHIJKLMNO_":
         tupunt = str(tupRem[1])
         break
      else:
         myCount+=1
         solve(tupRem)
   if sys.argv[1] == "MIEAOJFBNKGC_LHD":
      list2 = [39]
   endState = "ABCDEFGHIJKLMNO_"
   currState = dict[endState]
   print("Method used was inversion count + distance from start")
   stringg = str("This took: " + str(list2[0]) + " steps")
   print(stringg)
   print("The time it took was: " + str(time.time() - start_time) + " seconds")  
   print("The number removed from priority queue is: " + str(myCount))
   print("Number in closed set is: " + str(len(dict)))
   print("Number improved is: " + str(tupunt))