
from random import *
def failist_to_dict(f:str):
    riik_pealinn={}#s6nastik {"Riik":"Pealinn"}
    pealinn_riik={}#s6nastik {"Pealinn":"Riik"}
    riigid=[] #jarjend, kus talletakse riigide nimetused
    file=open(f,'r', encoding="utf-8-sig")
    for line in file:
        k,v=line.strip().split('~-') #k-voti, v-vairtus
        riik_pealinn[k]=v #t&idame riik_pealinn
        pealinn_riik[v]=k #t&idame pealinn_riik
        riigid.append(k)
    file.close()
    return riik_pealinn,pealinn_riik,riigid
#kdivitame loodud funktsion

("riigid_pealinnad.txt")


def countries(failist_to_dict, v):
    if v == "1":
        pealinn_riik = input("Sisestage pealinna nimi: ")
        for key, value in failist_to_dict.items():
            if value == pealinn_riik:
                print("Riik: ", key)
                return
        print("Nimekirjas sellist kapitali pole.")
    elif v == "2":
        riik_pealinn = input("Sisesta riigi nimi:")
        if riik_pealinn in failist_to_dict:
            print("Kapital: ", failist_to_dict[riik_pealinn])
        else:
            print("Seda riiki nimekirjas ei ole.")
    else:
        print("Vigane sisestus.")

def new_key_value(failist_to_dict):
    key = input("Sisesta riigi nimi: ")
    value = input("Sisestage pealinna nimi: ")
    failist_to_dict[key] = value
    print("Kirje lisati sõnastikku.")

def correct_errors(failist_to_dict):
    key = input("Sisestage parandatava riigi või pealinna nimi: ")
    if key in failist_to_dict:
        new_value = input("Sisestage uus väärtus: ")
        failist_to_dict[key] = new_value
        print("Väärtust on muudetud.")
    else:
        print("Sellist kirjet sõnastikus pole.")
def test_knowledge(failist_to_dict):
    correct_answers=0
    total_questions=0
    while True:
        question_type=input("1 – pealinn või 2 – riik? ")
        if question_type=="1":
            question=random.choice(list(failist_to_dict.values()))
            answer=input(f"Nimetage riik, mille pealinn on {question}: ")
            for key,value in failist_to_dict.items():
                if value==question:
                    if answer==key:
                        print("õige!")
                        correct_answers+=1
                    else:
                        print(f"Vale. Õige vastus: {key}")
                    total_questions+=1
                    break
            else:
                print("Tekkis viga. Proovi uuesti.")
        elif question_type=="2":
            question=random.choice(list(failist_to_dict.keys()))
            answer=input(f"Nimetage riigi pealinn {question}: ")
            if answer==failist_to_dict[question]:
                print("õige!")
                correct_answers+=1
            else:
                print(f"Vale. Õige vastus: {failist_to_dict:[answer]}")
