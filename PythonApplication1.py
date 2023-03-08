from module1 import *
while True:
    print("Tere! Käime läbi riigid ja nende pealinnad!")
    print("1 – Uurige välja riigi pealinn või vastupidi,\n2 – Lisage uus riik ja pealinn,\n3 – Parandage viga,\n4 – pange oma teadmised proovile")
    menu = input()
    if menu == "1":
        v = input("Otsime riiki pealinna järgi (1) või pealinna riigi järgi (2)? ")
        countries   (failist_to_dict, v)
    elif menu == "2":
        new_key_value (failist_to_dict)
    elif menu == "3":
        correct_errors(failist_to_dict)
    elif menu == "4":
        test_knowledge(failist_to_dict)
        # code for the knowledge test
        pass
    else:
        print("Vigane sisestus.")

