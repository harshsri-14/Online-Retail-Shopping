import time
import os

stock = {}

def Admin_Module(): 
    _ = os.system('clear')
    
    print("----------------------------------------------------------------------")
    print()
    print("    WELCOME TO ADMINISTRATOR MODULE OF ONLINE RETAIL SHOPPING APP   ")
    print()
    print("----------------------------------------------------------------------")
    print("\t   HINT: Select Your Desired Option \
        \n\t  By Pressing The Corresponding Number")
    print("----------------------------------------------------------------------")
    print()
    print("\t[1]. Add Product in Stock")
    print("\t[2]. Update Product price in Stock")
    print("\t[3]. Remove Product from Stock")
    print("\t[4]. View All Products in Stock")
    print("\t[5]. Sign Out")
    print()
    print('----------------------------------------------------------------------')

    print("\n")
    
    try :
        choice = int(input("\tYour Choice Here: "))
        
        if choice > 0 and choice < 6 :
            if choice == 1 :
                _ = os.system('clear')
                print("\n\n")
                NewProduct = input(" >> Enter Product Name: ")

                if NewProduct in stock :
                  print("\n\n >>> PRODUCT IS ALREADY IN STOCK !!")
                  
                else :
                  UnitPrice = float(input(" >> Enter Unit Price: "))
                  
                  stock[NewProduct] = UnitPrice
                  print("\n\n >>> PRODUCT ADDED SUCCESFULLY !!")

                input(" [ Press enter to return to menu. ]")
                return False
                
                

            elif choice == 2 :
                _ = os.system('clear')

                if len(stock) == 0 :
                    print("\n\n >> No Products Available.")

                else :
                    print(" ## FOLLOWING ITEMS ARE CURRENTLY IN-STOCK : ")
                    print()
                    print("-------------------------------------------------------------")
                    print("\t     Product Name          --     Per Unit Price")
                    print("-------------------------------------------------------------")

                    for item in stock.keys() :
                        print(item.center(30),"--\t\t Rs.",stock[item])

                    print()
                    print("-------------------------------------------------------------")
                    print("\n\n")

                    Product_Name = input(" >> Enter Product Name Which Price To Be Updated: ")
                    if Product_Name in stock :
                        New_Price = float(input(" >> Enter New Price: "))
                        stock[Product_Name] = New_Price
                        print("\n\n >>> PRICE OF {} UPDATED SUCCESSFULLY !!".format(Product_Name.upper()))

                    else :
                        print("\n\n >>> ERROR !! EITHER {} IS NOT AVAILABLE IN STOCK OR YOU MISS-SPELLED.".format(Product_Name.upper()))
                
                input(" [ Press enter to return to menu. ]")
                return False


            elif choice == 3 :
                _ = os.system('clear')

                if len(stock) == 0 :
                    print("\n\n >> No Products Available.")

                else :
                    print(" ## FOLLOWING ITEMS ARE CURRENTLY IN-STOCK : ")
                    print()
                    print("-------------------------------------------------------------")
                    print("\t     Product Name          --     Per Unit Price")
                    print("-------------------------------------------------------------")

                    for item in stock.keys() :
                        print(item.center(30),"--\t\t Rs.",stock[item])

                    print()
                    print("-------------------------------------------------------------")
                    print("\n\n")

                    Product_Name = input(" >> Enter Product Name Which You Want To Delete: ")
                    if Product_Name in stock :
                        del stock[Product_Name]
                        print("\n\n >>> STOCK UPDATED SUCCESSFULLY !!")

                    else :
                        print("\n\n >>> ERROR !! EITHER {} IS NOT AVAILABLE IN STOCK OR YOU MISS-SPELLED.".format(Product_Name.upper()))
                
                input(" [ Press enter to return to menu. ]")
                return False


            elif choice == 4 :
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


            elif choice == 5 :
                _ = os.system('clear')

                print("\n\n >> ADMINISTRATOR MODULE COMPLETED SUCCESSFULLY !!")
                print("\n\n * you'll be re-directed to USER-MODULE in few seconds...")
                time.sleep(2)

                return True
                
        else :
            print("\n>>> ERROR OCCURED !!")
            print(">>> CHOICE MUST BE IN RANGE OF 1-5 !!")
            input(" [ Press enter to retry. ]")

    
    except (ValueError) :
        print("\n>>> ENTER NUMBERS ONLY !!")
        input(" [ Press enter to retry. ]")