
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, Listbox
import pymysql


def clear_frame():

    for widget in main_frame.winfo_children():
        widget.destroy()
def menu_page():
    clear_frame()

    open_buttonframe= tk.Frame(main_frame, bg='light grey')
    open_buttonframe.pack(fill=BOTH,expand=True)

    display_lable = Label(open_buttonframe, text="PLEASE SELECT FROM BELOW MENU : " ,bg="light grey", font = (" Ariel ",16) )
    display_lable.place (x= 50 , y= 25)

    image = Image.open("G:/python/Assinments/pythonProject/menu1.jpg")
    image = image.resize((600, 500))
    menu_image = ImageTk.PhotoImage(image)
    img_label = tk.Label(open_buttonframe, image=menu_image)
    img_label.menu_image = menu_image
    img_label.place(x=50, y=70)

    GOTO_lable = Label(open_buttonframe, text="IF YOU WANT TO LOOK INTO FOOD CATOGORIES ! PLEASE \nPRESS "
                                              "CATOGORIES BUTTON FROM ABOVE MENU BAR OR BELOW \n THIS BUTTON "
                                              "TO GO TO CATOGORIES : ",bg="light grey", font=(" Ariel ", 16))
    GOTO_lable.place(x=680, y=100)

    goto_button=Button(open_buttonframe, text="GO TO CATEGORIES", padx= 5, pady = 5, font=("Ariel",12), fg= 'red' ,command =catogory_page )
    goto_button.place(x= 900, y= 200)
def catogory_page():
    clear_frame()

    cat_buttonframe = tk.Frame(main_frame, bg='light grey')
    cat_buttonframe.pack(fill=BOTH,expand=True)

    image = Image.open("G:/python/Assinments/pythonProject/burger.jpg")
    image = image.resize((150,120))
    burger_image = ImageTk.PhotoImage(image)
    img_label=tk.Label(cat_buttonframe, image=burger_image)
    img_label.burger_image = burger_image
    img_label.place(x=130, y=50)

    Burgerlabel= Label(cat_buttonframe, text="burger", font=("Ariel", 16) , fg='red')
    Burgerlabel.place(x=170,y= 180)

    burgerbuttton = Button(cat_buttonframe, text ="ADD TO CART", font=("Ariel", 12), padx= 5, pady=5 , command= cart)
    burgerbuttton.place(x=140, y=220)


    image = Image.open("G:/python/Assinments/pythonProject/pizza.jpg")
    image = image.resize((150,120))
    pizza_image = ImageTk.PhotoImage(image)
    img_label=tk.Label(cat_buttonframe, image=pizza_image)
    img_label.pizza_image = pizza_image
    img_label.place(x=130, y=350)

    Pizzalabel= Label(cat_buttonframe, text="Pizza", font=("Ariel", 16) , fg='red')
    Pizzalabel.place(x=170,y= 480)

    Pizzabuttton = Button(cat_buttonframe, text ="ADD TO CART", font=("Ariel", 12), padx= 5, pady=5 , command= cart)
    Pizzabuttton.place(x=140, y=520)


    image = Image.open("G:/python/Assinments/pythonProject/pasta.jpg")
    image = image.resize((150, 120))
    pasta_image = ImageTk.PhotoImage(image)
    img_label = tk.Label(cat_buttonframe, image=pasta_image)
    img_label.pasta_image = pasta_image
    img_label.place(x=570, y=50)

    Pastalabel = Label(cat_buttonframe, text="Pasta", font=("Ariel", 16), fg='red')
    Pastalabel.place(x=610, y=180)

    Pastabuttton = Button(cat_buttonframe, text ="ADD TO CART", font=("Ariel", 12), padx= 5, pady=5 , command= cart)
    Pastabuttton.place(x=580, y=220)


    image = Image.open("G:/python/Assinments/pythonProject/salad.jpg")
    image = image.resize((150, 120))
    salad_image = ImageTk.PhotoImage(image)
    img_label = tk.Label(cat_buttonframe, image=salad_image)
    img_label.salad_image = salad_image
    img_label.place(x=570, y=350)

    Saladlabel = Label(cat_buttonframe, text="Salad", font=("Ariel", 16), fg='red')
    Saladlabel.place(x=610, y=480)

    Saladbuttton = Button(cat_buttonframe, text ="ADD TO CART", font=("Ariel", 12), padx= 5, pady=5 , command=cart)
    Saladbuttton.place(x=580, y=520)


    image = Image.open("G:/python/Assinments/pythonProject/fries.jpg")
    image = image.resize((150, 120))
    fries_image = ImageTk.PhotoImage(image)
    img_label = tk.Label(cat_buttonframe, image=fries_image)
    img_label.fries_image = fries_image
    img_label.place(x=960, y=50)

    Frieslabel = Label(cat_buttonframe, text=" Fries ", font=("Ariel", 16), fg='red')
    Frieslabel.place(x=1000, y=180)

    Friesbuttton = Button(cat_buttonframe, text ="ADD TO CART", font=("Ariel", 12), padx= 5, pady=5 , command= cart)
    Friesbuttton.place(x=970, y=220)


    image = Image.open("G:/python/Assinments/pythonProject/chicken.jpeg")
    image = image.resize((150, 120))
    chicken_image = ImageTk.PhotoImage(image)
    img_label = tk.Label(cat_buttonframe, image=chicken_image)
    img_label.chicken_image = chicken_image
    img_label.place(x=960, y=350)

    Chickenlabel = Label(cat_buttonframe, text=" Chicken ", font=("Ariel", 16), fg='red')
    Chickenlabel.place(x=1000, y=480)

    Chickenbuttton = Button(cat_buttonframe, text ="ADD TO CART", font=("Ariel", 12), padx= 5, pady=5 , command= cart)
    Chickenbuttton.place(x=980, y=520)

