def CheckLeap(Year):
# Checking if the given year is leap year 
    if((Year % 400 == 0) or
      (Year % 100 != 0) and
      (Year % 4 == 0)):
      print("Given Year is a leap Year"); 
# Else it is not a leap year else:
    else:
      print ("Given Year is not a leap Year")



CheckLeap(2004)