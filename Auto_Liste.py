Garage = ["Mercedes", "ferrari", "BMW", "Porsche"]
while True:
    frage = input("Was willst du machen /hinzufügen/entfernen/zählen/anzeigen/quit " )


    if frage == "hinzufügen":
         auto = input("Wie heißt das Auto " )
         Garage.append(auto)
         if len(auto) >= 4:
             print("der name ist aber lang" )
         elif len(auto) <4:
             print("der name ist aber kurz")


    elif frage == "entfernen":
        entfernen = input("welches auto soll entfernt werden " )
        if entfernen in Garage:
            Garage.remove(entfernen)
        elif entfernen not in Garage:
            print("das Auto ist garnicht in der liste oder du hast es falsch geschrieben")

    elif frage == "anzeigen":
        print(Garage)


    elif frage == "zählen":
        print(len(Garage))

    elif frage == "quit":
        # Wir speichern die Liste in eine Datei namens "meine_autos.txt"
        with open("meine_autos.txt", "w") as datei:
            # Wir machen aus der Liste einen Text, getrennt durch Kommas
            datei.write(", ".join(Garage))
        print("Garage wurde in 'meine_autos.txt' gespeichert. Bis bald!")
        break
    else:
        print("bitte gebe nur hinzufügen/entfernen/zählen ein")

