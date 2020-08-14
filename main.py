from tkinter import Tk, messagebox, Label, Entry, Button, PhotoImage, Frame, LabelFrame
import functions, datetime

#GUI components
window = Tk()
window.geometry("1366x768+0+0")
window.title("Pizza Shop Management System")
window.configure(bg="Light Steel Blue")
window.resizable(0, 0)
window.iconphoto(False, PhotoImage(file="images/vegExtravaganza.png"))

#Images
#Pizza Images
vegExtravgImage = PhotoImage(file="images/vegExtravaganza.png")

freshVeggieImg = PhotoImage(file="images/freshVeggie.png")

deluxeVeggieImg = PhotoImage(file="images/deluxeVeggie.png")

nonVegSupremeImg = PhotoImage(file="images/nonVegSupreme.png")

pepperBbqImg = PhotoImage(file="images/pepperBbqCh.png")

chickenFiestaImg = PhotoImage(file="images/chickenFiesta.png")

#Beverages & Dessert Images
mirindaImg = PhotoImage(file="images/mirinda.png")

pepsiImg = PhotoImage(file="images/pepsi.png")

sevenUpImg = PhotoImage(file="images/7up.png")

chocLavaCakeImg = PhotoImage(file="images/chocLavaCake.png")

chocoBrownieImg = PhotoImage(file="images/chocoBrownie.png")

miniChocSundaeImg = PhotoImage(file="images/miniChocSundae.png")

resetImg = PhotoImage(file="images/reset.png")

#Frames
titleFrame = Frame(window, relief="sunken", bd=4, bg="khaki1")
titleFrame.place(x=15, y=15, width=1335, height=80)

titleLabel = Label(titleFrame, text="PIZZA SHOP", fg="Navy Blue", bg="khaki1", font=('Verdana', 36, 'bold'), pady=20)
titleLabel.pack()

userNameLabel = Label(titleFrame, text="Username: ", fg="Black", bg="khaki1", font=('Verdana', 14, 'bold'))
userNameLabel.place(x=5, y=5)

entUserName = Entry(titleFrame, font=('Verdana', 14, 'bold'))
entUserName.place(x=125, y=5, width=250)

mobileNumberLabel = Label(titleFrame, text="Mobile No.: ", font=('Verdana', 14, 'bold'), fg="Black", bg="khaki1")
mobileNumberLabel.place(x=5, y=35)

entMobileNumber = Entry(titleFrame, font=('Verdana', 14, 'bold'))
entMobileNumber.place(x=130, y=35, width=250)

dateLabel = Label(titleFrame, fg="Navy Blue", bg="khaki1", font=('Verdana', 15, 'bold'), padx=4, text=datetime.date.today().strftime("Date: %d-%m-%Y"))
dateLabel.place(x=1100, y=5)

timeLabel = Label(titleFrame, fg="Navy Blue", bg="khaki1", font=('Verdana', 15, 'bold'), padx=4)
timeLabel.place(x=1090, y=35)

functions.clock(window, timeLabel)

dataFrameLeft = LabelFrame(window, relief="sunken", bd=4, text='Pizza Menu (Single 10" size):', bg="khaki1", font=('Verdana', 14, 'bold'))
dataFrameLeft.place(x=15, y=105, width=670, height=500)

dataFrameRight = LabelFrame(window, relief="sunken", bd=4, text="Beverage(s) / Dessert(s):", bg="khaki1", font=('Verdana', 14, 'bold'))
dataFrameRight.place(x=700, y=105, width=650, height=500)

dataFrameBottom = Frame(window, relief="sunken", bd=4, bg="khaki1")
dataFrameBottom.place(x=15, y=620, width=1335, height=130)

