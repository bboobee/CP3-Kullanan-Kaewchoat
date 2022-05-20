usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "Test" and passwordInput == "1234":
    print ("Login Suucess!!")
    print("------WELCOME To TH SHOP------")
    print("1.Pen")
    print("2.Pencil")
    print("3.Rubber")
    print("4.Ruler")
    print("5.Paper")
    print("Select No.1-5 that you want to buy")
    userSelected = int(input("Selected No: "))
    if userSelected == 1:
        print("Pen   15 THB/Piece")
        numberPen = int(input("How many do you want?? :"))
        pricePen = numberPen*15
        print("Total = ", pricePen,"THB")
    elif userSelected == 2:
        print("Pencil   10 THB/Piece")
        numberPencil = int(input("How many do you want?? :"))
        pricePencil = numberPencil*10
        print("Total = ", pricePencil,"THB")
    elif userSelected == 3:
        print("Rubber   5 THB/Piece")
        numberRubber = int(input("How many do you want?? :"))
        priceRubber = numberRubber*5
        print("Total = ", priceRubber,"THB")
    elif userSelected == 4:
        print("Ruler   8 THB/Piece")
        numberRuler = int(input("How many do you want?? :"))
        priceRuler = numberRuler * 8
        print("Total = ", priceRuler, "THB")
    elif userSelected == 5:
        print("Paper   30 THB/Piece")
        numberPaper = int(input("How many do you want?? :"))
        pricePaper = numberPaper*30
        print("Total = ", pricePaper,"THB")
    print("-----------Thank you-------------")
else:
    print("You're FAIL!!")