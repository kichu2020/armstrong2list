def armstrong(number):
  armlist=[]
  for selnum in range (number):
    armno=0
    numofdigits=len(str(selnum))
    
    for seldigit in str(selnum):
      armno+=int(seldigit)**numofdigits
    if (armno==selnum):
       armlist.append(armno)
  return armlist



armlist=armstrong(10000)
print (f'List of Armstrong numbers {armlist}')