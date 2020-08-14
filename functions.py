from tkinter import messagebox, Toplevel, Text, Button
import datetime, mysql.connector

def clock(window, timeLabel):
    time = datetime.datetime.now().strftime("Time: %I:%M:%S %p")
    timeLabel.configure(text=time)
    def clockRecursiveCall():
        clock(window, timeLabel)
    window.after(1000, clockRecursiveCall)

#Reset all quantities
def resetAllNos(btnVegExtravgNos, btnFreshVeggieNos, btnDeluxeVeggieNos, btnNonVegSupremeNos, btnPepperBbqNos, btnChickenFiestaNos, btnMirindaNos, btnPepsiNos, btnSevenUpNos, btnChocLavaCakeNos, btnChocoBrownieNos, btnMiniChocSundaeNos, lblCalculateTotal):
    btnVegExtravgNos.configure(text="0")
    btnFreshVeggieNos.configure(text="0")
    btnDeluxeVeggieNos.configure(text="0")
    btnNonVegSupremeNos.configure(text="0")
    btnPepperBbqNos.configure(text="0")
    btnChickenFiestaNos.configure(text="0")
    btnMirindaNos.configure(text="0")
    btnPepsiNos.configure(text="0")
    btnSevenUpNos.configure(text="0")
    btnChocLavaCakeNos.configure(text="0")
    btnChocoBrownieNos.configure(text="0")
    btnMiniChocSundaeNos.configure(text="0")
    lblCalculateTotal.configure(text="0")

#Pizza Functions
#Veg. Extravaganza Pizza functions
def vegExtravg(btnVegExtravgNos):
    vegExtravgNos = int(btnVegExtravgNos.cget("text"))
    return vegExtravgNos

def incVegExtravgNos(btnVegExtravgNos):
    vegExtravgNos = vegExtravg(btnVegExtravgNos)
    if(vegExtravgNos < 20):
        vegExtravgNos = vegExtravgNos + 1
        btnVegExtravgNos.configure(text=vegExtravgNos)

def decVegExtravgNos(btnVegExtravgNos):
    vegExtravgNos = vegExtravg(btnVegExtravgNos)
    if(vegExtravgNos > 0):
        vegExtravgNos = vegExtravgNos - 1
        btnVegExtravgNos.configure(text=vegExtravgNos)

def resetVegExtravgNos(btnVegExtravgNos):
    btnVegExtravgNos.configure(text="0")

#Fresh Veggie Pizza functions
def freshVeggie(btnFreshVeggieNos):
    freshVeggieNos = int(btnFreshVeggieNos.cget("text"))
    return freshVeggieNos

def incFreshVeggieNos(btnFreshVeggieNos):
    freshVeggieNos = freshVeggie(btnFreshVeggieNos)
    if(freshVeggieNos < 20):
        freshVeggieNos = freshVeggieNos + 1
        btnFreshVeggieNos.configure(text=freshVeggieNos)

def decFreshVeggieNos(btnFreshVeggieNos):
    freshVeggieNos = freshVeggie(btnFreshVeggieNos)
    if(freshVeggieNos > 0):
        freshVeggieNos = freshVeggieNos - 1
        btnFreshVeggieNos.configure(text=freshVeggieNos)

def resetFreshVeggieNos(btnFreshVeggieNos):
    btnFreshVeggieNos.configure(text="0")

#Deluxe Veggie Pizza
def deluxeVeggie(btnDeluxeVeggieNos):
    deluxeVeggieNos = int(btnDeluxeVeggieNos.cget("text"))
    return deluxeVeggieNos

def incDeluxeVeggieNos(btnDeluxeVeggieNos):
    deluxeVeggieNos = deluxeVeggie(btnDeluxeVeggieNos)
    if(deluxeVeggieNos < 20):
        deluxeVeggieNos = deluxeVeggieNos + 1
        btnDeluxeVeggieNos.configure(text=deluxeVeggieNos)

