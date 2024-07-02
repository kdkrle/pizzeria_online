# 1. Project title
    ONLINE ORDERS FOR RESTAURANT (PIZZERIA)

# 2. Brief description of the project
The project was done as an integral part of the practice course "Python 
Developer - Advanced" in the company **ITOiP** (IT Training and Practice - 
https://itoip.rs).

Order and payment management system for a fictitious pizzeria.

The application was made in Python, with the help of the PostgreSQL 
database management system.

Tables made as an example are in the archive 'tables.zip'.

# 3. The README.md file contents
#### 1. Project title
#### 2. Brief description of the project
#### 3. The README.md file contents
#### 4. Database and table structure
#### 5. Application description and usage

# 4. Database and table structure
Database name: "picerija-porucivanje"

Tables:

    artikli
        naziv               (varchar (30), primary key, not null)
                                                    # article name
        vrsta               (varchar (29))          # article type
        sastav              (text, not null)        # article composition
        kolicina            (integer, not null)     # articles available number
        cena                (integer, not null)     # article price

    porudzbine
        sifra               (varchar (10), prmary key, not null)
                                                        # order code
        adresa              (varchar (30), not null)    # delivery address
        telefon             (varchar (10), not null)    # contact phone
        placanje            (varchar (10), not null)    # payment method
        status              (varchar (25), not null)    # order status
        ukupno              (integer, not null)         # total price

    stavke
        broj stavke         (serial, primary key, not null)
                                                        # item number
        sifra               (varchar (10), not null)    # order code
        stavka              (varchar (30), not null)    # single item
        komada              (integer, not null)         # item amount

    transakcije
        sifra               (varchar (10), primary key, not null)
                                                        # transaction code
        uplatilac           (varchar (25), not null)    # payer full name
        racun               (varchar (20), not null)    # bank account number
        iznos               (integer, not null)         # transaction amount
# 5. Application description and usage

## 5.1. Main Screen

The main screen consists of the name of the pizzeria, an image and buttons 
for selecting an action in the application. Each button has a short 
explanation next to it, except for the 'Zatvori' (Close) button at the 
bottom of the screen, which is used to close the application.

## 5.2 Menu

By pressing the 'Meni' (Menu) button on the main screen, a new window opens 
with a selection of items by category.

In the left part of the screen there are buttons for different categories 
of items. These are: 'Pica' (Pizzas), 'Salate' (Salads), 'Sendviči' 
(Sandwiches), 'Deserti' (Desserts) and 'Napici' (Drinks). By pressing a 
button, we get a list of items from that category that we can order. 
The tabular list consists of the name of the article, its composition and 
prices. When opening the screen, the category 'Pizzas' is loaded as the 
basic type of items offered.

At the bottom of this screen there is a 'Poruči' (Order) button, which takes 
us to the ordering section and an 'Izađi' (Exit) button which closes the 
screen. The 'Poruči' (Order) button also closes this screen and opens a new 
one, which can also be accessed from the main screen.

## 5.3 Ordering

#### 5.3.1 Article type, article list and cart

By pressing the 'Poručivanje' (Ordering) button, we open the part related to 
creating an order. As already mentioned, the 'Poruči' (Order) button from the 
previous window also brings us to the ordering section.

On the new screen that opens, below the title, there are short explanations 
about ordering, i.e. about the time of delivery, the method of inserting 
articles into the basket and deleting them from it, as well as about the 
letters at the end of the name of pizzas, which indicate the size of its 
diameter.

In a similar way as on the menu screen, here we also have a selection of 
categories of offered articles, only that here the selection is made by 
selecting one of the options. That choice of article type is offered to us on 
the left.

In the middle part of the screen we have the name, composition and price of 
the articles from the selected category. On the right side is the cart in 
which the articles and their quantity that we want to order are inserted. 
At the bottom of the screen there is a button to add an article to the basket, 
a button to delete from the basket, a button to complete the order and a 
button to close this screen.

In order for an article to be added to the cart, it must be marked in the 
middle of the screen. By pressing the 'Ubaci' (Insert) button, a small window 
opens which, in addition to the name of the article, allows us to increase the 
quantity of the selected article.

Below the basket itself, the total price of the articles added to the 
basket is displayed.

If we are not satisfied with what is in the cart, we can delete individual 
articles by marking them and pressing the 'Izbriši' (Delete) button. If we 
are satisfied with the contents of the cart, by pressing the 'Poruči' (Order) 
button, we open a new screen where the creation of the order is completed.

#### 5.3.2 Choice of payment and entry of necessary data

A new window allows us to choose the payment method. Payment can be made in 
cash or by card when picking up the order or immediately online, also with 
the help of a payment card.

In the left part of the screen there is a payment option. Below it are the 
details of the order in the form of the name of the articles and their 
quantity, while below those details is the total price of the order.

The right part of the screen is provided for entering the necessary data. 
At the top, there are fields for entering the delivery address and a 
contact phone number that can be used to contact the customer. This 
information is required for each type of payment choice. They are followed 
by a program-generated order code that can be used to track the status of 
the order.

