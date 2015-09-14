#def main():
#    names = ["greenjoa1","greenjoa2", "greenjoa3"]
#    newName = input("Enter last guest : ")
#    names.append(newName)
#    printNames(names)
#    return
#def printNames(names):
#    for name in names:
#        print(name)
#        return
#main()

#def sum_and_mul(a,b):
#    return a+b,a*b

#data = sum_and_mul(3,4)
#sum,mul = sum_and_mul(3,4)
#print (sum,mul)

#coding: cp949
#def printData(data,level=0):
#    for item in data:
#        if isinstance(item,list):
#            printData(item,level+1)
#        else:
#            for i in range (level):
#                print("\t",end="")
#            print(item)

#data=["홍길동",["hello","world"],"김길동",["hello1","world1"],"똥길동",["hello2","world2"]]
#printData(data)

import os

help(os.mkdir)