def cart():
    clear_frame()

    cart_buttonframe = tk.Frame(main_frame, bg='light grey')
    cart_buttonframe.pack(fill=BOTH, expand=True)

    menu = [
     ("Pizza", 1500),
     ("Burger", 650),
     ("Pasta", 400),
     ("Salad", 250),
     ("Fries", 100),
     ("Chicken",200)
    ]

    cart = []

    # Function to connect to the database
    def connect_db():
        try:
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password=' ',
                database='food_delivery'
            )
            return conn
        except pymysql.connect.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to the database: {e}")
            return None

    # Function to update the quantity in the database
    def update_quantity_in_db(item_name, quantity_sold):
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            # Update the quantity in the database by subtracting the sold quantity
            cursor.execute("""
                UPDATE menu_items 
                SET quantity_available = quantity_available - %s 
                WHERE item_name = %s AND quantity_available >= %s
            """, (quantity_sold, item_name, quantity_sold))

            if cursor.rowcount == 0:
                messagebox.showerror("Error", f"Not enough {item_name} available in stock!")
            else:
                conn.commit()
            conn.close()

    # Function to add item to the cart and update the quantity in the database
    def add_to_cart(item, price, quantity):
        if quantity.isdigit() and int(quantity) > 0:
            cart.append((item, price, int(quantity)))
            update_cart_list()
            update_quantity_in_db(item, int(quantity))
            messagebox.showinfo("Success", f"Added {quantity} x {item} to cart!")
        else:
            messagebox.showwarning("Input Error", "Please enter a valid quantity.")

    # Function to update the cart list in the Listbox
    def update_cart_list():
        cart_listbox.delete(0, tk.END)
        for item, price, quantity in cart:
            cart_listbox.insert(tk.END, f"{item} - Quantity: {quantity} - Price: {price * quantity}")

    # Function to place an order
    def place_order():
        if cart:
            total = sum(price * quantity for _, price, quantity in cart)
            messagebox.showinfo("Order Placed", f"Your order has been placed! Total amount: {total} PKR")
            cart.clear()
            update_cart_list()
        else:
            messagebox.showwarning("Cart Empty", "Your cart is empty!")

    # Function to remove an item from the cart
    def remove_from_cart():
        selected_item = cart_listbox.curselection()
        if selected_item:
            cart.pop(selected_item[0])
            update_cart_list()
            messagebox.showinfo("Success", "Item removed from cart!")
        else:
            messagebox.showwarning("Selection Error", "Please select an item to remove.")

    tk.Label(cart_buttonframe, text="Menu : ", bg="light grey",fg="red", font=("Ariel", 14)).grid(row=0, column=0, padx=10, pady=10)

    row = 1
    for item, price in menu:
        tk.Label(cart_buttonframe, text=item).grid(row=row, column=0, padx=10, pady=5)
        tk.Label(cart_buttonframe, text=f"{price} PKR").grid(row=row, column=1, padx=10, pady=5)
        tk.Label(cart_buttonframe, text="Quantity: ").grid(row=row,column=2,pady=5)
        quantity_entry = tk.Entry(cart_buttonframe)
        quantity_entry.grid(row=row, column=3, padx=10, pady=5)
        tk.Button(cart_buttonframe, text="Add to Cart", command=lambda i=item, p=price, q=quantity_entry: add_to_cart(i, p, q.get())).grid(row=row, column=4, padx=10, pady=5)
        row += 1

     # Cart Display
    tk.Label(cart_buttonframe, text="Shopping Cart : " ,bg="light grey",fg="red",font=("Ariel", 14)).grid(row=7, column=0, padx=10, pady=10)

    cart_listbox = Listbox(cart_buttonframe, width=110,height=15)
    cart_listbox.grid(row=8, column=1, rowspan=4, padx=10, pady=10)

   # Buttons to manage cart
    tk.Button(cart_buttonframe, text="Remove Selected", command=remove_from_cart).grid(row=5, column=5, padx=10, pady=5)
    tk.Button(cart_buttonframe, text="Place Order", command=place_order).grid(row=6, column=5, padx=10, pady=5)

    tk.Button(cart_buttonframe, text="Back to menu", command=menu_page,fg="red", font=("Ariel", 16)).grid(row= 8,column=5,padx=10,pady=5)