def decDeluxeVeggieNos(btnDeluxeVeggieNos):
    deluxeVeggieNos = deluxeVeggie(btnDeluxeVeggieNos)
    if(deluxeVeggieNos > 0):
        deluxeVeggieNos = deluxeVeggieNos - 1
        btnDeluxeVeggieNos.configure(text=deluxeVeggieNos)

def resetDeluxeVeggieNos(btnDeluxeVeggieNos):
    btnDeluxeVeggieNos.configure(text="0")

#Non Veg. Supreme Pizza
def nonVegSupreme(btnNonVegSupremeNos):
    nonVegSupremeNos = int(btnNonVegSupremeNos.cget("text"))
    return nonVegSupremeNos

def incNonVegSupremeNos(btnNonVegSupremeNos):
    nonVegSupremeNos = nonVegSupreme(btnNonVegSupremeNos)
    if(nonVegSupremeNos < 20):
        nonVegSupremeNos = nonVegSupremeNos + 1
        btnNonVegSupremeNos.configure(text=nonVegSupremeNos)

def decNonVegSupremeNos(btnNonVegSupremeNos):
    nonVegSupremeNos = nonVegSupreme(btnNonVegSupremeNos)
    if(nonVegSupremeNos > 0):
        nonVegSupremeNos = nonVegSupremeNos - 1
        btnNonVegSupremeNos.configure(text=nonVegSupremeNos)

def resetNonVegSupremeNos(btnNonVegSupremeNos):
    btnNonVegSupremeNos.configure(text="0")

#Pepper BBQ Chicken Pizza
def pepperBbq(btnPepperBbqNos):
    pepperBbqNos = int(btnPepperBbqNos.cget("text"))
    return pepperBbqNos

def incPepperBbqNos(btnPepperBbqNos):
    pepperBbqNos = pepperBbq(btnPepperBbqNos)
    if(pepperBbqNos < 20):
        pepperBbqNos = pepperBbqNos + 1
        btnPepperBbqNos.configure(text=pepperBbqNos)

def decPepperBbqNos(btnPepperBbqNos):
    pepperBbqNos = pepperBbq(btnPepperBbqNos)
    if(pepperBbqNos > 0):
        pepperBbqNos = pepperBbqNos - 1
        btnPepperBbqNos.configure(text=pepperBbqNos)

def resetPepperBbqNos(btnPepperBbqNos):
    btnPepperBbqNos.configure(text="0")

#Chicken Fiesta Pizza
def chickenFiesta(btnChickenFiestaNos):
    chickenFiestaNos = int(btnChickenFiestaNos.cget("text"))
    return chickenFiestaNos

def incChickenFiestaNos(btnChickenFiestaNos):
    chickenFiestaNos = chickenFiesta(btnChickenFiestaNos)
    if(chickenFiestaNos < 20):
        chickenFiestaNos = chickenFiestaNos + 1
        btnChickenFiestaNos.configure(text=chickenFiestaNos)

def decChickenFiestaNos(btnChickenFiestaNos):
    chickenFiestaNos = chickenFiesta(btnChickenFiestaNos)
    if(chickenFiestaNos > 0):
        chickenFiestaNos = chickenFiestaNos - 1
        btnChickenFiestaNos.configure(text=chickenFiestaNos)

def resetChickenFiestaNos(btnChickenFiestaNos):
    btnChickenFiestaNos.configure(text="0")

#Beverages & Dessert functions
#Mirinda
def mirinda(btnMirindaNos):
    mirindaNos = int(btnMirindaNos.cget("text"))
    return mirindaNos

def incMirindaNos(btnMirindaNos):
    mirindaNos = mirinda(btnMirindaNos)
    if(mirindaNos < 20):
        mirindaNos = mirindaNos + 1
        btnMirindaNos.configure(text=mirindaNos)

def decMirindaNos(btnMirindaNos):
    mirindaNos = mirinda(btnMirindaNos)
    if(mirindaNos > 0):
        mirindaNos = mirindaNos - 1
        btnMirindaNos.configure(text=mirindaNos)

def resetMirindaNos(btnMirindaNos):
    btnMirindaNos.configure(text="0")

