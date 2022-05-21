#*/ Mock Banking App
# BankingApp.py
# Ralph Graham
# rgraha03*/

from graphics import *
from random import randrange
from os import path

# Creating a class for transactions (CLOD)
class Transaction:
    def __init__(self, name, accnum, balance, type):
        self.name = name
        self.accnum = accnum
        self.balance = balance
        self.type = type

    # Displaying transaction object
    def display(self, i):
        TextString=str(self.name)+"\t"+str(self.accnum)+"\t"+str(self.balance)+"\t"+str(self.type)
        self.aText=Text(Point(0,i), TextString)
        self.aText.setFill("blue")
        self.aText.draw(win)

# Creating a class for save data (CLOD)
class SaveData:
    def __init__(self, password, save=False, textfile1=None, textfile2=None):
        self.password = password
        self.textfile1 = textfile1
        self.textfile2 = textfile2
        self.save = save

    # Writing the save data to a text file (FNC)
    def write(self):
        outfile=open("savefile.txt","w")
        print(self.password,self.save,self.textfile1,self.textfile2, file=outfile) # (OFL)
        outfile.close()


# Setting attributes of the window (GFW)
def setUpWindow():
    win=GraphWin("Banking App", 600,600)
    win.setCoords(-12,-12,12,12)
    return win

# Randomly generating a greeting, a background color, and a password from their lists and returning their values (FNC)
def random():
    greetList=["Welcome!", "Hello There!", "Let's Get Started!", "Good Morning!"]
    colorList=["orange","yellow","green"]
    passList=["fast","happy","fresh","lynx","art","super"]
    r=randrange(4) # (RND)
    greeting=greetList[r]
    r=randrange(3) # (RND)
    color=colorList[r]
    r=randrange(6) # (RND)
    password=passList[r]
    return greeting, color, password

#  Displaying the very first menu of the program consisting of account selection and the returned values from
#  random() (FNC)
def intro(g, c, p):
    win.setBackground(c)

    aGreeting=Text(Point(0,2), g)
    aGreeting.setSize(21)
    aGreeting.setStyle("bold")
    aGreeting.draw(win)

    aPassword = Text(Point(0, -11), "Your password will be: " + p)
    aPassword.setStyle("bold italic")
    if p=="":
        ...
    else:
        aPassword.draw(win)

    checking1=Rectangle(Point(-10,-2), Point(-2,-4))
    checking1.setFill("dodgerBlue")
    checking1Text=Text(checking1.getCenter(), "Checking #1")
    checking1.draw(win)
    checking1Text.draw(win)
    checking2=Rectangle(Point(2, -2), Point(10, -4))
    checking2.setFill("red")
    checking2Text=Text(checking2.getCenter(), "Checking #2")
    checking2.draw(win)
    checking2Text.draw(win)

    mouseClick=win.getMouse()
    if mouseClick.getX()<0 and mouseClick.getY()<0: # (IMS)
        interface="checking1"
        aGreeting.undraw()
        aPassword.undraw()
        checking1.undraw()
        checking2.undraw()
        checking1Text.undraw()
        checking2Text.undraw()
        win.setBackground("white")
        return p, interface
    elif mouseClick.getX()>0 and mouseClick.getY()<0: # (IMS)
        interface="checking2"
        aGreeting.undraw()
        aPassword.undraw()
        checking1.undraw()
        checking2.undraw()
        checking1Text.undraw()
        checking2Text.undraw()
        win.setBackground("white")
        return p, interface

# Displaying a screen with a password prompt (FNC)
def login(password):
    aRectangle=Rectangle(Point(-10,3), Point(10,-3))
    aRectangle.setFill("black")
    aRectangle.draw(win)

    passPrompt=Text(Point(-1, 0), "Enter password:")
    passPrompt.setFill("white")
    passPrompt.draw(win)
    passBox=Entry(Point(2,0), 5); passBox.draw(win) # (OTXT)

    submitButton=Rectangle(Point(-3,-5), Point(3,-6))
    submitButton.setFill("red")
    submitButtonText=Text(Point(0,-5.5), "Submit")
    submitButton.draw(win)
    submitButtonText.draw(win)

    win.getMouse()
    if passBox.getText() == password: # Correct password will take you to the main menu (IEB)
        aRectangle.undraw()
        passPrompt.undraw()
        passBox.undraw()
        submitButton.undraw()
        submitButtonText.undraw()
        mainMenu()
    else: # Incorrect passwords will trigger an error message until the correct one is entered (IEB)
        error=Text(Point(0,-4), "Error: Incorrect password. Please try again.")
        error.draw(win)
        while passBox.getText() != password: # (IEB)
            win.getMouse()
            if passBox.getText() == password: # (IEB)
                aRectangle.undraw()
                passPrompt.undraw()
                passBox.undraw()
                submitButton.undraw()
                submitButtonText.undraw()
                error.undraw()
                mainMenu()
            else:
                ...

