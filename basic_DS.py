#Assignment 5
#Student name : Suhani
#Student number: 119220491


#Function returns the list of elements in the numeric list numlist which exceed all previous ele-ments.
#Arguments: Take input as list.
#Return:the list of elements which exceeds previous elements.
def peaks(numlist):
    maxvalue=numlist[0]-1
    outlist=[]
    for i in numlist:
        if i<=maxvalue:
            pass
        else:
            maxvalue = i
            outlist.append(i)
    return(outlist)




#Function to check if given number is cube or not.
#Arguments: Take input as number.
#Return: true if number is cube and false if it's not cube.
def is_cube(n):
    r = range(0, n) if n > 0 else range(n, 1)
    for val in r:
        cube_val = val ** 3
        if cube_val == n:
            return True
            break
    return False


#Function to find the nearest cube above the input number.
#Arguments: Take input as a number
#Return: the first cube value above the input number.

def firstcubeabove(n):
    search=False
    var=n
    while search !=True:
        var = var + 1
        num=is_cube(var)
        if num==True:
            return(var)
            search=False





