# sample1=input("enter file name")  
# sample2=input("enter second file name")
# temp=sample2

# sample1=sample2
# sample2=sample1


# def SwapFiles():
   

#     fileName=input("enter file name")
#     file=open(fileName,'r')
def swapFileData():    
    sample1 = input("enter files name:- ")    
    sample2 = input("enter files name:- ")
    with open(file1, 'r') as a:    data_a = a.read()
    with open(file2, 'r') as b:    data_b = b.read()
    with open(file1, 'w') as a:    a.write(data_b)
    with open(file2, 'w') as b:    b.write(data_a)
swapFileData()
    