# Displaying the main menu with transaction, transfer, check, and print options (FNC)
def mainMenu():
    aTitle=Text(Point(-7,8), "Main Menu"); aTitle.setSize(36); aTitle.setStyle("bold"); aTitle.draw(win)

    option1=Rectangle(Point(-10,6), Point(-2,3))
    option1.setFill("dodgerBlue")
    option1Text=Text(option1.getCenter(), "Transactions")
    option1.draw(win)
    option1Text.draw(win)
    option2=Rectangle(Point(2,6), Point(10,3))
    option2.setFill("lightGreen")
    option2Text=Text(option2.getCenter(), "Write Check")
    option2.draw(win)
    option2Text.draw(win)
    option3=Rectangle(Point(-10,-6), Point(-2,-3))
    option3.setFill("orange")
    option3Text=Text(option3.getCenter(), "Transfer Money")
    option3.draw(win)
    option3Text.draw(win)
    option4=Rectangle(Point(2,-6), Point(10,-3))
    option4.setFill("yellow")
    option4Text=Text(option4.getCenter(), "Print Statement")
    option4.draw(win)
    option4Text.draw(win)

    mouseClick = win.getMouse()
    if mouseClick.getX() < 0 and mouseClick.getY() > 0: # (IMS)
        aTitle.undraw()
        option1.undraw(); option2.undraw(); option3.undraw(); option4.undraw()
        option1Text.undraw(); option2Text.undraw(); option3Text.undraw(); option4Text.undraw()
        if interface == "checking1":
            Transactions1()
        elif interface == "checking2":
            Transactions2()
    elif mouseClick.getX() > 0 and mouseClick.getY() > 0: # (IMS)
        aTitle.undraw()
        option1.undraw(); option2.undraw(); option3.undraw(); option4.undraw()
        option1Text.undraw(); option2Text.undraw(); option3Text.undraw(); option4Text.undraw()
        writeCheck()
    elif mouseClick.getX() < 0 and mouseClick.getY() < 0: # (IMS)
        aTitle.undraw()
        option1.undraw(); option2.undraw(); option3.undraw(); option4.undraw()
        option1Text.undraw(); option2Text.undraw(); option3Text.undraw(); option4Text.undraw()
        transferMoney()
    elif mouseClick.getX() > 0 and mouseClick.getY() < 0: # (IMS)
        aTitle.undraw()
        option1.undraw(); option2.undraw(); option3.undraw(); option4.undraw()
        option1Text.undraw(); option2Text.undraw(); option3Text.undraw(); option4Text.undraw()
        printStatment()

# Importing the input file the user enters to record transactions for Checking #1 (FNC)
def Transactions1():
    aTitle = Text(Point(-6, 9), "Transactions"); aTitle.setSize(36); aTitle.setStyle("bold"); aTitle.draw(win)

    aBalance = Text(Point(8, 9), ("Balance: " + "{0:0.2f}".format(0))); aBalance.setFill("red"); aBalance.setStyle("bold"); aBalance.draw(win)

    aRectangle=Rectangle(Point(-10,8), Point(10,-8)); aRectangle.draw(win)

    aPrompt=Text(Point(-2,-9), "Enter input file name for update:"); aPrompt.draw(win)

    aBox=Entry(Point(3,-9), 10); aBox.draw(win) # (OTXT)

    submitButton=Rectangle(Point(-3,-10), Point(3,-11))
    submitButton.setFill("red")
    submitButtonText=Text(Point(0,-10.5), "Submit")
    submitButtonText.setFill("white")
    submitButton.draw(win)
    submitButtonText.draw(win)

    if saveFileExists == True and contentData[2]!="None":
        aPrompt.undraw()
        aBox.undraw()
        aBox.setText(contentData[2])
        infile = open(contentData[2], "r")
        saving = SaveData(contentData[0], True, aBox.getText(),contentData[3]) # Using entry towards instance data for save data (CLOD), (IEB)
    elif saveFileExists==True and contentData[2]=="None":
        win.getMouse()
        infile = open(aBox.getText(), "r")
        saving = SaveData(contentData[0], True, aBox.getText(),contentData[3]) # (CLOD), (IEB)
    else:
        win.getMouse()
        infile = open(aBox.getText(), "r")
        saving = SaveData(p, True, aBox.getText()) # (CLOD), (IEB)

    infile.readline() # (IFL)
    i=7
    bal1=0
    for line in infile: # (IFL)
        lineList = line.split() # (LOOD)
        bal1 = bal1 + float(lineList[2])
        t=Transaction(lineList[0], lineList[1], lineList[2], lineList[3]) # (CLOD)
        t.display(i)
        i=i-1
    if bal1 < 0:
        overdraft(aBox.getText(),1)
    aBalance.setText("Balance: " + "{0:0.2f}".format(bal1))

    submitButtonText.setText("Exit")
    saving.write()
    win.getMouse()
    win.close()