def about():
    clear_frame()

    about_buttonframe = tk.Frame(main_frame, bg='light grey')
    about_buttonframe.pack(fill=BOTH, expand=True)

    about_label=Label(about_buttonframe, text="About Us : ",fg="red", font=("Ariel", 20))
    about_label.place(x= 100, y=50)

    info_label = Label(about_buttonframe, text="Welcome to Abdullah Fast Foods, your go-to destination for quick, delicious \n"
                                               "and convenient meals!Founded by Abdullah Naveed, alongside co-founder Naveed Akbar,\n "
                                               "our mission is to deliver exceptional fast food with a seamless user experience.\n "
                                               "As a student at the University of Central Punjab, I created this interactive GUI to provide \n"
                                               "customers with an easy-to-use platform for ordering food. Our system is designed to make the \n"
                                               "ordering process simple, efficient, and enjoyable, allowing you to explore our diverse menu or \n"
                                               "categories with just a few clicks. Whether you're craving a quick snack or a full meal, \n"
                                               "Abdullah Fast Foods ensures that your experience is as satisfying as the food we serve. \n"
                                               "We’re committed to enhancing your journey from menu selection to checkout, \n"
                                               "making fast food ordering faster and more accessible than ever! ",bg="light grey",  font=("Ariel", 16))


    info_label.place(x=250, y=90)

    aboutgotomenubutton=Button(about_buttonframe,text="Back to Menu",fg="red", font=("Ariel",16) ,command=menu_page)
    aboutgotomenubutton.place(x=600,y=400)

w = tk.Tk()
w.title("Custom Menu Bar")
w.state('zoom')

image = Image.open("G:/python/Assinments/pythonProject/bg.jpg")
bg_image = ImageTk.PhotoImage(image)



    # Create a frame for the custom menu bar
menu_frame = Frame(w, bg='yellow', padx=10, pady=10)
menu_frame.pack(side =TOP,fill=X)

    # Create buttons to act as the menu items
menu_button1 = Button(menu_frame, text="Menu",fg="red", font=("Ariel", 10), padx=10, pady=5, command=menu_page)
menu_button1.pack(side = LEFT, padx=50)

menu_button2 = Button(menu_frame, text="Categories",fg="red", font=("Ariel", 10), padx=10, pady=5 ,command= catogory_page)
menu_button2.pack(side=LEFT, padx=10)

menu_button3 = Button(menu_frame, text="CART",fg="red", font=("Ariel", 10), padx=10, pady=5, command= cart)
menu_button3.pack(side=LEFT, padx=50)

menu_button4 = Button(menu_frame, text="About Us",fg="red", font=("Ariel", 10), padx=10, pady=5, command=about)
menu_button4.pack(side=LEFT, padx=10)

label1 = Label( menu_frame, text="Search",fg="black",bg= 'yellow',font=("Ariel", 20) )
label1.pack(side = LEFT, padx=(250,5))

s_entry=Entry(menu_frame, font=("Ariel", 20))
s_entry.pack(side=LEFT, padx=5)


main_frame=tk.Frame(w, bg='light grey')
main_frame.pack(fill=BOTH, expand=True)

logo_label=Label(main_frame,text="WELCOME TO ABDULLAH FAST FOODS", font=("Ariel", 20) ,bg="white" ,fg="red")
logo_label.pack(padx= 10,pady=20)

image = Image.open("G:/python/Assinments/pythonProject/logo.jpg")
image = image.resize((350, 300))
logo_image = ImageTk.PhotoImage(image)
img_label = tk.Label(main_frame, image=logo_image)
img_label.logo_image = logo_image
img_label.place(x=500, y=100)

declabel = Label(main_frame, text=" Please press menu or catogories button for furthur process\n "
                                      " Or you can also choose from above Menu Bar", font=("Ariel", 16),bg="light grey", fg='red')
declabel.place(x=390, y=440)

menbuttton = Button(main_frame, text="Menu",fg="black",bg="yellow", font=("Ariel", 12), padx=15, pady=5, command=menu_page)
menbuttton.place(x=500, y=510 )

catbuttton = Button(main_frame, text="Catogories",fg="black",bg="yellow", font=("Ariel", 12), padx=5, pady=5, command=catogory_page)
catbuttton.place(x=800, y=510)

w.mainloop()


