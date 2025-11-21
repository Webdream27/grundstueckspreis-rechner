""" **********************************
Aufgabe 1 Grundstueckspreis Berechnung
***********************************""" 

# Konstanten
# Feste Werte, die nur einmal geaendert werden muessen

PROVISION_SATZ = 0.05  # 5 Prozent Provision
MWST_SATZ = 0.19       # 19 Prozent Mehrwertsteuer

# Funktion: berechnet den Grundstueckspreis inkl. Provision und Mehrwertsteuer
def berechne_grundstueckspreis():
    
    print("Grundstueckspreis-Rechner")
    
    # Faengt Fehler bei der Eingabe (z.B. Buchstaben statt Zahlen) ab
    try:
        # 1. Einlesen der Grundstuecksdaten
        laenge = float(input("Geben Sie die Laenge des Grundstuecks in Metern ein: "))
        breite = float(input("Geben Sie die Breite des Grundstuecks in Metern ein: "))
        preis_pro_qm = float(input("Geben Sie den Preis pro Quadratmeter ein: "))

        # Plausibilitaetspruefung: Sicherstellen, dass die Eingaben positiv sind
        if laenge <= 0 or breite <= 0 or preis_pro_qm <= 0:
            print("\nFehler: Laenge, Breite und Preis muessen positive Zahlen sein.")
            return

        
        # Berechnungen
        # 1. Grundpreis berechnen
        flaeche = laenge * breite
        grundpreis = flaeche * preis_pro_qm

        # 2. Provision auf den Grundpreis aufschlagen
        provision = PROVISION_SATZ * grundpreis
        preis_mit_provision = grundpreis + provision 

        # 3. Mehrwertsteuer auf den Preis inkl. Provision aufschlagen
        mehrwertsteuer = MWST_SATZ * preis_mit_provision
        endpreis = preis_mit_provision + mehrwertsteuer 

        
        # Ausgabe der Ergebnisse
        print("\n--- Ergebnisse der Grundstuecksberechnung ---")
        
        # 1. Grundpreis (Preis des Grundstuecks)
        print(f"Grundpreis (ohne Provision und MwSt.): {grundpreis:,.2f} €")
        
        # 5% Provision
        print(f"5% Provision: {provision:,.2f} €")
        
        # 2. Preis inkl. Provision (Erster geforderter Preis)
        print(f"Preis des Grundstuecks inkl. 5% Provision: {preis_mit_provision:,.2f} €")
        
        # 19% Mehrwertsteuer
        print(f"19% Mehrwertsteuer: {mehrwertsteuer:,.2f} €")
        
        # 3. Endgueltiger Preis (inkl. Provision und MwSt.) (Zweiter geforderter Preis)
        print(f"Endgueltiger Preis (inkl. Provision und MwSt.): {endpreis:,.2f} €")

    except ValueError:
        print("\nEingabefehler. Bitte geben Sie nur gueltige Zahlen ein.")

# Programmstart
if __name__ == "__main__":
    berechne_grundstueckspreis()