# Importing the input file the user enters to record transactions for Checking #2 (FNC)
def Transactions2():
    aTitle = Text(Point(-6, 9), "Transactions"); aTitle.setSize(36); aTitle.setStyle("bold"); aTitle.draw(win)

    aBalance = Text(Point(8, 9), ("Balance: " + "{0:0.2f}".format(0))); aBalance.setFill("red"); aBalance.setStyle("bold"); aBalance.draw(win)

    aRectangle = Rectangle(Point(-10, 8), Point(10, -8)); aRectangle.draw(win)

    aPrompt = Text(Point(-2, -9), "Enter input file name for update:"); aPrompt.draw(win)

    aBox = Entry(Point(3, -9), 10); aBox.draw(win) # (OTXT)

    submitButton = Rectangle(Point(-3, -10), Point(3, -11))
    submitButton.setFill("red")
    submitButtonText = Text(Point(0, -10.5), "Submit")
    submitButtonText.setFill("white")
    submitButton.draw(win)
    submitButtonText.draw(win)

    if saveFileExists==True and contentData[3]!="None":
        aPrompt.undraw()
        aBox.undraw()
        aBox.setText(contentData[3])
        infile = open(contentData[3], "r")
        saving = SaveData(contentData[0], True, contentData[2], aBox.getText()) # Using entry towards instance data for save data (CLOD), (IEB)
    elif saveFileExists==True and contentData[3]=="None":
        win.getMouse()
        infile = open(aBox.getText(), "r")
        saving = SaveData(contentData[0], True, contentData[2], aBox.getText()) # (CLOD), (IEB)
    else:
        win.getMouse()
        infile = open(aBox.getText(), "r")
        saving = SaveData(p, True, None, aBox.getText()) # (CLOD), (IEB)

    infile.readline() # (IFL)
    i = 7
    bal2 = 0
    for line in infile: # (IFL)
        lineList = line.split() # (LOOD)
        bal2 = bal2 + float(lineList[2])
        t = Transaction(lineList[0], lineList[1], lineList[2], lineList[3]) # (CLOD)
        t.display(i)
        i = i - 1
    if bal2 < 0:
        overdraft(aBox.getText(),2)
    aBalance.setText("Balance: " + "{0:0.2f}".format(bal2))

    submitButtonText.setText("Exit")
    saving.write()
    win.getMouse()
    win.close()

