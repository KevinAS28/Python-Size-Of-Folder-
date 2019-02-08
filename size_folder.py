#by Kevin A.S
#sort all folder size
import os

startfol = input("Start folder: ")
list_fol = []
size_fol = []

def folornot(berkas):
 try:
  start_dir = os.getcwd()
  os.chdir(berkas)
  os.chdir(start_dir)
  return True
 except NotADirectoryError:
  return False
for i in list(os.listdir(startfol)):
 try:
  if (folornot(os.path.join(startfol, i))):
   list_fol.append(os.path.join(startfol, i))
 except Exception as error:
  print("error while indexing %s" %(str(error)))
  continue


print("Counting...")
a=0
ang = 0
for i in list_fol:
 size = 0
 size_temp = 0
 for root, dirs, files in os.walk(top=i, topdown=False):
  for a in files:
   try:
    with open(os.path.join(root, a), "rb") as baca:
     for nung in baca:
       size_temp += len(nung)
     size += size_temp #dalam bytes
     size_temp = 0
   except:
    print("error while reading file at %s" %(os.path.join(root, a)))
 size_fol.append((size/1000000, ang))
 del size
 ang+=1
tersortir = sorted(size_fol)
for i in range(len(list_fol)):
 print(list_fol[tersortir[i][1]], " ", tersortir[i][0], " MB")
