#a=5
#b=10
#c=a+b
#print(c)

#import sys
#print(sys.version)
fo =open("D:\\isb superbrain\\warmupday1\\t1.txt",'w')
fo.write("hello world")
line_list=["Hello","how ae you\n","how is the weather"]
fo.writelines(line_list)


so =open("D:\\isb superbrain\\warmupday1\\t1.txt",'r')

sf=so.read()
fo.close()#very important
so.close()


# moving the files
import os
import shutil

#os.mkdir("the address")
#shutil.move("source path","destination path")
##shutil.copy("source path","destination path")
