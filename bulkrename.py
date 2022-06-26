import os
def main():
 i =0
 path = "C:/Users/larat/Documents/files/test/"
 for filename in os.listdir(path):
     mydest = "img"+str(i)+".jpg"
     mysource = path.filename
     my_dest = path +mydest
     os.rename(mysource, mydest)
      i+=1
if __name__ =='__main__':
   main()