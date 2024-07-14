import psycopg2 as pg
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


class Artikli:
    """Data manipulation from the 'artikli' table."""
    
    def __init__(self):
        self.con = pg.connect(
            database="picerija_porucivanje",
            user="postgres",
            password="pg11kdk",
            host="localhost",
            port="5433"
        )
        self.artikli_df = None
    
    def artikli_ucitavanje(self):
        """Refreshing the 'artikli' table data."""
        
        self.artikli_df = pd.read_sql_query("SELECT * FROM artikli", self.con)
    
    def azuriranje_kolicine(self, nova_kolicina, naziv_stavke):
        """Updating item quantities."""

        cursor = self.con.cursor()

        kolicina_update_sql = f"""
                                UPDATE artikli
                                SET kolicina = {nova_kolicina}
                                WHERE naziv = '{naziv_stavke}'
                                """

        cursor.execute(kolicina_update_sql)
        self.con.commit()
        cursor.close()
        
        self.artikli_ucitavanje()
    
    def visina_cena_artikala(self, cene_silazno=True):
        """Display of articles with the highest and lowest individual
        prices."""

        sortirano_najvise = self.artikli_df.sort_values(by=['cena'],
            ascending=False).head(10)
        sortirano_najnize = self.artikli_df.sort_values(
            by=['cena']).head(10)

        if cene_silazno:
            artikli_lista = sortirano_najvise.naziv.to_list()
            cene_lista = sortirano_najvise.cena.to_list()
            boja_naslova = "navy"
            boja_markera = "cornflowerblue"
            boja_linija = "mediumblue"
            stil_linije = ":"
            deo_teksta_naslov = "najvišim"
            ylabel_tekst = "Najviše cene"
        else:
            artikli_lista = sortirano_najnize.naziv.to_list()
            cene_lista = sortirano_najnize.cena.to_list()
            boja_naslova = "indigo"
            boja_markera = "plum"
            boja_linija = "darkviolet"
            stil_linije = "-."
            deo_teksta_naslov = "najnižim"
            ylabel_tekst = "Najniže cene"

        # Chart
        plt.figure(figsize=(10, 7))

        plt.plot(artikli_lista, cene_lista, marker="o", color=boja_linija,
                 markerfacecolor=boja_markera, linestyle=stil_linije)
        plt.title(
            f"Artikli s {deo_teksta_naslov} cenama".upper(),
            fontdict={"family": "Calibri", "color": boja_naslova, "size": 20,
                      "weight": "bold"})
        plt.xlabel("Nazivi artikala")
        plt.ylabel(ylabel_tekst)
        plt.xticks(rotation=80)
        plt.grid()
        plt.subplots_adjust(bottom=0.3)

        plt.show()