#Labels and Buttons
#Pizza Labels and Buttons
#Veg. Extravaganza Pizza
lblVegExtravg = Label(dataFrameLeft, text="Veg. Extravaganza Pizza", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblVegExtravg.place(x=15, y=5)

lblVegExtravg = Label(dataFrameLeft, text="\u20B9 550 each", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblVegExtravg.place(x=130, y=40)

btnVegExtravg = Button(dataFrameLeft, bd=4, relief="raised", image=vegExtravgImage)
btnVegExtravg.place(x=15, y=40, width=100, height=100)

btnVegExtravgNos = Button(dataFrameLeft, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", activebackground="white", activeforeground="green", bd=4, relief="groove", text="0")
btnVegExtravgNos.place(x=130, y=90, width=50, height=50)

btnResetVegExtravgNos = Button(dataFrameLeft, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", activebackground="white", activeforeground="green", bd=4, relief="groove", image=resetImg)
btnResetVegExtravgNos.place(x=190, y=90, width=50, height=50)

#Fresh Veggie Pizza
lblFreshVeggie = Label(dataFrameLeft,  text="Fresh Veggie Pizza", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblFreshVeggie.place(x=15, y=160)

lblFreshVeggieRate = Label(dataFrameLeft,  text="\u20B9 480 each", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblFreshVeggieRate.place(x=130, y=195)

btnFreshVeggie = Button(dataFrameLeft, bd=4, relief="raised", image=freshVeggieImg)
btnFreshVeggie.place(x=15, y=195, width=100, height=100)

btnFreshVeggieNos = Button(dataFrameLeft, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", bd=4, relief="groove", text="0", activeforeground="green", activebackground="white") #command=decFreshVeggieNos)
btnFreshVeggieNos.place(x=130, y=245, width=50, height=50)

btnResetFreshVeggieNos = Button(dataFrameLeft, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", activebackground="white", activeforeground="green", bd=4, relief="groove", image=resetImg) #command=btnResetFreshVeggieNos)
btnResetFreshVeggieNos.place(x=190, y=245, width=50, height=50)

#Deluxe Veggie Pizza
btnDeluxeVeggie = Label(dataFrameLeft,  text="Deluxe Veggie Pizza", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
btnDeluxeVeggie.place(x=15, y=310)

lblDeluxeVeggieRate = Label(dataFrameLeft,  text="\u20B9 600 each", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblDeluxeVeggieRate.place(x=130, y=350)

btnDeluxeVeggie = Button(dataFrameLeft, bd=4, relief="raised", image=deluxeVeggieImg)
btnDeluxeVeggie.place(x=15, y=350, width=100, height=100)

btnDeluxeVeggieNos = Button(dataFrameLeft, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", bd=4, relief="groove", text="0", activeforeground="green", activebackground="white")
btnDeluxeVeggieNos.place(x=130, y=400, width=50, height=50)

btnResetDeluxeVeggieNos = Button(dataFrameLeft, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", activebackground="white", activeforeground="green", bd=4, relief="groove", image=resetImg)
btnResetDeluxeVeggieNos.place(x=190, y=400, width=50, height=50)

#Non Veg. Supreme Pizza
lblNonVegSupreme = Label(dataFrameLeft,  text="Non Veg. Supreme Pizza", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblNonVegSupreme.place(x=300, y=5)

lblNonVegSupremeRate = Label(dataFrameLeft,  text="\u20B9 680 each", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblNonVegSupremeRate.place(x=420, y=40)

btnNonVegSupreme = Button(dataFrameLeft, bd=4, relief="raised", image=nonVegSupremeImg)
btnNonVegSupreme.place(x=300, y=40, width=100, height=100)

btnNonVegSupremeNos = Button(dataFrameLeft, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", bd=4, relief="groove", text="0", activeforeground="green", activebackground="white")
btnNonVegSupremeNos.place(x=420, y=90, width=50, height=50)

btnResetNonVegSupremeNos = Button(dataFrameLeft, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", activebackground="white", activeforeground="green", bd=4, relief="groove", image=resetImg)
btnResetNonVegSupremeNos.place(x=480, y=90, width=50, height=50)

#Pepper BBQ Chicken Pizza
lblPepperBbq = Label(dataFrameLeft,  text="Pepper Barbeque Chicken Pizza", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblPepperBbq.place(x=300, y=160)

lblPepperBbqRate = Label(dataFrameLeft,  text="\u20B9 580 each", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblPepperBbqRate.place(x=420, y=195)

btnPepperBbq = Button(dataFrameLeft, bd=4, relief="raised", image=pepperBbqImg)
btnPepperBbq.place(x=300, y=195, width=100, height=100)

btnPepperBbqNos = Button(dataFrameLeft, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", bd=4, relief="groove", text="0", activeforeground="green", activebackground="white")
btnPepperBbqNos.place(x=420, y=245, width=50, height=50)

btnResetPepperBbqNos = Button(dataFrameLeft, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", activebackground="white", activeforeground="green", bd=4, relief="groove", image=resetImg)
btnResetPepperBbqNos.place(x=480, y=245, width=50, height=50)

#Chicken Fiesta Pizza
lblChickenFiesta = Label(dataFrameLeft,  text="Chicken Fiesta Pizza", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblChickenFiesta.place(x=300, y=310)

lblChickenFiestaRate = Label(dataFrameLeft,  text="\u20B9 700 each", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblChickenFiestaRate.place(x=420, y=350)

btnChickenFiesta = Button(dataFrameLeft, bd=4, relief="raised", image=chickenFiestaImg)
btnChickenFiesta.place(x=300, y=350, width=100, height=100)

btnChickenFiestaNos = Button(dataFrameLeft, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", bd=4, relief="groove", text="0", activeforeground="green", activebackground="white")
btnChickenFiestaNos.place(x=420, y=400, width=50, height=50)

btnResetChickenFiestaNos = Button(dataFrameLeft, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", activebackground="white", activeforeground="green", bd=4, relief="groove", image=resetImg)
btnResetChickenFiestaNos.place(x=480, y=400, width=50, height=50)

#Beverages & Desserts Labels and Buttons
#Mirinda
lblMirinda = Label(dataFrameRight, text="Mirinda (500 ml)", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblMirinda.place(x=15, y=5)

lblMirindaRate = Label(dataFrameRight, text="\u20B9 40 each", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblMirindaRate.place(x=130, y=40)

btnMirinda = Button(dataFrameRight, bd=4, relief="raised", image=mirindaImg)
btnMirinda.place(x=15, y=40, width=100, height=100)

btnMirindaNos = Button(dataFrameRight, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", activebackground="white", activeforeground="green", bd=4, relief="groove", text="0")
btnMirindaNos.place(x=130, y=90, width=50, height=50)

btnResetMirindaNos = Button(dataFrameRight, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", activebackground="white", activeforeground="green", bd=4, relief="groove", image=resetImg)
btnResetMirindaNos.place(x=190, y=90, width=50, height=50)

#Pepsi
lblPepsi = Label(dataFrameRight,  text="Pepsi (500 ml)", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblPepsi.place(x=15, y=160)

lblPepsiRate = Label(dataFrameRight,  text="\u20B9 35 each", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblPepsiRate.place(x=130, y=195)

btnPepsiButton = Button(dataFrameRight, bd=4, relief="raised", image=pepsiImg)
btnPepsiButton.place(x=15, y=195, width=100, height=100)

btnPepsiNos = Button(dataFrameRight, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", bd=4, relief="groove", text="0", activeforeground="green", activebackground="white")
btnPepsiNos.place(x=130, y=245, width=50, height=50)

btnResetPepsiNos = Button(dataFrameRight, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", activebackground="white", activeforeground="green", bd=4, relief="groove", image=resetImg)
btnResetPepsiNos.place(x=190, y=245, width=50, height=50)

#7UP
lblSevenUp = Label(dataFrameRight,  text="7UP (500 ml)", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblSevenUp.place(x=15, y=310)

lblSevenUpRate = Label(dataFrameRight,  text="\u20B9 38 each", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblSevenUpRate.place(x=130, y=350)

btnSevenUp = Button(dataFrameRight, bd=4, relief="raised", image=sevenUpImg)
btnSevenUp.place(x=15, y=350, width=100, height=100)

btnSevenUpNos = Button(dataFrameRight, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", bd=4, relief="groove", text="0", activeforeground="green", activebackground="white")
btnSevenUpNos.place(x=130, y=400, width=50, height=50)

btnResetSevenUpNos = Button(dataFrameRight, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", activebackground="white", activeforeground="green", bd=4, relief="groove", image=resetImg)
btnResetSevenUpNos.place(x=190, y=400, width=50, height=50)

#Chocolate Lava Cake
lblChocLavaCake = Label(dataFrameRight,  text="Chocolate Lava Cake", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblChocLavaCake.place(x=300, y=5)

lblChocLavaCakeRate = Label(dataFrameRight,  text="\u20B9 50 each", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblChocLavaCakeRate.place(x=420, y=40)

btnChocLavaCake = Button(dataFrameRight, bd=4, relief="raised", image=chocLavaCakeImg, bg="White")
btnChocLavaCake.place(x=300, y=40, width=100, height=100)

btnChocLavaCakeNos = Button(dataFrameRight, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", bd=4, relief="groove", text="0", activeforeground="green", activebackground="white")
btnChocLavaCakeNos.place(x=420, y=90, width=50, height=50)

btnResetChocLavaCakeNos = Button(dataFrameRight, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", activebackground="white", activeforeground="green", bd=4, relief="groove", image=resetImg)
btnResetChocLavaCakeNos.place(x=480, y=90, width=50, height=50)

#Chocolate Brownie
lblChocoBrownie = Label(dataFrameRight,  text="Chocolate Brownie", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblChocoBrownie.place(x=300, y=160)

lblChocoBrownieRate = Label(dataFrameRight,  text="\u20B9 45 each", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblChocoBrownieRate.place(x=420, y=195)

btnChocoBrownie = Button(dataFrameRight, bd=4, relief="raised", image=chocoBrownieImg, bg="White")
btnChocoBrownie.place(x=300, y=195, width=100, height=100)

btnChocoBrownieNos = Button(dataFrameRight, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", bd=4, relief="groove", text="0", activeforeground="green", activebackground="white")
btnChocoBrownieNos.place(x=420, y=245, width=50, height=50)

btnResetChocoBrownieNos = Button(dataFrameRight, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", activebackground="white", activeforeground="green", bd=4, relief="groove", image=resetImg)
btnResetChocoBrownieNos.place(x=480, y=245, width=50, height=50)

#Mini Chocolate Sundae
lblMiniChocSundae = Label(dataFrameRight,  text="Mini Chocolate Sundae", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblMiniChocSundae.place(x=300, y=310)

lblMiniChocSundaeRate = Label(dataFrameRight,  text="\u20B9 60 each", font=('Verdana', 14), bg="Salmon", fg="Black", padx=5, relief="raised", bd=2)
lblMiniChocSundaeRate.place(x=420, y=350)

btnMiniChocSundae = Button(dataFrameRight, bd=4, relief="raised", image=miniChocSundaeImg, bg="White")
btnMiniChocSundae.place(x=300, y=350, width=100, height=100)

btnMiniChocSundaeNos = Button(dataFrameRight, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", bd=4, relief="groove", text="0", activeforeground="green", activebackground="white")
btnMiniChocSundaeNos.place(x=420, y=400, width=50, height=50)

btnResetMiniChocSundaeNos = Button(dataFrameRight, font=('Verdana', 14, 'bold'), justify="center", fg="green", bg="white", activebackground="white", activeforeground="green", bd=4, relief="groove", image=resetImg)
btnResetMiniChocSundaeNos.place(x=480, y=400, width=50, height=50)

#Data Frame Bottom
btnResetAll = Button(dataFrameBottom, bg="teal", fg="white", activebackground="green", activeforeground="white", text="Reset All", font=('Verdana', 14, 'bold'), bd=4, relief="groove", command=lambda:functions.resetAllNos(btnVegExtravgNos, btnFreshVeggieNos, btnDeluxeVeggieNos, btnNonVegSupremeNos, btnPepperBbqNos, btnMirindaNos, btnPepsiNos, btnSevenUpNos, btnChocLavaCakeNos, btnChocoBrownieNos, btnMiniChocSundaeNos, lblCalculateTotal, btnChickenFiestaNos))
btnResetAll.place(x=150, y=10, width=300, height=100)

btnCalculateTotal = Button(dataFrameBottom, bg="teal", fg="white", activebackground="green", activeforeground="white", text="Calculate Total & Generate Bill", font=('Verdana', 14, 'bold'), bd=4, relief="groove")
btnCalculateTotal.place(x=500, y=10, width=350, height=100)

lblRupeeSymbol = Label(dataFrameBottom, font=('Verdana', 20, 'bold'), padx=10, pady=10, text="\u20B9 ", bg="white", fg="black")
lblRupeeSymbol.place(x=880, y=10)

lblCalculateTotal = Label(dataFrameBottom, font=('Verdana', 20, 'bold'), padx=10, pady=10, text="0", bg="white", fg="black")
lblCalculateTotal.place(x=930, y=10, width=300)

btnCalculateTotal.configure(command=lambda:functions.totalBill(btnVegExtravgNos, btnFreshVeggieNos, btnDeluxeVeggieNos, btnNonVegSupremeNos, btnPepperBbqNos, btnChickenFiestaNos, btnMirindaNos, btnPepsiNos, btnSevenUpNos, btnChocLavaCakeNos, btnChocoBrownieNos, btnMiniChocSundaeNos, lblCalculateTotal, entUserName, entMobileNumber, window))

#Assigning functions to buttons
#Veg. Extravaganza Pizza
btnVegExtravg.configure(command=lambda:functions.incVegExtravgNos(btnVegExtravgNos))

btnVegExtravgNos.configure(command=lambda:functions.decVegExtravgNos(btnVegExtravgNos))

btnResetVegExtravgNos.configure(command=lambda:functions.resetVegExtravgNos(btnVegExtravgNos))

#Fresh Veggie Pizza
btnFreshVeggie.configure(command=lambda:functions.incFreshVeggieNos(btnFreshVeggieNos))

btnFreshVeggieNos.configure(command=lambda:functions.decFreshVeggieNos(btnFreshVeggieNos))

btnResetFreshVeggieNos.configure(command=lambda:functions.resetFreshVeggieNos(btnFreshVeggieNos))

#Deluxe Veggie Pizza
btnDeluxeVeggie.configure(command=lambda:functions.incDeluxeVeggieNos(btnDeluxeVeggieNos))

btnDeluxeVeggieNos.configure(command=lambda:functions.decDeluxeVeggieNos(btnDeluxeVeggieNos))

btnResetDeluxeVeggieNos.configure(command=lambda:functions.resetDeluxeVeggieNos(btnDeluxeVeggieNos))

#Non Veg. Supreme Pizza
btnNonVegSupreme.configure(command=lambda:functions.incNonVegSupremeNos(btnNonVegSupremeNos))

btnNonVegSupremeNos.configure(command=lambda:functions.decNonVegSupremeNos(btnNonVegSupremeNos))

btnResetNonVegSupremeNos.configure(command=lambda:functions.resetNonVegSupremeNos(btnNonVegSupremeNos))

#Pepper Barbeque Chicken Pizza
btnPepperBbq.configure(command=lambda:functions.incPepperBbqNos(btnPepperBbqNos))

btnPepperBbqNos.configure(command=lambda:functions.decPepperBbqNos(btnPepperBbqNos))

btnResetPepperBbqNos.configure(command=lambda:functions.resetPepperBbqNos(btnPepperBbqNos))

#Chicken Fiesta Pizza
btnChickenFiesta.configure(command=lambda:functions.incChickenFiestaNos(btnChickenFiestaNos))

btnChickenFiestaNos.configure(command=lambda:functions.decChickenFiestaNos(btnChickenFiestaNos))

btnResetChickenFiestaNos.configure(command=lambda:functions.resetChickenFiestaNos(btnChickenFiestaNos))

#Mirinda
btnMirinda.configure(command=lambda:functions.incMirindaNos(btnMirindaNos))

btnMirindaNos.configure(command=lambda:functions.decMirindaNos(btnMirindaNos))

btnResetMirindaNos.configure(command=lambda:functions.resetMirindaNos(btnMirindaNos))

#Pepsi
btnPepsiButton.configure(command=lambda:functions.incPepsiNos(btnPepsiNos))

btnPepsiNos.configure(command=lambda:functions.decPepsiNos(btnPepsiNos))

btnResetPepsiNos.configure(command=lambda:functions.resetPepsiNos(btnPepsiNos))

#7UP
btnSevenUp.configure(command=lambda:functions.incSevenUpNos(btnSevenUpNos))

btnSevenUpNos.configure(command=lambda:functions.decSevenUpNos(btnSevenUpNos))

btnResetSevenUpNos.configure(command=lambda:functions.resetSevenUpNos(btnSevenUpNos))

#Chocolate Lava Cake
btnChocLavaCake.configure(command=lambda:functions.incChocLavaCakeNos(btnChocLavaCakeNos))

btnChocLavaCakeNos.configure(command=lambda:functions.decChocLavaCakeNos(btnChocLavaCakeNos))

btnResetChocLavaCakeNos.configure(command=lambda:functions.resetChocLavaCakeNos(btnChocLavaCakeNos))

#Chocolate Brownie
btnChocoBrownie.configure(command=lambda:functions.incChocoBrownieNos(btnChocoBrownieNos))

btnChocoBrownieNos.configure(command=lambda:functions.decChocoBrownieNos(btnChocoBrownieNos))

btnResetChocoBrownieNos.configure(command=lambda:functions.resetChocoBrownieNos(btnChocoBrownieNos))

#Mini Chocolate Sundae
btnMiniChocSundae.configure(command=lambda:functions.incMiniChocSundaeNos(btnMiniChocSundaeNos))

btnMiniChocSundaeNos.configure(command=lambda:functions.decMiniChocSundaeNos(btnMiniChocSundaeNos))

btnResetMiniChocSundaeNos.configure(command=lambda:functions.resetMiniChocSundaeNos(btnMiniChocSundaeNos))

window.mainloop()