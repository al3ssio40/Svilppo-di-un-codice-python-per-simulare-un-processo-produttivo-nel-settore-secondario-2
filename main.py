import random

# Funzione 1: genera quantità casuali per almeno 3 prodotti
def genera_quantita_prodotti(n=3):
    prodotti = {}
    for i in range(n):
        nome = f"Prodotto_{i+1}"
        quantita = random.randint(50, 500)  # quantità richiesta (casuale)
        prodotti[nome] = {"quantita": quantita}
    return prodotti

# Funzione 2: genera parametri casuali per ogni prodotto
def genera_parametri(prodotti):
    for nome, dati in prodotti.items():
        # tempo di produzione per unità in minuti (tra 1 e 10)
        dati["tempo_unitario"] = random.randint(1, 10)
        # capacità giornaliera (pezzi che si riescono a produrre in un giorno)
        dati["capacita_giornaliera"] = random.randint(100, 400)
    return prodotti

# Funzione 3: calcola tempo totale di produzione (in giorni e ore)
def calcola_tempo_totale(prodotti):
    tempo_totale_min = 0
    for nome, dati in prodotti.items():
        q = dati["quantita"]
        t_unit = dati["tempo_unitario"]
        tempo_totale_min += q * t_unit  # tempo totale in minuti
    
    # output in ore e giorni (approssimati)
    ore = tempo_totale_min / 60
    giorni = ore / 8  # ipotesi: 1 giornata lavorativa = 8 ore
    return tempo_totale_min, ore, giorni

# MAIN
if __name__ == "__main__":
    prodotti = genera_quantita_prodotti(3)
    prodotti = genera_parametri(prodotti)

    print("=== Parametri generati ===")
    for nome, dati in prodotti.items():
        print(f"{nome}: Quantità={dati['quantita']} pezzi, "
              f"Tempo unitario={dati['tempo_unitario']} min, "
              f"Capacità giornaliera={dati['capacita_giornaliera']} pezzi")

    tempo_min, ore, giorni = calcola_tempo_totale(prodotti)

    print("\n=== Risultato ===")
    print(f"Tempo totale di produzione: {tempo_min} minuti "
          f"({ore:.2f} ore ≈ {giorni:.2f} giorni lavorativi)")
