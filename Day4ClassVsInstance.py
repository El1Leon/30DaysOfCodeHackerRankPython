class Person:

    #__init__ is a reserved word in python

    def __init__(self,initialAge):
    

        # Add some more code to run some checks on initialAge
        #If initial age is less than 0

        if initialAge < 0:
            self.age = 0
            #print age is not valid
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct
        #  statement to the console
        #If age is less than 13, print "You are young"
        if self.age < 13:
            print("You are young.")
        #If less than 18,  print "You are a teenager"
        elif self.age in range(13,18):
            print("You are a teenager.")
        #Otherwise "You are old"
        else:
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1


t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")