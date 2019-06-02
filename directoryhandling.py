def write(a,b):
    import os
    path=os.getcwd() + "\\test1234"
    #os.mkdir(path)
    f1=open("%s"%(a),'w')
    f1.write(b)
    f1.close()

def append(a,b):
    f1=open("%s"%(a),'a')
    f1.write(b)
    f1.close()

def read(a):
    f1=open("%s"%(a),'r')
    print(f1.read())
    f1.close()
print("Enter Your Choice")
x='''1- write on a file
     2- append a file
     3- read a file
     4- exit'''
print(x)
ch=int(input())
if(ch==1):
    print("enter path")
    m=input()
    print("enter content to write on a file")
    n=input()
    write(m,n)
elif(ch==2):
    print("enter path")
    m=input()
    print("enter content to append")
    n=input()
    append(m,n)
elif(ch==3):
    print("enter path")
    m=input()
    read(m)
else:
    exit()
    