# Displaying an interactive check and recording the transaction by using the amount of $ entered (FNC)
def writeCheck():
    aTitle = Text(Point(-6, 9), "Write Check"); aTitle.setSize(36); aTitle.setStyle("bold"); aTitle.draw(win)

    checkImage = Image(Point(0,0), "check.gif"); checkImage.draw(win)

    date = Entry(Point(3.5,2), 6); date.draw(win) # (OTXT)
    payTo = Entry(Point(-2,1), 20); payTo.draw(win) # (OTXT)
    numDollars = Entry(Point(5.75,1), 6); numDollars.draw(win) # (OTXT)
    textDollars = Entry(Point(-2,0), 30); textDollars.draw(win) # (OTXT)
    memo = Entry(Point(-4,-2), 15); memo.draw(win) # (OTXT)
    sign = Entry(Point(3.5, -2), 20); sign.draw(win) # (OTXT)

    submitButton = Rectangle(Point(-3, -10), Point(3, -11))
    submitButton.setFill("red")
    submitButtonText = Text(Point(0, -10.5), "Submit")
    submitButtonText.setFill("white")
    submitButton.draw(win)
    submitButtonText.draw(win)

    win.getMouse()

    if saveFileExists==True:
        if interface=="checking1" and contentData[2]!="None":
            infile = open(contentData[2], "r")
            transactionList1 = infile.readlines(); infile.close() # (LOOD), (IFL)
            outfile = open(contentData[2], "w")
            if len(transactionList1) > 1:
                print(transactionList1[0], end="", file=outfile) # (OFL)
            else:
                print(transactionList1[0], file=outfile)
            print("accchk",1,"-"+numDollars.getText(),"check", file=outfile) # (IEB), (OFL)
            for i in range(1, int(len(transactionList1))):
                print(transactionList1[i], end="", file=outfile) # (OFL)
            outfile.close(); aPrompt = Text(Point(0, -9), "Check written!"); aPrompt.draw(win)
        elif interface=="checking1" and contentData[2]=="None":
            aError = Text(Point(0, -9), "Error: Please update transaction file for Checking #2"); aError.draw(win)
        elif interface=="checking2" and contentData[3]!="None":
            infile = open(contentData[3], "r")
            transactionList2 = infile.readlines(); infile.close() # (LOOD), (IFL)
            outfile = open(contentData[3], "w")
            if len(transactionList2) > 1:
                print(transactionList2[0], end="", file=outfile) # (OFL)
            else:
                print(transactionList2[0], file=outfile) # (OFL)
            print("accchk",2,"-"+numDollars.getText(),"check", file=outfile) # (IEB), (OFL)
            for i in range(1, int(len(transactionList2))):
                print(transactionList2[i], end="", file=outfile) # (OFL)
            outfile.close(); aPrompt = Text(Point(0, -9), "Check written!"); aPrompt.draw(win)
        elif interface=="checking2" and contentData[3]=="None":
            aError = Text(Point(0, -9), "Error: Please update transaction file for Checking #1"); aError.draw(win)
    else:
        aError = Text(Point(0, -9), "Error: Please update transaction files"); aError.draw(win)

    submitButtonText.setText("Exit")
    win.getMouse()
    win.close()

# Charging a $30 overdraft fee each time the user views an account with a negative balance (FNC)
def overdraft(acctxt,accnum):
    infile = open(acctxt, "r")
    transactionList = infile.readlines(); infile.close() # (LOOD), (IFL)
    outfile = open(acctxt, "w")
    if len(transactionList) > 1:
        print(transactionList[0], end="", file=outfile) # (OFL)
    else:
        print(transactionList[0], file=outfile) # (OFL)
    print("overdraftfee",str(accnum),"-30","charge", file=outfile) # (OFL)
    for i in range(1, int(len(transactionList))):
        print(transactionList[i], end="", file=outfile) # (OFL)
    outfile.close()

# Recording a charge on the account that is sending a transfer of money (FNC)
def charge(acctxt, accnum, balance):
    infile=open(acctxt,"r")
    transactionList = infile.readlines(); infile.close() # (LOOD), (IFL)
    outfile = open(acctxt,"w")
    if len(transactionList) > 1:
        print(transactionList[0], end="", file=outfile) # (OFL)
    else:
        print(transactionList[0], file=outfile) # (OFL)
    print("acc"+str(accnum)+"transfer",accnum,"-"+balance,"transfer",file=outfile) # (OFL)
    for i in range(1, int(len(transactionList))):
        print(transactionList[i], end="", file=outfile); outfile.close() # (OFL)

