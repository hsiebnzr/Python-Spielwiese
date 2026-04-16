print("Willkommen zum Trinkgeld Rechner")
Gesamtkosten = float(input("Was waren die Gesamtkosten? \n€"))
Trinkgeld = float(input("Was möchten Sie an Trinkgeld zahlen? 10 20 30\n%"))
Personen = int(input("Auf wie viele Personen wollen Sie es aufteilen?\n"))

Prozent_Trinkgeld = Trinkgeld / 100

Gesamt_Trinkgeld = Gesamtkosten * Prozent_Trinkgeld

Insgesamt = (float(((Gesamtkosten + Gesamt_Trinkgeld) / Personen)))

print(f"Jeder sollte am Ende so viel zahlen: {Insgesamt:.2f} €")