#Pepsi
def pepsi(btnPepsiNos):
    pepsiNos = int(btnPepsiNos.cget("text"))
    return pepsiNos

def incPepsiNos(btnPepsiNos):
    pepsiNos = pepsi(btnPepsiNos)
    if(pepsiNos < 20):
        pepsiNos = pepsiNos + 1
        btnPepsiNos.configure(text=pepsiNos)

def decPepsiNos(btnPepsiNos):
    pepsiNos = pepsi(btnPepsiNos)
    if(pepsiNos > 0):
        pepsiNos = pepsiNos - 1
        btnPepsiNos.configure(text=pepsiNos)

def resetPepsiNos(btnPepsiNos):
    btnPepsiNos.configure(text="0")

#7UP
def sevenUp(btnSevenUpNos):
    sevenUpNos = int(btnSevenUpNos.cget("text"))
    return sevenUpNos

def incSevenUpNos(btnSevenUpNos):
    sevenUpNos = sevenUp(btnSevenUpNos)
    if(sevenUpNos < 20):
        sevenUpNos = sevenUpNos + 1
        btnSevenUpNos.configure(text=sevenUpNos)

def decSevenUpNos(btnSevenUpNos):
    sevenUpNos = sevenUp(btnSevenUpNos)
    if(sevenUpNos > 0):
        sevenUpNos = sevenUpNos - 1
        btnSevenUpNos.configure(text=sevenUpNos)

def resetSevenUpNos(btnSevenUpNos):
    btnSevenUpNos.configure(text="0")

#Chocolate Lava Cake
def chocLavaCake(btnChocLavaCakeNos):
    chocLavaCakeNos = int(btnChocLavaCakeNos.cget("text"))
    return chocLavaCakeNos

def incChocLavaCakeNos(btnChocLavaCakeNos):
    chocLavaCakeNos = chocLavaCake(btnChocLavaCakeNos)
    if(chocLavaCakeNos < 20):
        chocLavaCakeNos = chocLavaCakeNos + 1
        btnChocLavaCakeNos.configure(text=chocLavaCakeNos)

def decChocLavaCakeNos(btnChocLavaCakeNos):
    chocLavaCakeNos = chocLavaCake(btnChocLavaCakeNos)
    if(chocLavaCakeNos > 0):
        chocLavaCakeNos = chocLavaCakeNos - 1
        btnChocLavaCakeNos.configure(text=chocLavaCakeNos)

def resetChocLavaCakeNos(btnChocLavaCakeNos):
    btnChocLavaCakeNos.configure(text="0")

#Chocolate Brownie
def chocoBrownie(btnChocoBrownieNos):
    chocoBrownieNos = int(btnChocoBrownieNos.cget("text"))
    return chocoBrownieNos

def incChocoBrownieNos(btnChocoBrownieNos):
    chocoBrownieNos = chocoBrownie(btnChocoBrownieNos)
    if(chocoBrownieNos < 20):
        chocoBrownieNos = chocoBrownieNos + 1
        btnChocoBrownieNos.configure(text=chocoBrownieNos)

def decChocoBrownieNos(btnChocoBrownieNos):
    chocoBrownieNos = chocoBrownie(btnChocoBrownieNos)
    if(chocoBrownieNos > 0):
        chocoBrownieNos = chocoBrownieNos - 1
        btnChocoBrownieNos.configure(text=chocoBrownieNos)

def resetChocoBrownieNos(btnChocoBrownieNos):
    btnChocoBrownieNos.configure(text="0")

#Mini Chocolate Sundae
def miniChocSundae(btnMiniChocSundaeNos):
    miniChocSundaeNos = int(btnMiniChocSundaeNos.cget("text"))
    return miniChocSundaeNos

def incMiniChocSundaeNos(btnMiniChocSundaeNos):
    miniChocSundaeNos = miniChocSundae(btnMiniChocSundaeNos)
    if(miniChocSundaeNos < 20):
        miniChocSundaeNos = miniChocSundaeNos + 1
        btnMiniChocSundaeNos.configure(text=miniChocSundaeNos)