# Displaying a prompt asking how much $ should be transferred from one account to the other, redirects to charge() after value
# is entered (FNC)
def transferMoney():
    aRectangle = Rectangle(Point(-10, 3), Point(10, -3)); aRectangle.setFill("black"); aRectangle.draw(win)

    if interface == "checking1":
        outPrompt = Text(Point(-2, 0), "Enter Amount to Transfer to Checking #2:")
    else:
        outPrompt = Text(Point(-2, 0), "Enter Amount to Transfer to Checking #1:")
    outPrompt.setFill("white"); outPrompt.draw(win)
    outBox = Entry(Point(4, 0), 6); outBox.draw(win) # (OTXT)

    submitButton = Rectangle(Point(-3, -5), Point(3, -6))
    submitButton.setFill("red")
    submitButtonText = Text(Point(0, -5.5), "Submit")
    submitButton.draw(win)
    submitButtonText.draw(win)
    win.getMouse()

    if saveFileExists == True:
        if interface=="checking1" and contentData[3]!="None":
            infile=open(contentData[3],"r")
            transactionList2 = infile.readlines(); infile.close() # (LOOD), (IFL)
            outfile=open(contentData[3],"w")
            if len(transactionList2) > 1:
                print(transactionList2[0], end="", file=outfile) # (OFL)
            else:
                print(transactionList2[0], file=outfile) # (OFL)
            print("acc1transfer",2,outBox.getText(),"transfer", file=outfile) # (IEB)
            for i in range(1,int(len(transactionList2))):
                print(transactionList2[i], end="", file=outfile) # (OFL)
            outfile.close()
            charge(contentData[2],1,outBox.getText()); aPrompt = Text(Point(0, -9), "Transfer complete!"); aPrompt.draw(win)
        elif interface=="checking1" and contentData[3]=="None":
            aError = Text(Point(0, -9), "Error: Please update transaction file for Checking #2"); aError.draw(win)
        elif interface=="checking2" and contentData[2]!="None":
            infile = open(contentData[2],"r")
            transactionList1 = infile.readlines(); infile.close() # (LOOD), (IFL)
            outfile = open(contentData[2],"w")
            if len(transactionList1) > 1:
                print(transactionList1[0], end="", file=outfile) # (OFL)
            else:
                print(transactionList1[0], file=outfile)
            print("acc2transfer",1,outBox.getText(),"transfer", file=outfile) # (IEB), (OFL)
            for i in range(1,int(len(transactionList1))):
                print(transactionList1[i], end="", file=outfile) # (OFL)
            outfile.close()
            charge(contentData[3], 2, outBox.getText()); aPrompt = Text(Point(0, -9), "Transfer complete!"); aPrompt.draw(win)
        elif interface=="checking2" and contentData[2]=="None":
            aError=Text(Point(0,-9), "Error: Please update transaction file for Checking #1"); aError.draw(win)
    else:
        aError = Text(Point(0, -9), "Error: Please update transaction files"); aError.draw(win)

    submitButtonText.setText("Exit")
    win.getMouse()
    win.close()

# Displaying a prompt asking for a text file name to print a copy of the imported file with record of transactions for the account (FNC)
def printStatment():
    aRectangle = Rectangle(Point(-10, 3), Point(10, -3))
    aRectangle.setFill("black")
    aRectangle.draw(win)

    outPrompt = Text(Point(-1, 0), "Name output file:")
    outPrompt.setFill("white")
    outPrompt.draw(win)
    outBox = Entry(Point(2, 0), 5) # (OTXT)
    outBox.draw(win)

    submitButton = Rectangle(Point(-3, -5), Point(3, -6))
    submitButton.setFill("red")
    submitButtonText = Text(Point(0, -5.5), "Submit")
    submitButton.draw(win)
    submitButtonText.draw(win)

    win.getMouse()

    if saveFileExists==True:
        if interface=="checking1" and contentData[2]!="None":
            infile = open(contentData[2], "r")
            transactionList1 = infile.readlines(); infile.close() # (LOOD), (IFL)
            outfile = open(outBox.getText(), "w") # (IEB)
            for i in range(int(len(transactionList1))):
                print(transactionList1[i], end="", file=outfile) # (OFL)
            outfile.close(); aPrompt = Text(Point(0, -9), "Statement Printed!"); aPrompt.draw(win)
        elif interface=="checking1" and contentData[2]=="None":
            aError = Text(Point(0, -9), "Error: Please update transaction file for Checking #1"); aError.draw(win)
        elif interface=="checking2" and contentData[3]!="None":
            infile = open(contentData[3], "r")
            transactionList2 = infile.readlines(); infile.close() # (LOOD), (IFL)
            outfile = open(outBox.getText(), "w") # (IEB)
            for i in range(int(len(transactionList2))):
                print(transactionList2[i], end="", file=outfile) # (OFL)
            outfile.close(); aPrompt = Text(Point(0, -9), "Statement Printed!"); aPrompt.draw(win)
        elif interface=="checking2" and contentData[3]=="None":
            aError = Text(Point(0, -9), "Error: Please update transaction file for Checking #2"); aError.draw(win)
    else:
        aError = Text(Point(0, -9), "Error: Please update transaction files"); aError.draw(win)

    submitButtonText.setText("Exit")
    win.getMouse()
    win.close()


if __name__=='__main__':
    saveFileExists=path.exists("savefile.txt")
    win=setUpWindow() # (GW)
    greeting,color,password=random()
    if saveFileExists == True:
        infile=open("savefile.txt","r")
        contentList = infile.readlines() # (LOOD)
        contentData = contentList[0].split()
        p, interface = intro(greeting, color, "")
        login(contentData[0])
    else:
        p, interface = intro(greeting, color, password)
        login(p)
    win.getMouse()
    win.close()