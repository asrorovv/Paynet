import classes
def menu():

    print(f"<<<<<<<<<<<<<<<<<<<<<<<<<<<{classes.Card.get_balance} SO`M>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    enter = input(f"""
                                            MENU
                                    1. Asosiy
                                    2. O`tkazmalar
                                    3. To`lov
                                    4. Tarix>>> """)

    if enter == "1":
        print(f"""          Raqam: {classes.Card.get_phone}
        
        
         
        Balans: {classes.Card.get_balance}
        
""")
        karta = input(f"""
        
                        1. Kartalarim
                        2. O`tkazish
                        3. To'lash 
""")
        if karta == "1":
            return