class Porudzbine:
    """Data manipulation from the 'porudzbine' table."""

    def __init__(self):
        self.con = pg.connect(
            database="picerija_porucivanje",
            user="postgres",
            password="pg11kdk",
            host="localhost",
            port="5433"
        )
        self.porudzbine_df = None

    def porudzbine_ucitavanje(self):
        """Refreshing the 'porudzbine' table data."""
    
        self.porudzbine_df = pd.read_sql_query("SELECT * FROM porudzbine",
                                               self.con)

    def porudzbine_ubacivanje_podataka(self, sifra_por, entry_adresa,
                                       entry_telefon, var_placanje, rb_dict,
                                       cena):
        """Inserting data in the 'porudzbine' table."""
    
        cursor = self.con.cursor()
        
        for (key, val) in rb_dict.items():
            if val == var_placanje.get():
                nacin_placanja = key
        
        tekuci_status = "Kreirana"
    
        porudzbine_sql = f"INSERT INTO porudzbine (sifra, adresa, telefon, " \
                         f"placanje, status, ukupno) VALUES ('{sifra_por}', " \
                         f"'{entry_adresa.get()}', '{entry_telefon.get()}', " \
                         f"'{nacin_placanja}', '{tekuci_status}', '{cena}');"
        
        cursor.execute(porudzbine_sql)
        self.con.commit()
    
        cursor.close()
    
        self.porudzbine_ucitavanje()
    
    def promena_statusa(self, sifra_cb_vrednost, status_cb_vrednost):
        """Changing the old status to a new one."""

        cursor = self.con.cursor()
        
        promena_statusa_sql = f"""
        UPDATE porudzbine
        SET status = '{status_cb_vrednost}'
        WHERE sifra = '{sifra_cb_vrednost}'
        """

        cursor.execute(promena_statusa_sql)
        self.con.commit()

        cursor.close()

        self.porudzbine_ucitavanje()
    
    def visina_cena_porudzbina(self, visina_cene=True):
        """The highest and lowest prices of individual orders and their
        graphic display."""
        
        sortirano_najvise = self.porudzbine_df.sort_values(
            by=['ukupno'], ascending=False).head()
        sortirano_najnize = self.porudzbine_df.sort_values(
            by=['ukupno']).head()
        
        if visina_cene:
            sifre_lista = sortirano_najvise.sifra.to_list()
            cene_lista = sortirano_najvise.ukupno.to_list()
            boja_stubaca = "crimson"
            boja_naslova = "maroon"
            deo_teksta_naslov = "najvišim"
            ylabel_tekst = "Najviše cene porudžbina"
        else:
            sifre_lista = sortirano_najnize.sifra.to_list()
            cene_lista = sortirano_najnize.ukupno.to_list()
            boja_stubaca = "yellowgreen"
            boja_naslova = "olive"
            deo_teksta_naslov = "najnižim"
            ylabel_tekst = "Najniže cene porudžbina"
        
        # Chart
        plt.figure(figsize=(10, 7))
        
        plt.bar(sifre_lista, cene_lista, color=boja_stubaca)
        plt.title(
            f"Porudžbine s {deo_teksta_naslov} cenama".upper(),
            fontdict={"family": "Calibri", "color": boja_naslova, "size":
                18, "weight": "bold"}
        )
        plt.xlabel("Šifre porudžbina")
        plt.ylabel(ylabel_tekst)
        plt.xticks(rotation=60)
        plt.grid()
        plt.subplots_adjust(bottom=0.2)
        
        plt.show()