Below all that, there are input fields for online payment. They are 
unavailable until online payment is selected on the left side of the screen.
In these fields, the name and surname of the payer must be entered, which 
must match the number of the card from which the payment is made. 
Immediately follows the field used to enter exactly that bank account 
number. As additional insurance, the entry of a PIN known to the account 
user is used, which digits are not visible when entering. If all three 
values agree and there is enough money in the account to pay for the order, 
it is possible to complete the transaction.

**NOTE**: Here it would be best to insert some of the existing APIs that 
enable real transactions. However, they are mostly commercial. In addition, 
they serve for real transactions, which for the purposes of this project are 
neither necessary nor desirable. Therefore, a simplified system is made 
here with the help of data placed in the file 'podaci.py' (data). The 
'Generiši' (Generate) button in the online payment fields inserts data that 
is considered valid, any other random input or change of the generated data 
will be considered as an incorrect input and the transaction simulation 
will be rejected. It should also be noted that funds are not withdrawn from 
the account during the transaction, as this is not the job of this program. 
These fictitious funds exist only for the purposes of displaying other 
functions and features of the application.

The button 'Realizuj' (Realize) serves to complete the creation of the order.

If the order is rejected, a notification will appear about what went wrong. 
On the other hand, if it is accepted, this screen closes, and a greeting 
screen opens with a notification about the successfully created order, 
which, in addition to the notification and greeting, contains the order 
code, which is used to track its status.

Finally, since the order is successfully created, the relevant data is 
inserted into all the tables. In the 'artikli' (articles) table, the 
quantity of items is corrected, order data is entered in the 'porudzbine' 
(orders) table, order details are entered in the 'stavke' (items) table, 
transaction information (if the payment was online) is entered in the 
'transakcije' (transactions) table.

## 5.4. Payment methods

The button 'Načini plaćanja' (Payment methods), from the main screen, takes us 
to a new window where we can see the ways in which it is possible to pay 
for the order and when the payment is executed. Apart from these 
notifications, there is only one button 'Zatvori' (Close) which, as the name 
suggests, closes this window.

## 5.5. Order tracking

Pressing the 'Praćenje porudžbine' (Order tracking) button on the main 
screen opens a new window that requires you to enter the code of the order 
you want to track. Only the one who knows the code can continue.

When the correct code is entered, a new window opens in which, under the 
title, we can see the status of the order. Possible statuses are: 'Kreirana' 
(Created), 'U pripremi' (Preparing), 'Poslata' (Sent) and 'Isporučena' 
(Delivered). Below the status is the code of the order we want to track. 
This is followed by details about the ordered articles and their quantities, 
and finally the price of the order is highlighted.

The 'Zatvori' (Close) button closes this window.

## 5.6 Changes

Pressing the 'Izmene' (Changes) button on the main form opens a password entry 
window. This window is necessary, because the changes made should not be 
accessed by all users, but only by those persons who are authorized to do 
so. Since this project has the role of showing the capabilities of the 
application, it should be said that the password is 'MP-pice', in order to 
get an insight into that part of the program as well.

After entering the correct password and confirming it, a new window opens 
in which we can make two types of changes.

#### 5.6.1 Changing status

In the left part of the new window, it is possible to change the status of 
the order. The drop-down menu for selecting a new status and the 'Promeni' 
(Change) button, which makes the change, are unavailable until the order 
code is selected.

A list of all order codes can be found in the drop-down menu above. When 
selecting any password, the status selection drop-down menu and the change 
button become available. The current status of the order is entered in the 
status drop-down menu, which can be changed by selecting one of the other 
statuses offered.

#### 5.6.2 Adding articles

The right part of the screen is for adding articles in stock. First there 
is a selection of all articles, only those articles with less than 20 in 
stock or a selection of only those articles with less than 10 in stock. It 
is clear that the latter serves to quickly gain insight into what urgently 
needs to be added.

Each of these selections offers a list of items according to their amount 
in stock. The selection of an articles from the list is made in the following 
drop-down menu. After selecting an article, its current amount in stock is 
shown - under the text 'Items in stock:'.

How many items are added to the balance is entered in the Spinbox at the 
bottom. If we are satisfied with the entered number, by pressing the 'Dodaj' 
(Add) button we can add the entered quantity of the selected article in 
stock.

After adding in stock, the 'artikli' (articles) table and the list of 
articles are updated if the selected item exceeds the default values of 20 
and 10.

The 'Zatvori' (Close) button closes this window.

## 5.6 Reports

Finally, the 'Izveštaji' (Reports) button, from the main screen, takes us to a 
new window where we have 8 choices. The first choice only gives us a 
notification about the total income of the pizzeria, in a separate window. 
Other options are graphical displays according to the described criteria.

The second and third options show the top 5 and top 20 best-selling articles.

The fourth option shows the percentage income for the top 5 articles, which 
are the best in that category, along with the percentage income of all other 
articles combined.

The fifth and sixth choices give us 5 orders each with income values are
the biggest and the smallest.

The last two options give us an insight into the 10 most expensive and 10 
cheapest articles.
