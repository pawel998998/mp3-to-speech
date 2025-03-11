from gtts import gTTS
import os

def tekst_na_mp3(tekst, nazwa_pliku="output.mp3", jezyk="pl"):
    try:
    tts = gTTS(text=tekst, lang=jezyk, slow=False)
    tts.save(nazwa_pliku)
    print(f"Tekst został zapisany jako {nazwa_pliku}")
  except Exception as e:
    print(f"Wystąpił błąd: {e}")

def pobierz_tekst_z_pliku(nazwa_pliku="tekst.txt"):
  try:
    with open(nazwa_pliku, "r", encoding="utf-8") as f:
      tekst = f.read()
    return tekst
  except FileNotFoundError:
    print(f"Plik {nazwa_pliku} nie został znaleziony.")
    return ""
  except Exception as e:
    print(f"Wystąpił błąd podczas odczytu pliku: {e}")
    return ""

if __name__ == "__main__":
  nazwa_pliku_tekstowego = "tekst.txt"
  if not nazwa_pliku_tekstowego:
      nazwa_pliku_tekstowego = "tekst.txt"
  tekst_do_zamiany = pobierz_tekst_z_pliku(nazwa_pliku_tekstowego)
  if not tekst_do_zamiany:
    print("Brak tekstu do przetworzenia. Program zakończy się.")
    exit()

  nazwa_mp3 = "mowa.mp3"
  jezyk_mowy = "pl"
  if not nazwa_mp3:
    nazwa_mp3 = "output.mp3"
  if not jezyk_mowy:
    jezyk_mowy = "pl"
  tekst_na_mp3(tekst_do_zamiany, nazwa_mp3, jezyk_mowy)
  print ("Program zakończony.")