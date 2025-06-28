#API

import requests

def pytanie():
    url = "http://numbersapi.com/random/year?json"
    response = requests.get(url)

    data = response.json()
    tekst = data["text"]
    rok = data["number"]
    print(rok)
    return tekst, rok

def quiz():
    print("🧩 Witaj w quizie .")
    tekst, poprawna_odpowiedz =pytanie()

    tekst_z_luka = tekst.replace(str(poprawna_odpowiedz), "___")
    print("\n📜 Ciekawostka:")
    print(tekst_z_luka)

    try:
        odpowiedz = int(input("\n🔢 Twoja odpowiedź: "))
        if odpowiedz == poprawna_odpowiedz:
            print("✅ Brawo! To poprawna odpowiedź.")
        else:
            print(f"❌ Pudło! Chodziło o rok {poprawna_odpowiedz}.")
    except ValueError:
        print("⚠️ Wprowadź poprawną liczbę.")
quiz()