def decMiniChocSundaeNos(btnMiniChocSundaeNos):
    miniChocSundaeNos = miniChocSundae(btnMiniChocSundaeNos)
    if(miniChocSundaeNos > 0):
        miniChocSundaeNos = miniChocSundaeNos - 1
        btnMiniChocSundaeNos.configure(text=miniChocSundaeNos)

def resetMiniChocSundaeNos(btnMiniChocSundaeNos):
    btnMiniChocSundaeNos.configure(text="0")

def insertData(userNameData, mobileNumberData):
    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = ""
        )
        cur = conn.cursor()
        
        cur.execute("CREATE DATABASE IF NOT EXISTS pizza_orders")
        cur.execute("USE pizza_orders")
        cur.execute("CREATE TABLE IF NOT EXISTS order_details(id INT AUTO_INCREMENT PRIMARY KEY, username TEXT NOT NULL, mobile_number TEXT NOT NULL)")
        
        sql = "INSERT INTO order_details(username, mobile_number) VALUES(%s, %s)"
        val = (userNameData, mobileNumberData)
        cur.execute(sql, val)
        cur.execute("SELECT id FROM order_details WHERE username=%s AND mobile_number=%s", (userNameData, mobileNumberData))
        
        global receivedId
        receivedId = cur.fetchall()
        conn.commit()
    except mysql.connector.DatabaseError as de:
        conn.rollback()
        messagebox.showerror("Database Error", de)
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Error", e)
    finally:
        if (conn != None):
            conn.close()
    return receivedId[0][0]

def openNewWindow(totalCost, userNameData, mobileNumberData, window, btnVegExtravgNos, btnFreshVeggieNos, btnDeluxeVeggieNos, btnNonVegSupremeNos, btnPepperBbqNos, btnChickenFiestaNos, btnMirindaNos, btnPepsiNos, btnSevenUpNos, btnChocLavaCakeNos, btnChocoBrownieNos, btnMiniChocSundaeNos, lblCalculateTotal):
    if (totalCost !=0 or totalCost > 0):
        billWindow = Toplevel(window)
        billWindow.title("Bill")
        billWindow.geometry("550x500")
        billWindow.config(bg="Light Steel Blue")

        receivedId = str(insertData(userNameData, mobileNumberData))

        txtBill = Text(billWindow, state="disabled")
        txtBill.place(x=20, y=10, width=510, height=400)

        btnOk = Button(billWindow, text="OK", font=('Verdana', 15, 'bold'))
        btnOk.place(x=220, y=430, width=120)

        f = open("data/order.txt", "r+")

        txtBill.configure(state="normal")
        txtBill.insert('1.0', "\t\t\tPIZZA SHOP\n")
        dateToday = datetime.date.today().strftime("Date: %d-%m-%Y") + "\n"
        timeNow = datetime.datetime.now().strftime("Time: %I:%M:%S %p") + "\n"
        txtBill.insert('2.0', dateToday)
        txtBill.insert('3.0', timeNow)
        idString = "\nID: " + receivedId
        userNameString = "\nUsername: " + userNameData
        mobileNumberString = "\nMobile Number: " + mobileNumberData
        txtBill.insert('5.0', idString)
        txtBill.insert('6.0', userNameString)
        txtBill.insert('7.0', mobileNumberString)
        txtBill.insert('10.0', "\nContents\t\t\t\tQuantity\t\tPrice\n")
        txtBill.insert('13.0', f.read())
        txtBill.insert('24.0', "\t\t\t\t\nTotal Cost: Rs. ")
        txtBill.insert('24.0', totalCost)
        txtBill.insert('26.0', "\n\n\n\t\t\tTHANK YOU!")
        txtBill.configure(state="disabled")
        f.truncate(0)
        f.close()

        def closeWindow(btnVegExtravgNos, btnFreshVeggieNos, btnDeluxeVeggieNos, btnNonVegSupremeNos, btnPepperBbqNos, btnChickenFiestaNos, btnMirindaNos, btnPepsiNos, btnSevenUpNos, btnChocLavaCakeNos, btnChocoBrownieNos, btnMiniChocSundaeNos, lblCalculateTotal):
            resetAllNos(btnVegExtravgNos, btnFreshVeggieNos, btnDeluxeVeggieNos, btnNonVegSupremeNos, btnPepperBbqNos, btnChickenFiestaNos, btnMirindaNos, btnPepsiNos, btnSevenUpNos, btnChocLavaCakeNos, btnChocoBrownieNos, btnMiniChocSundaeNos, lblCalculateTotal)
            messagebox.showinfo("Done", "Order placed!")
            billWindow.destroy()

        btnOk.configure(command=lambda:closeWindow(btnVegExtravgNos, btnFreshVeggieNos, btnDeluxeVeggieNos, btnNonVegSupremeNos, btnPepperBbqNos, btnChickenFiestaNos, btnMirindaNos, btnPepsiNos, btnSevenUpNos, btnChocLavaCakeNos, btnChocoBrownieNos, btnMiniChocSundaeNos, lblCalculateTotal))
    else:
        messagebox.showerror("Error", "Empty order cannot be placed")

