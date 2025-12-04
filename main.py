import random

# ================================
# FUNZIONI DI BASE
# ================================

def genera_quantita_prodotti(n=3):
    prodotti = {}
    for i in range(n):
        nome = f"Prodotto_{i+1}"
        quantita = random.randint(50, 500)
        prodotti[nome] = {"quantita": quantita}
    return prodotti


def genera_parametri(prodotti):
    for nome, dati in prodotti.items():

        dati["tempo_unitario"] = random.randint(1, 10)
        dati["capacita_giornaliera"] = random.randint(100, 400)

        # **NUOVO: percentuale difetti**
        dati["percentuale_difetti"] = random.uniform(0.01, 0.10)

        # **NUOVO: tempo guasti (minuti al giorno)**
        dati["guasti_min"] = random.randint(30, 180)

        # **NUOVO: tempo di setup iniziale (minuti)**
        dati["tempo_setup"] = random.randint(15, 60)

        # **NUOVO: tasso di scarto dopo controlli qualità**
        dati["scarto_post_controllo"] = random.uniform(0.005, 0.03)

    return prodotti


# ================================
# CALCOLO TEMPO COMPLESSIVO
# ================================

def calcola_tempo_totale(prodotti):
    tempo_totale_min = 0
    
    for nome, dati in prodotti.items():

        q = dati["quantita"]      

        # **APPLICAZIONE DIFETTI**
        q = q * (1 + dati["percentuale_difetti"])

        # **APPLICAZIONE SCARTI POST-CONTROLLO**
        q = q * (1 + dati["scarto_post_controllo"])

        # **TEMPO DI PRODUZIONE**
        tempo_produzione = q * dati["tempo_unitario"]

        # **TEMPO GUASTI + SETUP**
        tempo_guasti = dati["guasti_min"] + dati["tempo_setup"]

        tempo_totale_min += tempo_produzione + tempo_guasti

    ore = tempo_totale_min / 60
    giorni = ore / 8
    return tempo_totale_min, ore, giorni


# ================================
# STAMPA DATI PRODOTTO
# ================================

def stampa_parametri(prodotti):
    print("=== Parametri generati per prodotto ===")
    for nome, p in prodotti.items():
        print(
            f"{nome}: "
            f"Q={p['quantita']} pezzi | "
            f"T_unit={p['tempo_unitario']} min | "
            f"Cap={p['capacita_giornaliera']} pezzi/g | "
            f"**Difetti={p['percentuale_difetti']:.1%} | "
            f"Scarti QC={p['scarto_post_controllo']:.1%} | "
            f"Guasti={p['guasti_min']} min | "
            f"Setup={p['tempo_setup']} min**"
        )
    print("\n")


# ================================
# CONFRONTO SCENARI
# ================================

def crea_scenario(miglioramento=False):

    prodotti = genera_parametri(genera_quantita_prodotti(3))

    if miglioramento:
        for p in prodotti.values():
            # **NUOVO: applico miglioramenti (strategia Industria 4.0)**
            p["percentuale_difetti"] *= 0.5
            p["scarto_post_controllo"] *= 0.5
            p["guasti_min"] *= 0.5
            p["tempo_setup"] *= 0.5

    return prodotti


def confronta_scenari():

    print("\n========== SCENARIO A (Baseline) ==========")
    baseline = crea_scenario(miglioramento=False)
    stampa_parametri(baseline)
    min_a, ore_a, giorni_a = calcola_tempo_totale(baseline)
    print(f"Tempo Totale Scenario A = {giorni_a:.2f} giorni\n")

    print("========== SCENARIO B (Miglioramento tecnologico: 4.0) ==========")
    migliorato = crea_scenario(miglioramento=True)
    stampa_parametri(migliorato)
    min_b, ore_b, giorni_b = calcola_tempo_totale(migliorato)
    print(f"Tempo Totale Scenario B = {giorni_b:.2f} giorni\n")

    print("========== CONFRONTO ==========")
    print(f"Riduzione % = {((giorni_a - giorni_b) / giorni_a * 100):.1f}%")
    print(f"Giorni risparmiati = {giorni_a - giorni_b:.2f} giorni")


# ================================
# MAIN
# ================================

if __name__ == "__main__":
    confronta_scenari()
