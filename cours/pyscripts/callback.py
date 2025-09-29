def fct_callback(arg):
    print("J'aime bien les {} !".format(arg))

def une_fct(ma_callback):
    print("Je suis au début de une_fct(), "
          "et je vais exécuter la fonction callback :")
    ma_callback("fraises")
    print("Aye, une_fct() se termine.")

# prog principal
une_fct(fct_callback)