def totalBill(btnVegExtravgNos, btnFreshVeggieNos, btnDeluxeVeggieNos, btnNonVegSupremeNos, btnPepperBbqNos, btnChickenFiestaNos, btnMirindaNos, btnPepsiNos, btnSevenUpNos, btnChocLavaCakeNos, btnChocoBrownieNos, btnMiniChocSundaeNos, lblCalculateTotal, entUserName, entMobileNumber, window):
    vegExtravgNos = vegExtravg(btnVegExtravgNos)
    freshVeggieNos = freshVeggie(btnFreshVeggieNos)
    deluxeVeggieNos = deluxeVeggie(btnDeluxeVeggieNos)
    nonVegSupremeNos = nonVegSupreme(btnNonVegSupremeNos)
    pepperBbqNos = pepperBbq(btnPepperBbqNos)
    chickenFiestaNos = chickenFiesta(btnChickenFiestaNos)
    mirindaNos = mirinda(btnMirindaNos)
    pepsiNos = pepsi(btnPepsiNos)
    sevenUpNos = sevenUp(btnSevenUpNos)
    chocLavaCakeNos = chocLavaCake(btnChocLavaCakeNos)
    chocoBrownieNos = chocoBrownie(btnChocoBrownieNos)
    miniChocSundaeNos = miniChocSundae(btnMiniChocSundaeNos)
    totalCost = 0
    userNameData = entUserName.get()
    mobileNumberData = entMobileNumber.get()
    if (userNameData != "" or mobileNumberData != ""):
        if (userNameData.isalpha() == True or (userNameData.find('_'))!= -1 or (userNameData.find(' ')) != -1):
            if (len(mobileNumberData) == 10 and mobileNumberData.isnumeric() == True):
                if( mobileNumberData[0]=='7' or mobileNumberData[0]=='8' or mobileNumberData[0]=='9' ):
                    f = open("data/order.txt", "at")
                    if (vegExtravgNos > 0):
                        f.write("".join(["Veg. Extravaganza Pizza", "\t\t\t\t", "x", str(vegExtravgNos), "\t\t"]))
                        cost = 550 * vegExtravgNos
                        f.write("".join([str(cost), "\n"]))
                        totalCost = totalCost + cost
                    if (freshVeggieNos > 0):
                        f.write("".join(["Fresh Veggie Pizza", "\t\t\t\t", "x", str(freshVeggieNos), "\t\t"]))
                        cost = 480 * freshVeggieNos
                        f.write("".join([str(cost), "\n"]))
                        totalCost = totalCost + cost
                    if (deluxeVeggieNos > 0):
                        f.write("".join(["Deluxe Veggie Pizza", "\t\t\t\t", "x", str(deluxeVeggieNos), "\t\t"]))
                        cost = 600 * deluxeVeggieNos
                        f.write("".join([str(cost), "\n"]))
                        totalCost = totalCost + cost
                    if (nonVegSupremeNos > 0):
                        f.write("".join(["Non Veg. Supreme Pizza", "\t\t\t\t", "x", str(nonVegSupremeNos), "\t\t"]))
                        cost = 680 * nonVegSupremeNos
                        f.write("".join([str(cost), "\n"]))
                        totalCost = totalCost + cost
                    if (pepperBbqNos > 0):
                        f.write("".join(["Pepper BBQ Chicken Pizza", "\t\t\t\t", "x", str(pepperBbqNos), "\t\t"]))
                        cost = 580 * pepperBbqNos
                        f.write("".join([str(cost), "\n"]))
                        totalCost = totalCost + cost
                    if (chickenFiestaNos > 0):
                        f.write("".join(["Chicken Fiesta Pizza", "\t\t\t\t", "x", str(chickenFiestaNos), "\t\t"]))
                        cost = 700 * chickenFiestaNos
                        f.write("".join([str(cost), "\n"]))
                        totalCost = totalCost + cost
                    if (mirindaNos > 0):
                        f.write("".join(["Mirinda", "\t\t\t\t", "x", str(mirindaNos), "\t\t"]))
                        cost = 40 * mirindaNos
                        f.write("".join([str(cost), "\n"]))
                        totalCost = totalCost + cost
                    if (pepsiNos > 0):
                        f.write("".join(["Pepsi", "\t\t\t\t", "x", str(pepsiNos), "\t\t"]))
                        cost = 35 * pepsiNos
                        f.write("".join([str(cost), "\n"]))
                        totalCost = totalCost + cost
                    if (sevenUpNos > 0):
                        f.write("".join(["7UP", "\t\t\t\t", "x", str(sevenUpNos), "\t\t"]))
                        cost = 38 * sevenUpNos
                        f.write("".join([str(cost), "\n"]))
                        totalCost = totalCost + cost
                    if (chocLavaCakeNos > 0):
                        f.write("".join(["Chocolate Lava Cake", "\t\t\t\t", "x", str(chocLavaCakeNos), "\t\t"]))
                        cost = 50 * chocLavaCakeNos
                        f.write("".join([str(cost), "\n"]))
                        totalCost = totalCost + cost
                    if (chocoBrownieNos > 0):
                        f.write("".join(["Chocolate Brownie", "\t\t\t\t", "x", str(chocoBrownieNos), "\t\t"]))
                        cost = 45 * chocoBrownieNos
                        f.write("".join([str(cost), "\n"]))
                        totalCost = totalCost + cost
                    if (miniChocSundaeNos > 0):
                        f.write("".join(["Mini Chocolate Sundae", "\t\t\t\t", "x", str(miniChocSundaeNos), "\t\t"]))
                        cost = 60 * miniChocSundaeNos
                        f.write("".join([str(cost), "\n"]))
                        totalCost = totalCost + cost
                    lblCalculateTotal.configure(text=str(totalCost))
                    f.close()
                    f = open("data/order.txt", "r+")
                    f1 = open("data/allOrders.txt", "at")
                    f1.write(f.read())
                    f1.write("\n\n\n")
                    openNewWindow(totalCost, userNameData, mobileNumberData, window, btnVegExtravgNos, btnFreshVeggieNos, btnDeluxeVeggieNos, btnNonVegSupremeNos, btnPepperBbqNos, btnChickenFiestaNos, btnMirindaNos, btnPepsiNos, btnSevenUpNos, btnChocLavaCakeNos, btnChocoBrownieNos, btnMiniChocSundaeNos, lblCalculateTotal)
                    f.close()
                    f1.close()
                else:
                    messagebox.showerror("Error", "First digit of the mobile number should be '7', '8' or '9'.")
            else:
                messagebox.showerror("Error", "Length of the mobile number should be exactly 10 digits and must contain integers only.")
        else:
            messagebox.showerror("Error", "Username must only contain characters.")
    else:
        messagebox.showerror("Error", "Username / Mobile Number field is empty.")