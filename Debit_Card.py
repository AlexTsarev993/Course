card = input("Enter card(16 numbers) : ")
hide_card = card[:4] + "********" + card[-4:]
print(hide_card)