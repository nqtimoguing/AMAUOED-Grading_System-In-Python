
print("\t\t\n\n AMAUOED GRADING POINT SYSTEM \n")

grade = int(input("\t Enter Grade:  "))

if grade > 96:
  print("\n\t Grade Point:    1.00")
  print("\t Grade Input:    A+")
  print("\t Description:    Excellent")
  print("\n \n")
  
elif grade < 96 and grade >= 91:
  print("\n\t Grade Point:    1.25")
  print("\t Grade Input:    A")
  print("\t Description:    Very Good")
  print("\n \n")

elif grade < 91 and grade >= 86:
  print("\n\t Grade Point:    1.50")
  print("\t Grade Input:    A-")
  print("\t Description:    Very Good")
  print("\n \n")

elif grade < 86 and grade >= 81:
  print("\n\t Grade Point:    1.75")
  print("\t Grade Input:    B+")
  print("\t Description:    Good")
  print("\n \n")

elif grade < 81 and grade >= 75:
  print("\n\t Grade Point:    2.00")
  print("\t Grade Input:    B")
  print("\t Description:    Good")
  print("\n \n")

elif grade < 75 and grade >= 69:
  print("\n\t Grade Point:    2.25")
  print("\t Grade Input:    B-")
  print("\t Description:    Good")
  print("\n \n")
  
elif grade < 69 and grade >= 63:
  print("\n\t Grade Point:    2.50")
  print("\t Grade Input:    C+")
  print("\t Description:    Fair")
  print("\n \n")

elif grade < 63 and grade >= 57:
  print("\n\t Grade Point:    2.75")
  print("\t Grade Input:    C")
  print("\t Description:    Fair")
  print("\n \n")

elif grade < 57 and grade >= 50:
  print("\n\t Grade Point:    3.00")
  print("\t Grade Input:    C-")
  print("\t Description:    Fair")
  
elif grade < 50:
  print("\n\t Grade Point:    5.00")
  print("\t Grade Input:    F")
  print("\t Description:    Failed")
  print("\n \n")

else:

  print("\n\t Grade Point:    IP")
  print("\t Grade Input:    IP")
  print("\t Description:    In Progress")
  print("\n \n")
  
 # End of the program