class Stavke:
    """Data manipulation from the 'stavke' table, which gives details of
    individual orders."""
    
    def __init__(self):
        self.con = pg.connect(
            database="picerija_porucivanje",
            user="postgres",
            password="pg11kdk",
            host="localhost",
            port="5433"
        )
        self.stavke_df = None
    
    def stavke_ucitavanje(self):
        """Refreshing the 'stavke' table data."""
        
        self.stavke_df = pd.read_sql_query("SELECT * FROM stavke", self.con)

    def stavke_ubacivanje_podataka(self, sifra_por, stavke_spisak):
        """Inserting date in the 'stavke' table."""
    
        cursor = self.con.cursor()
        
        for i in range(len(stavke_spisak)):
            broj_komada = stavke_spisak[i][0]
            izabrana_stavka = stavke_spisak[i][1]
    
            stavke_sql = f"INSERT INTO stavke (sifra, stavka, komada) VALUES" \
                         f" ('{sifra_por}', '{izabrana_stavka}', " \
                         f"'{broj_komada}');"
    
            cursor.execute(stavke_sql)
            self.con.commit()
        
        cursor.close()
    
        self.stavke_ucitavanje()
    
    def najprodavaniji_artikli(self, broj_prvih_artikala):
        """Graphic representation of the best-selling items."""
        
        # All items that have been sold
        prodavani_artikli = set(self.stavke_df.stavka.to_list())
        
        # Getting how many times individual items have been sold and sorting
        # by that criteria
        prodavani_dict = {}
        for artikal in prodavani_artikli:
            prodato_komada = self.stavke_df.komada[
                self.stavke_df.stavka == artikal].to_list()
            
            ukupno_prodato = 0
            for i in range(len(prodato_komada)):
                ukupno_prodato += prodato_komada[i]
            
            prodavani_dict[artikal] = ukupno_prodato
        sortirano_po_prodaji = dict(Counter(prodavani_dict).most_common())
        
        # A list of the best-selling items and a list of how many times they
        # have been sold
        artikli_lst = []
        komada_lst = []
        for key, value in sortirano_po_prodaji.items():
                artikli_lst.append(key)
                komada_lst.append(value)
        prvih_x_artikala = artikli_lst[:broj_prvih_artikala]
        prvih_x_komada = komada_lst[:broj_prvih_artikala]
        
        # Chart
        plt.figure(figsize=(10, 7))
        
        plt.barh(prvih_x_artikala, prvih_x_komada, color="darkred")
        plt.title(
            f"Najprodavaniji artikli - prvih {broj_prvih_artikala}".upper(),
            fontdict={"family": "Calibri", "color": "navy", "size": 20,
                      "weight": "bold"}
        )
        plt.xlabel("Naziv artikla")
        plt.ylabel("Broj prodaje")
        plt.grid()
        plt.subplots_adjust(left=0.24, right=0.95)
        
        plt.show()
    
    def artikal_najveci_prihod(self):
        """Graphic representation of the items that provided the highest
        income"""

        # All items that have been sold
        prodavani_artikli = set(self.stavke_df.stavka.to_list())

        # Getting the number of individual items sold
        prodavani_dict = {}
        for artikal in prodavani_artikli:
            prodato_komada = self.stavke_df.komada[
                self.stavke_df.stavka == artikal].to_list()
    
            ukupno_prodato = 0
            for i in range(len(prodato_komada)):
                ukupno_prodato += prodato_komada[i]

            prodavani_dict[artikal] = ukupno_prodato
        
        # Getting income from each item sold
        artikli_prihod_dict = {}
        for key, value in prodavani_dict.items():
            cena_artikla = int(artikli.artikli_df.cena[
                artikli.artikli_df.naziv == key].to_string(index=False))
            prihod_artikla = cena_artikla * value
            
            artikli_prihod_dict[key] = prihod_artikla

        sortirano_po_prihodu = dict(Counter(artikli_prihod_dict).most_common())
        
        # List of the highest income items and list of their income
        naziv_lst = []
        prihod_lst = []
        for key, value in sortirano_po_prihodu.items():
            naziv_lst.append(key)
            prihod_lst.append(value)
         
        prvi_artikli = naziv_lst[:5]
        prvi_prihodi = prihod_lst[:5]
        
        # Amount of all other income combined (excluding the top 5)
        lista_ostalih_prihoda = prihod_lst[5:]
        
        ostali_prihodi_zajedno = 0
        for prihod in lista_ostalih_prihoda:
            ostali_prihodi_zajedno += prihod
        
        # Chart
        prvi_artikli.append("Svi ostali")
        prvi_prihodi.append(ostali_prihodi_zajedno)

        plt.figure(figsize=(8, 8))
        
        plt.pie(
            prvi_prihodi,
            labels=prvi_artikli,
            autopct="%1.1f%%",
            colors=["tomato", "cornflowerblue", "yellowgreen", "orchid",
                    "gold", "burlywood"],
            startangle=90,
            explode=[0.12, 0, 0, 0, 0, 0]
        )
        plt.title(
            label="Najveći prihod po artiklu i ostali prihodi zajedno".upper(),
            fontdict={"fontsize": 20, "weight": "bold", "family": "Calibri",
                      "color": "dimgray"},
            pad=20
        )
        plt.subplots_adjust(bottom=0)
        
        plt.show()


class Transakcije:
    """Data manipulation from the 'transakcije' table."""
    
    def __init__(self):
        self.con = pg.connect(
            database="picerija_porucivanje",
            user="postgres",
            password="pg11kdk",
            host="localhost",
            port="5433"
        )
        self.transakcije_df = None
    
    def transakcije_ucitavanje(self):
        """Refreshing the 'transakcije' table data."""
        
        self.transakcije_df = pd.read_sql_query("SELECT * FROM transakcije",
                                                self.con)
    
    def transakcije_ubacivanje_podataka(self, entry_ime, entry_racun,
                                        ukupno, sifra_por):
        """Inserting data in the 'transakcije' table."""
        
        cursor = self.con.cursor()

        transakcija_sql = f"INSERT INTO transakcije (uplatilac, " \
                          f"racun, iznos, sifra) VALUES (" \
                          f"'{entry_ime.get()}', '{entry_racun.get()}', " \
                          f"'{ukupno}', '{sifra_por}');"

        cursor.execute(transakcija_sql)
        self.con.commit()
        cursor.close()
        
        self.transakcije_ucitavanje()


artikli = Artikli()
artikli.artikli_ucitavanje()
porudzbine = Porudzbine()
porudzbine.porudzbine_ucitavanje()
stavke = Stavke()
stavke.stavke_ucitavanje()
transakcije = Transakcije()
transakcije.transakcije_ucitavanje()
