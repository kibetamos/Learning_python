#programe to display step by step proces to assemble ACME dryer

def main():
    startup_message()
    input('Press Enter to see Step 1 .')
    #Display ste 1
    step1()
    input('Press Enter to see Step 2')
    #Display step 2
    step2()
    input('Press Enter to see Step 3. ')

    #Display step 3
    step3()
    input('Press Enter to see Step 4. ')

    #Display step 4
    step4()


# The startup_message function displays the
# program's initial message on the screen.
    
def startup_message():
    print('This is how to disassemble an ACME laundry dryer')
    print('We have 4 steps in the process')


#Step 1
def step1():
    print('Step 1: Unplug the dryer and move it away from the wall' )

#step 2
def step2():
    print('Step 2: Remove the six screws from the back of the dryer')

#step 3
def step3():
    print('Step 3: Remove the back panel from th dryer')

#step 4
def step4():
    print('Step 4: Pull the top of the dryer straight up.')

main()