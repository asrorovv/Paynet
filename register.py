import classes


import mainmenu


def register():
    try:
        print("<<<REGISTER PAGE>>>")
        first_name = input("Ism: ")
        last_name = input("Familiya: ")
        phone = input("Telefon raqamni kiriting +998__ ")
        card = input("Karta raqamni kiriting: ")
        card_period = input("Amal qilish muddatini kiriting: ")

        if (first_name and last_name and card_period is True) and len(phone) == 9 and len(card) == 16:
            user = classes.Paynet(first_name, last_name, phone, card, card_period)
            user.save()
            return mainmenu.menu()
        else:
            return register()

    except Exception as error:
        print(f"{error}")


