from admin import stock
import time
import os

shopping_basket = {}


def User_Module() :
    _ = os.system('clear')

    print("----------------------------------------------------------------------")
    print()
    print("    WELCOME TO USER-MODULE OF ONLINE RETAIL SHOPPING APP   ")
    print()
    print("----------------------------------------------------------------------")
    print("\t   HINT: Select Your Desired Option \
        \n\t  By Pressing The Corresponding Number")
    print("----------------------------------------------------------------------")
    print()
    print("\t[1]. View All Products in Stock")
    print("\t[2]. Add to shopping basket")
    print("\t[3]. View all product of basket")
    print("\t[4]. Search product in Stock")
    print("\t[5]. Remove product from basket")
    print("\t[6]. Print invoice")
    print("\t[7]. Sign Out")
    print()
    print('----------------------------------------------------------------------')
    print("\n")    

    try :
        choice = int(input("\tYour Choice Here: "))
        
        if choice > 0 and choice < 8 :
            if choice == 1 :
                _ = os.system('clear')

                if len(stock) == 0 :
                    print("\n\n >> No Products Available.")

                else :
                    print("\n")
                    print(" ## FOLLOWING ITEMS ARE CURRENTLY IN-STOCK : ")
                    print()
                    print("-------------------------------------------------------------")
                    print("\t     Product Name          --     Per Unit Price")
                    print("-------------------------------------------------------------")

                    for item in stock.keys() :
                        print(item.center(30),"--\t\t Rs.",stock[item])
                    print()
                    print("-------------------------------------------------------------")

                print()
                input("\t [ Press enter to return to menu. ]")

                return False


            elif choice == 2 :
                _ = os.system('clear')
                Product_Name = input("\n >> Enter Product Name: ")

                if Product_Name in stock :
                    Req_Quantity = int(input(" >> Enter Quantity: "))
                    shopping_basket[Product_Name] = Req_Quantity
                    print("\n\n >>> {} is added to Cart.".format(Product_Name))

                else :
                    print("\n\n >>> This Product is Not Available in Stock.")

                input(" [ Press enter to return to menu. ]")

                return False



            elif choice == 3 :
                _ = os.system('clear')

                if len(shopping_basket) == 0 :
                    print("\n\n >> No Products Available.")
                    print("\n\n\n\n\n\n")

                else :
                    print("\n")
                    print(" ## FOLLOWING ITEMS ARE AVAILABLE IN YOUR BASKET : ")
                    print()
                    print("-------------------------------------------------------------")
                    print("\t     Product Name          --     Quantity")
                    print("-------------------------------------------------------------")

                    for item in shopping_basket.keys() :
                        print(item.center(30),"--\t\t ",shopping_basket[item])
                    print()
                    print("-------------------------------------------------------------")

                print()
                input("\t [ Press enter to return to menu. ]")

                return False



            elif choice == 4 :
                _ = os.system('clear')
                Product_Name = input("\n >> Enter Product Name: ")

                if Product_Name in stock :
                    print("\n\n >>> {} is IN-STOCK !!".format(Product_Name))
                else :
                    print("\n\n >>> {} is Not Available in Stock.".format(Product_Name))

                input(" [ Press enter to return to menu. ]")
                return False



            elif choice == 5 :
                _ = os.system('clear')

                if len(shopping_basket) == 0 :
                    print("\n\n >> No Products Available.")

                else :
                    print("\n")
                    print(" ## FOLLOWING ITEMS ARE AVAILABLE IN YOUR BASKET : ")
                    print()
                    print("-------------------------------------------------------------")
                    print("\t     Product Name          --     Quantity")
                    print("-------------------------------------------------------------")

                    for item in shopping_basket.keys() :
                        print(item.center(30),"--\t\t ",shopping_basket[item])
                    print()
                    print("-------------------------------------------------------------")

                    print("\n\n")


                    Product_Name = input(" >> Edit Product Name To Remove From Shopping Basket: ")

                    if Product_Name in shopping_basket :
                        del shopping_basket[Product_Name]
                        print("\n >>> CART UPDATED SUCCESSFULLY !!")

                    else :
                        print("\n\n >>> {} is Not Available in Cart.".format(Product_Name))

                input(" [ Press enter to return to menu. ]")
                return False



            elif choice == 6 :
                _ = os.system('clear')

                from datetime import date
                cust_name = input("\n\n >> Enter Customer Name to be Printed on Invoice: ")
                print("\n\n >> Please wait, we're generating your invoice...!!")
                time.sleep(3)

                _ = os.system('clear')

                print("\n\n")
                print("------------------------------------------------------------------------")
                print(" \t\t INVOICE | ONLINE SHOPPING REATAIL APP ")
                print("------------------------------------------------------------------------")
                print()
                print("  Customer Name: {}".format(cust_name))
                print("  Date: {}".format(date.today()))
                print()
                print("------------------------------------------------------------------------")
                print("     PRODUCT NAME    |  QTY.  |  UNIT PRICE |   Amount")
                print("------------------------------------------------------------------------")

                for items in shopping_basket.keys() :
                    print(items.center(20), "|", str(shopping_basket[items]).center(6), "|", 
                    str(stock[items]).center(11), "|", str(shopping_basket[items] * stock[items]).center(8))
                print()
                print("------------------------------------------------------------------------")

                grand_total = 0
                for price in shopping_basket :
                    grand_total += shopping_basket[price] * stock[price]

                print("\t GRAND TOTAL \t = \tRs. {}".format(grand_total))
                print("------------------------------------------------------------------------")
                
                print("\n\n")
                input("\t\t [ Press enter to exit. ]")
                return False

                

            elif choice == 7 :
                _ = os.system('clear')
                print("\n\n >>> This Program Has Been Successfully Executed! :)")
                print(" >>> Developed by: Harsh Srivastava")
                print("\n\n")
                
                return True

        else :
            print("\n>>> ERROR OCCURED !!")
            print(">>> CHOICE MUST BE IN RANGE OF 1-7 !!")

            input(" [ Press enter to retry. ]")

            return False

    
    except (ValueError) :
        print("\n>>> ENTER NUMBERS ONLY !!")
        input(" [ Press enter to retry. ]")
        return False