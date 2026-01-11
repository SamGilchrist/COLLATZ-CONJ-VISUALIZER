import matplotlib.pyplot as plt
import time as te

def Quit():
    print("Do You want to Quit  [yes = y ; no = n]")
    ask = input()
    if ask == 'n':
        pass
    elif ask == 'y':
        quit()

# List Declared (For Generation of Graph)
lst = []

# Main Code
intro()
while True:
    print(' ')
    Num = int(input("Enter the Number: "))
    print(Num)
    lst.append(Num)  # Adds The Elements in the Declared List (lst)

    # To Calculate the Number received frm the User as per "(3x + 1) Conjucture".
    while True:
        if Num == 1 or Num == -1 or Num == -5 or Num == -17:
            print("This is a Loop")
            break
        elif Num % 2 == 0:
            Num = Num // 2
            print(Num)
            lst.append(Num)
        elif Num % 2 != 0:
            Num = 3 * Num + 1
            print(Num)
            lst.append(Num)

    # Job Done... Time for Graph!

    # All for the Sake of X-Vertex...(Due to ERROR! :( ,because this Snake can't Handle things if the Number of
    # Elements in Both List are not Equal)
    # So...
    x = list(range(len(lst)))  # list of coordinates of X-axis
    y = lst                    # list of coordinates of Y-axis


    # Creating a Graph for the Set of Numbers Generated !
    plt.plot(x, y, marker='.', color='k')
    plt.title("3x + 1 Graph")
    plt.xlabel('Number of Times(Calculated) -->')
    plt.ylabel('Numbers -->')
    plt.show()

    # Clearing the list for Next Run!!
    lst.clear()

    # "DO YOU WANNA QUIT!"
    Quit()

#    Bug Fixes and Improvements:-
#        1)Add Intro and Outro Tunes if possible      [DONE]
#        2)Aligning Y-Axis
#        3)Text to Speech!!                           [DONE]
