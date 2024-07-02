from porudzbine import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint, choice
from podaci import *
from PIL import ImageTk, Image
import textwrap

root = Tk()
root.title("Picerija \"Monty Python\"")
root.geometry("610x870")
root.resizable(0, 0)

# Stil za velika slova na glavnom ekranu.
style_btn = ttk.Style()
style_btn.configure("velika.TButton", font=("Calibri", 18, "bold"))
style_btn.map(
    "velika.TButton",
    foreground=[("pressed", "darkblue"), ("active", "maroon"),
                ("!disabled", "royalblue")]
)

# Stil za okvir na glavnom ekranu.
style_frm = ttk.Style()
style_frm.configure("okvir.TFrame", background="gainsboro")

# Stil za Radiobutton.
rb_style = ttk.Style()
rb_style.configure("sb.TRadiobutton", font=("Calibri", 14))

# Stil za Radiobutton sa sivom pozadinom.
rb_gray = ttk.Style()
rb_gray.configure("gray.TRadiobutton", font=("Calibri", 14),
                  background="gainsboro")

# Stil za LabelFrame.
style_lf = ttk.Style()
style_lf.configure("lblfrm.TLabelframe")
style_lf.configure("lblfrm.TLabelframe.Label", foreground="navy",
                   font=("Calibri", 14))


def len_char_limit(inp):
    """Ograničavanje broja i vrste karaktera (samo brojevi)."""
    
    if inp.isdigit() and len(inp) <= 10:
        return True
    elif inp == "":
        return True
    else:
        return False


def validacija_unosa(unos):
    """Validacija numeričkog unosa u spinbox polja."""
    return unos.isdigit()


def sirina_visina(widget):
    """Dobijanje širine i visine nekog od elemenata."""
    
    widget.update()
    sirina = widget.winfo_width()
    visina = widget.winfo_height()
    
    return sirina, visina


def artikli_sastavi_cene(kategorija="Pice"):
    """Dobijanje lista artikala, njihovog sastava i njihovih cena po
    kategorijama."""
    
    # Rečnik s kategorijama u koje smo podelili artikle.
    kategorije_dict = {
        "Pice": ["pica"],
        "Salate": ["salata"],
        "Sendviči": ["sendvič"],
        "Deserti": ["desert"],
        "Napici": ["sok", "pivo", "voda", "jogurt", "ceđeno voće"]
    }

    lista_artikala = []
    for stavka in kategorije_dict[kategorija]:
        odabrano = artikli.artikli_df.naziv[
            artikli.artikli_df.vrsta == stavka].tolist()
        privremena_lista = sorted(odabrano)
        lista_artikala += privremena_lista
    
    lista_sastava = []
    lista_cena = []
    for i in range(len(lista_artikala)):
        # Dobijanje celog teksta za u koloni 'sastav'.
        sastav_artikla = "\n".join(artikli.artikli_df.sastav[
                                         artikli.artikli_df.naziv ==
                                         lista_artikala[i]])
        lista_sastava.append(sastav_artikla)
        
        cena_artikla = artikli.artikli_df.cena[
            artikli.artikli_df.naziv ==
            lista_artikala[i]].to_string(index=False)
        lista_cena.append(cena_artikla)
    
    return lista_artikala, lista_sastava, lista_cena


def prelom(text, length=60):
    """Prelamanje dugačkog teksta kako bi ceo mogao da bude vidljiv."""
    
    return '\n'.join(textwrap.wrap(text, length))


def generisanje_sifre():
    """Generisanje šifre porudžbine, uz proveru da li takva već postoji."""
    
    sifre_lst = porudzbine.porudzbine_df.sifra.to_list()
    
    # Generisanje šifre.
    sifra = ""
    for i in range(10):
        cifra = randint(0, 9)
        sifra += str(cifra)
    
    if sifra in sifre_lst:
        generisanje_sifre()
    else:
        return sifra


def zatvaranje():
    """Otvaranje messagebox prozora za potvrdu zatvaranja aplikacije."""
    pitanje = messagebox.askyesno(
        title="Zatvaranje aplikacije",
        message="Da li želite da izađete iz aplikacije?"
    )
    if pitanje:
        root.destroy()


def prikaz_artikala():
    """Prikazivanje svih artikala po kategorijama (kolona 'vrsta')."""
    
    meni_tl = Toplevel(root)
    meni_tl.title("Meni picerije \"Monty Python\"")
    meni_tl.attributes("-topmost", "true")
    meni_tl.resizable(0, 0)
    meni_tl.geometry("920x800")
    meni_tl.grab_set()
    
    def uklanjanje_elemenata():
        """Uklanjanje svih elemenata sa okvira koji je na kanvasa i
        vraćanje na početnu poziciju."""
        
        for widget in meni_frm.winfo_children():
            widget.destroy()
        meni_canvas.yview_moveto(0.0)

    def izbor_prikaza(kategorija="Pice"):
        """U zavisnosti od pritiska na dugme u sidebaru prikazuje se samo ta
         vrsta artikala."""
        
        liste = artikli_sastavi_cene(kategorija)

        # Kreiranje elemenata na formi.
        meni_naslov = ttk.Label(
            meni_frm,
            text="Meni picerije \"Monty Python\"",
            background="royalblue",
            foreground="white",
            font=("Calibri", 32, "bold"),
            anchor=CENTER
        )
        meni_naslov.grid(column=0, row=0, columnspan=3, pady=20, sticky=EW)

        artikli_lbl = ttk.Label(
            meni_frm,
            text=kategorija,
            background="orange",
            foreground="white",
            font=("Calibri", 28, "bold"),
            anchor=CENTER
        )
        artikli_lbl.grid(column=0, row=1, columnspan=3, ipadx=10, ipady=5,
                         sticky=EW)

        for i in range(len(liste[0])):
            ttk.Label(
                meni_frm,
                text=liste[0][i],
                font=("Calibri", 16, "bold"),
                foreground="royalblue"
            ).grid(column=0, row=i + 2, padx=10, pady=10, sticky=W)
        
            ttk.Label(
                meni_frm,
                text=liste[1][i],
                wraplength=350,
                font=("Calibri", 14),
                foreground="royalblue"
            ).grid(column=1, row=i + 2, padx=10, pady=10, sticky=W)
    
            ttk.Label(
                meni_frm,
                text=liste[2][i],
                font=("Calibri", 16, "bold")
            ).grid(column=2, row=i + 2, padx=10, pady=10, sticky=E)
            
            meni_poruci_btn = ttk.Button(
                meni_frm,
                text="Poruči",
                style="velika.TButton",
                command=lambda : [meni_tl.destroy(), porucivanje()]
            )
            meni_poruci_btn.grid(column=0, row=len(liste[0]) + 3,
                                 pady=30, sticky=E)

            meni_izadji_btn = ttk.Button(
                meni_frm,
                text="Izađi",
                style="velika.TButton",
                command=meni_tl.destroy
            )
            meni_izadji_btn.grid(column=1, row=len(liste[0]) + 3,
                                 pady=30, sticky=E)
    
    def podesavanje_skrolbara():
        """Postavljanje skrolbara i oblasti za skrolovanje za prikaz nove
        kategorije artikala."""
        
        sirina_okvira = sirina_visina(meni_frm)[0]
        visina_okvira = sirina_visina(meni_frm)[1]
        
        if visina_okvira >= meni_tl.winfo_height():
            meni_canvas.bind_all(
                "<MouseWheel>",
                lambda event: meni_canvas.yview_scroll(-int(event.delta / 60),
                                                       "units"))
            meni_canvas.configure(
                yscrollcommand=meni_sb.set,
                scrollregion=(0, 0, sirina_okvira, visina_okvira)
            )
            meni_sb.place(relx=1, rely=0, relheight=1, anchor=NE)
        else:
            meni_canvas.unbind_all("<MouseWheel>")
            meni_sb.place_forget()

    # Sidebar.
    sidebar_style = ttk.Style()
    sidebar_style.configure("sb.TFrame", background="orange")

    sidebar_frm = ttk.Frame(meni_tl, style="sb.TFrame")
    sidebar_frm.pack(side=LEFT, expand=False, fill=BOTH)

    sidebar_lbl = ttk.Label(
        sidebar_frm,
        text="MENI",
        background="orange",
        foreground="navy",
        font=("Calibri", 24, "bold")
    )
    sidebar_lbl.grid(column=0, row=0, padx=50, pady=30)

    # Dugmad za prikaz vrste artikla na sidebaru.
    sb_pice_btn = ttk.Button(
        sidebar_frm,
        text="Pice",
        style="velika.TButton",
        command=lambda : [
            uklanjanje_elemenata(),
            izbor_prikaza(sb_pice_btn.cget("text")),
            podesavanje_skrolbara()
        ]
    )
    sb_pice_btn.grid(column=0, row=1, padx=30, pady=5, sticky=N)
    sb_salate_btn = ttk.Button(
        sidebar_frm,
        text="Salate",
        style="velika.TButton",
        command=lambda: [
            uklanjanje_elemenata(),
            izbor_prikaza(sb_salate_btn.cget("text")),
            podesavanje_skrolbara()
        ]
    )
    sb_salate_btn.grid(column=0, row=2, padx=30, pady=5, sticky=N)
    sb_sendvici_btn = ttk.Button(
        sidebar_frm,
        text="Sendviči",
        style="velika.TButton",
        command=lambda: [
            uklanjanje_elemenata(),
            izbor_prikaza(sb_sendvici_btn.cget("text")),
            podesavanje_skrolbara()
        ]
    )
    sb_sendvici_btn.grid(column=0, row=3, padx=30, pady=5, sticky=N)
    sb_deserti_btn = ttk.Button(
        sidebar_frm,
        text="Deserti",
        style="velika.TButton",
        command=lambda: [
            uklanjanje_elemenata(),
            izbor_prikaza(sb_deserti_btn.cget("text")),
            podesavanje_skrolbara()
        ]
    )
    sb_deserti_btn.grid(column=0, row=4, padx=30, pady=5, sticky=N)
    sb_napici_btn = ttk.Button(
        sidebar_frm,
        text="Napici",
        style="velika.TButton",
        command=lambda: [
            uklanjanje_elemenata(),
            izbor_prikaza(sb_napici_btn.cget("text")),
            podesavanje_skrolbara()
        ]
    )
    sb_napici_btn.grid(column=0, row=5, padx=30, pady=5, sticky=N)

    # Canvas.
    meni_canvas = Canvas(meni_tl)
    meni_canvas.pack(expand=True, fill=BOTH)
    
    meni_frm = ttk.Frame(meni_canvas)
    meni_canvas.create_window((0, 0), window=meni_frm, anchor=NW)
    meni_frm.configure(padding=(20, 0, 20, 0))

    izbor_prikaza()

    # Scrollbar i povezivanje sa skrolovanjem na mišu:
    meni_sb = ttk.Scrollbar(
        meni_canvas,
        orient="vertical",
        command=meni_canvas.yview
    )

    # Širina i visina okvira
    okvir = sirina_visina(meni_frm)

    meni_canvas.bind_all(
        "<MouseWheel>",
        lambda event: meni_canvas.yview_scroll(-int(event.delta / 60), "units")
    )
    
    meni_canvas.configure(
        yscrollcommand=meni_sb.set,
        scrollregion=(0, 0, okvir[0], okvir[1])
    )
    meni_sb.place(relx=1, rely=0, relheight=1, anchor=NE)


def porucivanje():
    """Kreiranje forma za poručivanje pojedinačnih artikala, prebacivanje u
    korpu i konačno prihvatanje izbora."""
    
    def popunjavanje_tabele(kategorija="Pice"):
        """Popunjavanje Treeview tabele vrednostima za obeleženu kategoriju."""
        
        for item in lista_artikala_tv.get_children():
            lista_artikala_tv.delete(item)
        
        for key, value in rd_buttons.items():
            if kategorija_var.get() == value:
                kategorija = key
        
        tv_podaci = artikli_sastavi_cene(kategorija)
        for i in range(len(tv_podaci[0])):
            lista_artikala_tv.insert(
                parent="",
                index=i,
                values=(tv_podaci[0][i], prelom(tv_podaci[1][i]),
                        tv_podaci[2][i])
            )
        lista_artikala_tv.update()

    def ubaci_u_korpu():
        """Ubacivanje izabranog artikla u korpu."""
        
        id_artikla = lista_artikala_tv.focus()
        
        oznaceni_artikal = lista_artikala_tv.item(id_artikla)
        if not oznaceni_artikal.get("values"):
            messagebox.showinfo(
                title="Nijedan artikal nije označen",
                message="Da bi se bilo što ubacilo u korpu,\npotrebno je "
                        "izabrati neki artikal iz tabele."
            )
        else:
            artikal_i_cena = oznaceni_artikal.get("values")[0], \
                oznaceni_artikal.get("values")[2]
        
            # Toplevel za ubacivanje artikla i njegove količine.
            dodaj_tl = Toplevel(poruci_tl)
            dodaj_tl.title("Dodaj u korpu")
            dodaj_tl.resizable(0, 0)
            dodaj_tl.attributes("-topmost", "true")
            dodaj_tl.grab_set()
            
            dodaj_komada_lbl = ttk.Label(
                dodaj_tl,
                text="komada",
                font="Calibri 12 bold"
            )
            dodaj_komada_lbl.grid(column=0, row=0, padx=10, pady=5)
            
            spin_var = IntVar(value=1)
            dodaj_reg = dodaj_tl.register(validacija_unosa)
            dodaj_spin = ttk.Spinbox(
                dodaj_tl,
                from_=1,
                to=10,
                textvariable=spin_var,
                width=5,
                validate="key",
                validatecommand=(dodaj_reg, "%P")
            )
            dodaj_spin.grid(column=0, row=1, padx=10)
            
            dodaj_naslov_lbl = ttk.Label(
                dodaj_tl,
                text="naziv artikla",
                font="Calibri 12 bold"
            )
            dodaj_naslov_lbl.grid(column=1, row=0, padx=10, pady=5)
            
            dodaj_artikal_lbl = ttk.Label(dodaj_tl, text=artikal_i_cena[0])
            dodaj_artikal_lbl.grid(column=1, row=1, padx=10)
            
            dodaj_btn = ttk.Button(
                dodaj_tl,
                text="Dodaj",
                command=lambda : [stavljanje_u_korpu(), dodaj_tl.destroy()]
            )
            dodaj_btn.grid(column=1, row=2, padx=10, pady=10, sticky=E)
            
        # Stavljanje artikla u korpu i prikazivanje ukupne cene.
        def stavljanje_u_korpu():
            komada = spin_var.get()
            stavka = artikal_i_cena[0]
            cena = artikal_i_cena[1]

            # Količina traženog artikla iz baze podataka.
            kolicina_artikla = int(artikli.artikli_df.kolicina[
                artikli.artikli_df.naziv == stavka].to_string(index=False))
            
            # Provera da li ima dovoljno artikala.
            if komada > kolicina_artikla:
                messagebox.showinfo(
                    title="Nema na stanju",
                    message=f"Artikla '{stavka}' nema dovljno na stanju."
                )
            else:
                korpa_tv.insert("", END, values=[komada, stavka])
                
                dodatna_vrednost = komada * cena
                ranija_vrednost = int(ukupno_iznos_lbl.cget("text")[:-5])
                nova_vrednost = ranija_vrednost + dodatna_vrednost
                
                ukupno_iznos_lbl.configure(text=f"{nova_vrednost} din.")
    
    def brisanje_iz_korpe():
        """Brisanje stavke iz korpe i korekcija ukupne cene."""

        oznacena_stavka = korpa_tv.selection()
        
        if not len(korpa_tv.get_children()):
            messagebox.showinfo(
                title="Korpa je prazna",
                message="Ne može se brisati iz korpe,\n"
                        "kada u njoj nema nijedne stavke."
            )
        elif not oznacena_stavka:
            messagebox.showinfo(
                title="Nijedna stavka nije označena",
                message="Da bi se bilo što izbrisalo iz korpe,\npotrebno je "
                        "izabrati neku stavku iz tabele."
            )
        else:
            # Korekcija ukupne cene.
            komada_stavka = korpa_tv.item(oznacena_stavka).get("values")
            cena_stavke = int(artikli.artikli_df.cena[
                artikli.artikli_df.naziv ==
                komada_stavka[1]].to_string(index=False))
            
            umanjenje = cena_stavke * komada_stavka[0]
            korigovano = int(ukupno_iznos_lbl.cget("text")[:-5]) - umanjenje
            ukupno_iznos_lbl.configure(text=f"{korigovano} din.")
            
            # Brisanje stavke
            korpa_tv.delete(oznacena_stavka)
    
    def izbor_placanja():
        """Forma za izbor plaćanja, uz detalja o porudžbini."""
        
        def online_placanje():
            """Otključvanje i zaključavanje polja potrebnih za online
            plaćanje."""
            if placanje_var.get() == "3":
                ime_ent.configure(state="enabled")
                racun_ent.configure(state="enabled")
                pin_ent.configure(state="enabled")
                generisi_btn.configure(state="enabled")
            else:
                ime_ent.configure(state="disabled")
                racun_ent.configure(state="disabled")
                pin_ent.configure(state="disabled")
                generisi_btn.configure(state="disabled")
        
        def generisanje_podataka():
            """Generisanje podataka iz fajla 'podaci', koji se upisuju u
            polja za online plaćanje."""
            
            # Podaci za upis.
            podaci = choice(IME_RACUN_PIN_SREDSTVA)
            gen_ime = podaci[0]
            gen_racun = podaci[1]
            gen_pin = podaci[2]
            
            # Ubacivanje podataka u polja za online plaćanje.
            ime_ent.delete(0, END)
            ime_ent.insert(0, gen_ime)
            racun_ent.delete(0, END)
            racun_ent.insert(0, gen_racun)
            pin_ent.delete(0, END)
            pin_ent.insert(0, gen_pin)
            
        
        def realizacija_porudzbine():
            """Zaključivanje i kreiranje porudžbine, provera da li su sva
            polja popunjena i ubacivanje podataka u tabele."""

            # Provera popunjenosti polja.
            if not adresa_ent.get():
                messagebox.showinfo(
                    title="Nedostaje adresa",
                    message="Adresa isporuke nije upisana."
                )
            elif not telefon_ent.get():
                messagebox.showinfo(
                    title="Nedostaje telefon",
                    message="Kontakt telefon nije upisan."
                )
            else:
                prvi_deo_poruke = "Vaša porudžbina je kreirana."
                ispravni_podaci = []

                if placanje_var.get() == "3":
                    prvi_deo_poruke = "Transakcija je uspešno izvršena.\n" \
                                      "Vaša porudžbina je kreirana."
                    
                    if not ime_ent.get():
                        messagebox.showinfo(
                            title="Nedostaju ime i prezime",
                            message="Prilikom online plaćanja\npotrebno je "
                                    "uneti ime i prezime platioca."
                        )
                    elif not racun_ent.get():
                        messagebox.showinfo(
                            title="Nedostaje broj računa",
                            message="Prilikom online plaćanja\nneophodno je "
                                    "uneti ime računa s platne kartice."
                        )
                    elif not pin_ent.get():
                        messagebox.showinfo(
                            title="Nedostaje PIN",
                            message="Prilikom online plaćanja\nneophodno je "
                                    "uneti PIN\nkoji služi za proveru "
                                    "autentičnosti."
                        )
                    else:
                        ispravno_ime = False
                        ispravni_podaci = []
                        for i in range(len(IME_RACUN_PIN_SREDSTVA)):
                            if ime_ent.get() == IME_RACUN_PIN_SREDSTVA[i][0]:
                                ispravno_ime = True
                                ispravni_podaci = IME_RACUN_PIN_SREDSTVA[i]
                        
                        if not ispravno_ime or racun_ent.get() != \
                                ispravni_podaci[1]:
                            messagebox.showinfo(
                                title="Neslaganje podataka",
                                message="Ime i prezime platioca i njegov "
                                        "račun se ne slažu."
                            )
                        elif pin_ent.get() != ispravni_podaci[2]:
                            messagebox.showinfo(
                                title="Neslaganje podataka",
                                message="Uneseni PIN nije ispravan."
                            )
                        
                    # Provera da uplatilac ima dovoljno sredstava na računu.
                    for i in range(len(IME_RACUN_PIN_SREDSTVA)):
                        if ime_ent.get() == IME_RACUN_PIN_SREDSTVA[i][0]:
                            sredstva_na_racunu = IME_RACUN_PIN_SREDSTVA[i][3]
                            
                    if ukupna_cena > sredstva_na_racunu:
                        messagebox.showinfo(
                            title="Nedovljno sredstava",
                            message="Na računu nema dovoljno "
                                    "sredstava!\n\nIzaberite drugi način "
                                    "plaćanja ili otkažite porudžbinu."
                        )
                        return
                
                # Skidanje artikala sa stanja.
                for i in range(broj_stavki):
                    kolicina_iz_tabele = int(artikli.artikli_df.kolicina[
                        artikli.artikli_df.naziv == spisak_stavki[i][
                            1]].to_string(index=False))
                    
                    novo_stanje = kolicina_iz_tabele - spisak_stavki[i][0]
                    artikli.azuriranje_kolicine(novo_stanje, spisak_stavki[
                        i][1])
                        
                
                # Ubacivanje podataka u tabele.
                # Tabela 'transakcije'.
                if ispravni_podaci and placanje_var.get() == "3":
                    transakcije.transakcije_ubacivanje_podataka(
                        ime_ent, racun_ent, ukupna_cena, sifra_porudzbine)
                
                # Tabela 'porudzbine'.
                porudzbine.porudzbine_ubacivanje_podataka(
                    sifra_porudzbine, adresa_ent, telefon_ent, placanje_var,
                    izbor_rb, ukupna_cena)
                
                # Tabela 'stavke'.
                stavke.stavke_ubacivanje_podataka(sifra_porudzbine,
                                                  spisak_stavki)
                
                # Zatvaranje forme za unos podataka potrebnih za porudžbinu.
                izbor_tl.destroy()
                
                # Brisanje stavki iz korpe.
                for i in korpa_tv.get_children():
                    korpa_tv.delete(i)
                poruci_tl.update()
                
                # Vraćanje vrednosti ukupnog iznosa na nulu.
                ukupno_iznos_lbl.configure(text="0 din.")
                
                # Obaveštenje o kreiranoj porudžbini.
                drugi_deo_poruke = f"Šifra za praćenje porudžbine je:\n" \
                                   f"{sifra_porudzbine}"
                treci_deo_poruke = "Dostava uskoro stiže.\n\nPRIJATNO!"
                poruka = f"{prvi_deo_poruke}\n\n{drugi_deo_poruke}\n\n" \
                         f"{treci_deo_poruke}"
                
                obavestenje_tl = Toplevel(poruci_tl)
                obavestenje_tl.title("Porudžbina")
                obavestenje_tl.attributes("-topmost", "true")
                obavestenje_tl.resizable(0, 0)
                obavestenje_tl.grab_set()
                
                obavestenje_frm = ttk.Frame(obavestenje_tl, relief="ridge",
                                            style="okvir.TFrame")
                obavestenje_frm.pack(expand=True, fill=BOTH, padx=10, pady=10)
                
                
                obavestenje_lbl = ttk.Label(
                    obavestenje_frm,
                    text=poruka,
                    foreground="navy",
                    background="gainsboro",
                    font=("Calibri", 18, "bold")
                )
                obavestenje_lbl.pack(anchor=CENTER, padx=20, pady=20)
                
                obavestenje_btn = ttk.Button(
                    obavestenje_frm,
                    text="Zatvori",
                    style="velika.TButton",
                    command=obavestenje_tl.destroy
                )
                obavestenje_btn.pack(anchor=E, padx=20, pady=20)
        
        broj_stavki = len(korpa_tv.get_children())
        
        if not broj_stavki:
            messagebox.showinfo(
                title="Korpa je prazna",
                message="Nema nijedne stavke u korpi."
            )
        else:
            izbor_tl = Toplevel(poruci_tl)
            izbor_tl.title("Izbor plaćanja")
            izbor_tl.resizable(0, 0)
            izbor_tl.grab_set()
            
            izbor_placanja_naslov = ttk.Label(
                izbor_tl,
                text="Picerija \"Monty Python\"",
                background="royalblue",
                foreground="white",
                font=("Calibri", 32, "bold"),
                anchor=CENTER
            )
            izbor_placanja_naslov.pack(ipadx=50, pady=(20, 0), fill=X)
            
            izbor_placanja_podnaslov = ttk.Label(
                izbor_tl,
                text="IZBOR PLAĆANJA",
                background="orange",
                foreground="royalblue",
                font=("Calibri", 28, "bold"),
                anchor=CENTER
            )
            izbor_placanja_podnaslov.pack(ipadx=50, pady=(0, 10), fill=X)
            
            # Frame za sve podatke.
            info_frm = ttk.Frame(izbor_tl)
            info_frm.pack(expand=True, fill=BOTH)
            
            # Frame za izbor plaćanja i detalje porudžbine.
            left_frm = ttk.Frame(info_frm)
            left_frm.pack(side=LEFT, padx=20, pady=20)
            
            izbor_placanja_frm = ttk.Frame(left_frm)
            izbor_placanja_frm.pack(anchor=W, padx=20)
            
            naslov_izbora_lbl = ttk.Label(
                izbor_placanja_frm,
                text="Izbor plaćanja",
                font=("Calibri", 18, "bold"),
                foreground="navy",
                anchor=W
            )
            naslov_izbora_lbl.pack(padx=10, pady=(0, 10))
            
            izbor_rb = {"Gotovina": "1", "Kartica": "2", "Online": "3"}
            placanje_var = StringVar(izbor_placanja_frm)
            
            for (tekst, vrednost) in izbor_rb.items():
                ttk.Radiobutton(
                    izbor_placanja_frm,
                    text=tekst,
                    variable=placanje_var,
                    value=vrednost,
                    style="sb.TRadiobutton",
                    command=online_placanje
                ).pack(anchor=NW, padx=10)
            placanje_var.set("1")
            
            separator_1 = ttk.Separator(left_frm, orient="horizontal")
            separator_1.pack(pady=20, fill=X)
            
            detalji_porudzbine_frm = ttk.Frame(left_frm)
            detalji_porudzbine_frm.pack(anchor=W, padx=20)
    
            detalji_naslov_lbl = ttk.Label(
                detalji_porudzbine_frm,
                text="Detalji porudžbine",
                font=("Calibri", 18, "bold"),
                foreground="navy"
            )
            detalji_naslov_lbl.pack(anchor=W, padx=10, pady=(0, 10))
            
            detalji_stavke_frm = ttk.Frame(detalji_porudzbine_frm)
            detalji_stavke_frm.pack(anchor=W)
            
            detalji_komada_lbl = ttk.Label(
                detalji_stavke_frm,
                text="Komada",
                font=("Calibri", 12, "bold")
            )
            detalji_komada_lbl.grid(column=0, row=1, pady=2, padx=10)
            detalji_artikal_lbl = ttk.Label(
                detalji_stavke_frm,
                text="Artikal",
                font=("Calibri", 12, "bold")
            )
            detalji_artikal_lbl.grid(column=1, row=1, pady=2, padx=10)
            
            spisak_stavki = []
            for row in korpa_tv.get_children():
                spisak_stavki.append(korpa_tv.item(row)["values"])
            
            ukupna_cena = 0
            for i in range(broj_stavki):
                ttk.Label(
                    detalji_stavke_frm,
                    text=spisak_stavki[i][0],
                    font=("Cambria", 12),
                    anchor=CENTER
                ).grid(column=0, row=i+2)
                
                ttk.Label(
                    detalji_stavke_frm,
                    text=spisak_stavki[i][1],
                    font=("Cambria", 12)
                ).grid(column=1, row=i+2, padx=10, sticky=W)
                
                cena_stavke = artikli.artikli_df.cena[
                    artikli.artikli_df.naziv == spisak_stavki[i][1]].item()
                pomnozena_stavka = cena_stavke * int(spisak_stavki[i][0])
                ukupna_cena += pomnozena_stavka

            separator_2 = ttk.Separator(left_frm, orient="horizontal")
            separator_2.pack(pady=20, fill=X)

            ukupno_frm = ttk.Frame(left_frm)
            ukupno_frm.pack(anchor=W, padx=20)
            
            ukupno_naslov = ttk.Label(
                ukupno_frm,
                text="Ukupno",
                font=("Calibri", 18, "bold"),
                foreground="navy",
                anchor=W
            )
            ukupno_naslov.pack(expand=True, fill=X, padx=10)
            
            porudzbina_ukupno = ttk.Label(
                ukupno_frm,
                text=f"{ukupna_cena} din.",
                font=("Calibri", 14, "bold"),
                anchor=W)
            porudzbina_ukupno.pack(expand=True, fill=X, padx=10, pady=10)
    
            # Frame za isporuku i plaćanje.
            right_frm = ttk.Frame(info_frm)
            right_frm.pack(side=LEFT, padx=20, pady=20)
            
            isporuka_frm = ttk.LabelFrame(right_frm, text="Podaci za isporuku")
            isporuka_frm.pack(padx=20, anchor=W)
            
            adresa_lbl = ttk.Label(isporuka_frm, text="Adresa isporuke")
            adresa_lbl.pack(padx=10, pady=(10, 0), anchor=W)
            adresa_ent = ttk.Entry(isporuka_frm, width=30)
            adresa_ent.pack(padx=10, pady=(0, 10), anchor=W)
            
            kontakt_lbl = ttk.Label(isporuka_frm, text="Kontakt telefon")
            kontakt_lbl.pack(padx=10, anchor=W)
            reg = isporuka_frm.register(len_char_limit)
            telefon_ent = ttk.Entry(isporuka_frm, width=30)
            telefon_ent.pack(padx=10, pady=(0, 10), anchor=W)
            telefon_ent.configure(validate="key", validatecommand=(reg, "%P"))
            
            sifra_naslov_lbl = ttk.Label(isporuka_frm, text="Šifra porudžbine")
            sifra_naslov_lbl.pack(padx=10, anchor=W)
            
            sifra_porudzbine = generisanje_sifre()
            
            sifra_lbl = ttk.Label(
                isporuka_frm,
                text=sifra_porudzbine,
                font=("Calibri", 12, "bold")
            )
            sifra_lbl.pack(padx=10, pady=(0, 10), anchor=W)
            
            placanje_frm = ttk.LabelFrame(right_frm, text="Online plaćanje")
            placanje_frm.pack(padx=20, pady=20, anchor=W)

            ime_lbl = ttk.Label(placanje_frm, text="Ime i prezime")
            ime_lbl.pack(padx=10, pady=(10, 0), anchor=W)
            ime_ent = ttk.Entry(placanje_frm, width=30, state="disabled")
            ime_ent.pack(padx=10, pady=(0, 10), anchor=W)
            
            racun_lbl = ttk.Label(placanje_frm, text="Broj računa")
            racun_lbl.pack(padx=10, anchor=W)
            racun_ent = ttk.Entry(placanje_frm, width=30, state="disabled")
            racun_ent.pack(padx=10, pady=(0, 10), anchor=W)
            
            pin_lbl = ttk.Label(placanje_frm, text="PIN")
            pin_lbl.pack(padx=10, anchor=W)
            pin_ent = ttk.Entry(placanje_frm, width=10, state="disabled",
                                show="*")
            pin_ent.pack(padx=10, pady=(0, 10), anchor=W)

            # Dugme koje generiše podatke za transakciju.
            generisi_btn = ttk.Button(
                placanje_frm,
                text="Generiši",
                state="disabled",
                command=generisanje_podataka
            )
            generisi_btn.pack(padx=10, pady=10, anchor=E)


            # Frame za dugmad.
            bottom_frm = ttk.Frame(izbor_tl)
            bottom_frm.pack(expand=True, fill=BOTH, padx=20, pady=20)
            bottom_frm.columnconfigure(0, weight=1)

            realizuj_izbor_btn = ttk.Button(
                bottom_frm,
                text="Realizuj",
                style="velika.TButton",
                command=realizacija_porudzbine
            )
            realizuj_izbor_btn.grid(row=0, padx=20, pady=10, sticky=E)

            
            zatvori_izbor_btn = ttk.Button(
                bottom_frm,
                text="Zatvori",
                style="velika.TButton",
                command=izbor_tl.destroy
            )
            zatvori_izbor_btn.grid(row=1, padx=20, pady=10, sticky=E)

    poruci_tl = Toplevel(root)
    poruci_tl.title("Poručivanje")
    poruci_tl.resizable(0, 0)
    poruci_tl.geometry("1050x920")
    poruci_tl.grab_set()

    # Naslov i informacije o poručivanju.
    poruci_naslov = ttk.Label(
        poruci_tl,
        text="Picerija \"Monty Python\"",
        background="royalblue",
        foreground="white",
        font=("Calibri", 32, "bold"),
        anchor=CENTER
    )
    poruci_naslov.grid(column=0, row=0, columnspan=3, pady=(20, 0), ipadx=40,
                       sticky=EW)
    
    poruci_podnaslov = ttk.Label(
        poruci_tl,
        text="PORUČIVANJE",
        background="orange",
        foreground="royalblue",
        font=("Calibri", 28, "bold"),
        anchor=CENTER
    )
    poruci_podnaslov.grid(column=0, row=1, columnspan=3, pady=(0, 20),
                          ipadx=40, sticky=EW)

    dostava_txt = "Dostava se vrši u roku od 45 minuta od kreirane porudžbine."
    dostava_info = ttk.Label(
        poruci_tl,
        text=dostava_txt,
        font=("Cambria", 13),
        foreground="royalblue"
    )
    dostava_info.grid(column=1, row=2, sticky=EW, pady=5, padx=(30, 0))
    
    prebaci_txt = "Obeležite stavku koju želite da ubacite u korpu i " \
                  "pritisnite dugme \"Ubaci\".\nKada se otvori novi " \
                  "prozor, izaberite broj komada stavke.\nUkoliko želite da " \
                  "uklonite neku stavku, označite je i pritisnite dugme " \
                  "\"Izbriši\"."
    prebacivanje_info = ttk.Label(
        poruci_tl,
        text=prebaci_txt,
        font=("Cambria", 13),
        foreground="royalblue"
    )
    prebacivanje_info.grid(column=1, row=3, sticky=EW, pady=5, padx=(30, 0))

    velicina_info = "Oznake na kraju imena pica pokazuju njihovu veličinu:" \
                    "\n S - 24cm, L - 28cm, XL - 35cm"
    velicina_lbl = ttk.Label(
        poruci_tl,
        text=velicina_info,
        font=("Cambria", 13),
        foreground="royalblue"
    )
    velicina_lbl.grid(column=1, row=4, sticky=EW, pady=5, padx=(30, 0))

    # Frame za izbor artikala.
    artikli_frm = ttk.Frame(poruci_tl)
    artikli_frm.grid(column=0, row=5, pady=20, sticky=NSEW)
    
    izbor_lbl = ttk.Label(
        artikli_frm,
        text="VRSTA ARTIKLA",
        background="black",
        foreground="orange",
        font=("Calibri", 18, "bold"),
        anchor=CENTER
    )
    izbor_lbl.grid(row=0, ipadx=20, ipady=5, pady=(0, 20), sticky=EW)

    rd_buttons = {"Pice": "1", "Salate": "2", "Sendviči": "3", "Deserti": "4",
                  "Napici": "5"}
    kategorija_var = StringVar(artikli_frm)
    for (tekst, vrednost) in rd_buttons.items():
        ttk.Radiobutton(
            artikli_frm,
            text=tekst,
            variable=kategorija_var,
            value=vrednost,
            style="sb.TRadiobutton",
            command=lambda : popunjavanje_tabele(kategorija_var.get())
        ).grid(row=(int(vrednost)), padx=(50, 10), pady=5, sticky=NW)
    kategorija_var.set("1")
    
    # Frame za prikaz treeview stavki i naslova odeljka.
    treeview_frm = ttk.Frame(poruci_tl)
    treeview_frm.grid(column=1, row=5, pady=20, sticky=NSEW)

    treeview_lbl = ttk.Label(
        treeview_frm,
        text="SPISAK ARTIKALA",
        background="black",
        foreground="orange",
        font=("Calibri", 18, "bold"),
        anchor=CENTER
    )
    treeview_lbl.grid(row=0, ipadx=20, ipady=5, pady=(0, 20), sticky=EW)

    ttk.Style().configure("tv_style.Treeview", rowheight=45)
    kolone = ["artikal", "sastav", "cena"]

    # Poseban okvir, tabela (treeview) i skrolbar za nju.
    table_frm = ttk.Frame(treeview_frm)
    table_frm.grid(row=1, padx=10)
    
    lista_artikala_tv = ttk.Treeview(
        table_frm,
        columns=kolone,
        show='headings',
        style="tv_style.Treeview",
        height=8
    )

    lista_artikala_tv.heading("artikal", text="Artikal")
    lista_artikala_tv.heading("sastav", text="Sastav")
    lista_artikala_tv.heading("cena", text="Cena")

    lista_artikala_tv.column("artikal", width=180, anchor=W)
    lista_artikala_tv.column("sastav", width=350, anchor=W)
    lista_artikala_tv.column("cena", width=50, anchor=E)

    lista_artikala_tv.pack(side=LEFT, fill=BOTH)
    
    tree_scroll = ttk.Scrollbar(
        table_frm,
        orient="vertical",
        command=lista_artikala_tv.yview
    )
    tree_scroll.bind_all(
        "<MouseWheel>",
        lambda event: lista_artikala_tv.yview_scroll(-int(event.delta / 60),
                                                     "units")
    )
    lista_artikala_tv.configure(
        yscrollcommand=tree_scroll.set,
        selectmode="browse"
    )
    tree_scroll.pack(side=RIGHT, fill=Y)
    
    # Ubacivanje početnih podataka u treeview.
    popunjavanje_tabele()

    # Frame za korpu.
    korpa_frm = ttk.Frame(poruci_tl)
    korpa_frm.grid(column=2, row=5, padx=0, pady=20, sticky=NSEW)
    
    korpa_lbl = ttk.Label(
        korpa_frm,
        text="KORPA",
        background="black",
        foreground="orange",
        font=("Calibri", 18, "bold"),
        anchor=CENTER
    )
    korpa_lbl.grid(column=0, row=0, ipadx=20, ipady=5, pady=(0, 20), sticky=EW)

    # Frame za spinbox i stavke.
    stavke_frm = ttk.Frame(korpa_frm)
    stavke_frm.grid(column=0, row=1, sticky=NSEW)
    
    korpa_frm.grid_rowconfigure(1, weight=1)
    
    korpa_tv = ttk.Treeview(
        stavke_frm,
        columns=["komada", "artikal"],
        show="headings",
        selectmode="browse"
    )
    
    korpa_tv.heading("komada", text="Kom.")
    korpa_tv.heading("artikal", text="Artikal")
    
    korpa_tv.column("komada", width=50, anchor=CENTER)
    korpa_tv.column("artikal", width=170, anchor=W)
    
    korpa_tv.pack(expand=True, fill=BOTH)

    # Frame za ispisivanje ukupne cene artikala u korpi.
    cena_frm = ttk.Frame(korpa_frm)
    cena_frm.grid(column=0, row=2, padx=5, sticky="sew")
    cena_frm.grid_columnconfigure((0, 1), weight=1)
    
    ukupno_tekst_lbl = ttk.Label(cena_frm, text="Ukupno:", font="Calibri 14")
    ukupno_tekst_lbl.grid(column=0, row=0, padx=5, sticky=W)
    
    ukupno_iznos_lbl = ttk.Label(
        cena_frm,
        text="0 din.",
        font="Calibri 14 bold"
    )
    ukupno_iznos_lbl.grid(column=1, row=0, padx=5, sticky=E)
    
    # Dugmad za ubacivanje artikala u korpu, prihvatanje porudžbine i
    # zatvaranje prozora.
    por_ubaci_btn = ttk.Button(
        poruci_tl,
        text="Ubaci",
        style="velika.TButton",
        command=ubaci_u_korpu
    )
    por_ubaci_btn.grid(column=1, row=6, padx=30, pady=5, sticky=E)
    
    por_poruci_btn = ttk.Button(
        poruci_tl, text="Poruči",
        style="velika.TButton",
        command=izbor_placanja
    )
    por_poruci_btn.grid(column=1, row=7, padx=30, pady=5, sticky=E)
    
    por_izbrisi_btn = ttk.Button(
        poruci_tl,
        text="Izbriši",
        style="velika.TButton",
        command=brisanje_iz_korpe
    )
    por_izbrisi_btn.grid(column=2, row=6, padx=10, pady=5, sticky=E)
    
    por_zatvori_btn = ttk.Button(
        poruci_tl,
        text="Zatvori",
        style="velika.TButton",
        command=poruci_tl.destroy
    )
    por_zatvori_btn.grid(column=2, row=7, padx=10, pady=5, sticky=E)


def nacini_placanja():
    """Osnovne informacije o načinima plaćanja."""
    
    nacini_tl = Toplevel(root)
    nacini_tl.title("Načini plaćanja")
    nacini_tl.resizable(0, 0)
    nacini_tl.attributes("-topmost", "true")
    nacini_tl.geometry("700x500")
    nacini_tl.grab_set()
    
    # Naslov.
    nacini_glavni_naslov = ttk.Label(
        nacini_tl,
        text="Picerija \"Monty Python\"",
        background="royalblue",
        foreground="white",
        font=("Calibri", 32, "bold"),
        anchor=CENTER
    )
    nacini_glavni_naslov.pack(fill=X)
    
    nacini_podnaslov = ttk.Label(
        nacini_tl,
        text="NAČINI PLAĆANJA",
        background="orange",
        foreground="royalblue",
        font=("Calibri", 28, "bold"),
        anchor=CENTER
    )
    nacini_podnaslov.pack(fill=X)
    
    nacini_frm = ttk.Frame(
        nacini_tl,
        style="okvir.TFrame",
        relief="ridge"
    )
    nacini_frm.pack(expand=True, fill=BOTH, padx=10, pady=(20, 10))
    nacini_frm.grid_columnconfigure(0, weight=1)
    nacini_frm.grid_columnconfigure(1, weight=2)
    
    nacini_gotovina_lbl = ttk.Label(
        nacini_frm,
        text="Gotovina",
        background="black",
        foreground="orange",
        font=("Calibri", 20, "bold"),
        anchor=CENTER
    )
    nacini_gotovina_lbl.grid(column=0, row=0, padx=30, pady=(40, 20),
                             sticky=EW)
    nacini_kartica_lbl = ttk.Label(
        nacini_frm,
        text="Kartica",
        background="black",
        foreground="orange",
        font=("Calibri", 20, "bold"),
        anchor=CENTER
    )
    nacini_kartica_lbl.grid(column=0, row=1, padx=30, pady=20, sticky=EW)
    nacini_online_lbl = ttk.Label(
        nacini_frm,
        text="Online",
        background="black",
        foreground="orange",
        font=("Calibri", 20, "bold"),
        anchor=CENTER
    )
    nacini_online_lbl.grid(column=0, row=2, padx=30, pady=20, sticky=EW)
    
    tekst_gotovina_lbl = ttk.Label(
        nacini_frm,
        text="Plaća se gotovinom, prilikom preuzimanja.",
        font=("Cambria", 14),
        background="gainsboro"
    )
    tekst_gotovina_lbl.grid(column=1, row=0, pady=(40, 20), sticky=W)
    tekst_kartica_lbl = ttk.Label(
        nacini_frm,
        text="Plaća se karticom, prilikom preuzimanja.",
        font=("Cambria", 14),
        background="gainsboro"
    )
    tekst_kartica_lbl.grid(column=1, row=1, pady=20, sticky=W)
    tekst_online_lbl = ttk.Label(
        nacini_frm,
        text="Plaća se karticom, prilikom poručivanja.",
        font=("Cambria", 14),
        background="gainsboro"
    )
    tekst_online_lbl.grid(column=1, row=2, pady=20, sticky=W)
    
    nacini_zatvori_btn = ttk.Button(
        nacini_tl,
        text="Zatvori",
        style="velika.TButton",
        command=nacini_tl.destroy
    )
    nacini_zatvori_btn.pack(padx=20, pady=30, anchor=E)


def pracenje_porudzbine():
    """Praćenje statusa porudžbine pomoću njene šifre."""
    
    def pracenje_prikaz():
        """Prikazivanje statusa i detalja porudžbine."""
        
        sve_sifre = porudzbine.porudzbine_df.sifra.to_list()
        unesena_sifra = unos_sifre_ent.get()
        
        if not unos_sifre_ent.get():
            messagebox.showinfo(
                title="Neunesena šifra",
                message="Niste uneli šifru."
            )
        elif unesena_sifra not in sve_sifre:
            messagebox.showinfo(
                title="Neispravna šifra",
                message="Ne postoji porudžbina sa unetom šifrom."
            )
        else:
            # Zatvaranje prethodnog prozora.
            pracenje_tl.destroy()
            
            # Dobijanje detalja porudžbine.
            pracenje_stavke = stavke.stavke_df.stavka[
                stavke.stavke_df.sifra == unesena_sifra].to_list()
            pracenje_komada = stavke.stavke_df.komada[
                stavke.stavke_df.sifra == unesena_sifra].to_list()
            pracenje_status = porudzbine.porudzbine_df.status[
                porudzbine.porudzbine_df.sifra == unesena_sifra].to_string(
                index=False)
            
            # Kreiranje novog prozora.
            pracenje_detalji_tl = Toplevel(root)
            pracenje_detalji_tl.title("Status i detalji porudžbine")
            pracenje_detalji_tl.attributes("-topmost", "true")
            pracenje_detalji_tl.resizable(0, 0)
            pracenje_detalji_tl.grab_set()
            
            # Naziv picerije i naslov prozora
            pracenje_naziv = ttk.Label(
                pracenje_detalji_tl,
                text="Picerija \"Monty Python\"",
                background="royalblue",
                foreground="white",
                font=("Calibri", 32, "bold"),
                anchor=CENTER
            )
            pracenje_naziv.grid(row=0, columnspan=2, sticky=EW, ipadx=50)
            
            pracenje_naslov = ttk.Label(
                pracenje_detalji_tl,
                text="STATUS I DETALJI PORUDŽBINE",
                background="orange",
                foreground="royalblue",
                font=("Calibri", 24, "bold"),
                anchor=CENTER
            )
            pracenje_naslov.grid(row=1, columnspan=2, sticky=EW, pady=(0, 20),
                                 ipadx=50)
            # Status i šifra porudžbine.
            ttk.Label(
                pracenje_detalji_tl,
                text="STATUS PORUDŽBINE:",
                background="gainsboro",
                font=("Calibri", 20),
                anchor=CENTER
            ).grid(row=2, columnspan=2, sticky=EW)
            
            ttk.Label(
                pracenje_detalji_tl,
                text=pracenje_status,
                font=("Calibri", 20, "bold"),
                anchor=CENTER
            ).grid(row=3, columnspan=2, pady=(0, 10), sticky=EW)

            ttk.Label(
                pracenje_detalji_tl,
                text="ŠIFRA PORUDŽBINE:",
                background="gainsboro",
                font=("Calibri", 20),
                anchor=CENTER
            ).grid(row=4, columnspan=2, pady=(10, 0), sticky=EW)
            
            ttk.Label(
                pracenje_detalji_tl,
                text=unesena_sifra,
                font=("Calibri", 20, "bold"),
                anchor=CENTER
            ).grid(row=5, columnspan=2, pady=(0, 10), sticky=EW)

            # Detalji porudžbine.
            ttk.Label(
                pracenje_detalji_tl,
                text="PORUČENO:",
                background="gainsboro",
                font=("Calibri", 20),
                anchor=CENTER
            ).grid(row=6, columnspan=2, pady=(10, 0), sticky=EW)
            
            ttk.Label(
                pracenje_detalji_tl,
                text="komada",
                font=("Calibri", 20, "bold"),
                anchor=CENTER
            ).grid(column=0, row=7, padx=(50, 30))
            
            ttk.Label(
                pracenje_detalji_tl,
                text="stavka",
                font=("Calibri", 20, "bold")
            ).grid(column=1, row=7, sticky=W, padx=(30, 50))

            for i in range(len(pracenje_stavke)):
                ttk.Label(
                    pracenje_detalji_tl,
                    text=pracenje_komada[i],
                    font=("Calibri", 20),
                    anchor=CENTER
                ).grid(column=0, row=8+i, padx=(50, 30))
                
                ttk.Label(
                    pracenje_detalji_tl,
                    text=pracenje_stavke[i],
                    font=("Calibri", 20),
                    anchor=W
                ).grid(column=1, row=8+i, padx=(30, 50), sticky=EW)
            
            # Ukupna cena.
            ukupna_cena_porudzbine = porudzbine.porudzbine_df.ukupno[
                porudzbine.porudzbine_df.sifra == unesena_sifra].to_string(
                index=False)

            ttk.Label(
                pracenje_detalji_tl,
                text="UKUPNA CENA:",
                background="gainsboro",
                font=("Calibri", 20),
                anchor=CENTER
            ).grid(row=8+len(pracenje_stavke), columnspan=2, pady=(30, 0),
                   sticky=EW)
            
            ttk.Label(
                pracenje_detalji_tl,
                text=f"{ukupna_cena_porudzbine} dinara",
                font=("Calibri", 20, "bold"),
                anchor=CENTER
            ).grid(row=9+len(pracenje_stavke), columnspan=2, pady=(0, 10),
                   sticky=EW)
                
            ttk.Button(
                pracenje_detalji_tl,
                text="Zatvori",
                style="velika.TButton",
                command=pracenje_detalji_tl.destroy
            ).grid(column=1, row=10+len(pracenje_stavke), padx=(30, 50),
                   pady=20, sticky=E)
                
    pracenje_tl = Toplevel(root)
    pracenje_tl.title("PRAĆENJE PORUDŽBINE")
    pracenje_tl.attributes("-topmost", "true")
    pracenje_tl.resizable(0, 0)
    pracenje_tl.grab_set()
    
    unos_sifre_lbl = ttk.Label(
        pracenje_tl,
        text="Unesite šifru porudžbine:",
        font=("Calibri", 20, "bold")
    )
    unos_sifre_lbl.grid(column=0, row=0, columnspan=2, padx=10, pady=10,
                        sticky=W)
    
    pracenje_reg = pracenje_tl.register(len_char_limit)
    unos_sifre_ent = ttk.Entry(pracenje_tl, width=30, font=("Calibri", 14))
    unos_sifre_ent.grid(column=0, row=1, columnspan=2, padx=10, sticky=W)
    unos_sifre_ent.configure(validate="key", validatecommand=(pracenje_reg,
                                                              "%P"))
    unos_sifre_ent.focus()
    
    unos_sifre_btn = ttk.Button(
        pracenje_tl,
        text="Prikaži",
        style="velika.TButton",
        command=pracenje_prikaz
        
    )
    unos_sifre_btn.grid(column=0, row=2, padx=10, pady=20, sticky=E)
    
    pracenje_izadji_btn = ttk.Button(
        pracenje_tl,
        text="Izađi",
        style="velika.TButton",
        command=pracenje_tl.destroy
    )
    pracenje_izadji_btn.grid(column=1, row=2, padx=10, pady=20, sticky=E)


def izmene():
    """Menjanje statusa porudžbine i dodavanje artikala na stanje."""
    
    def return_key_event(event):
        """Potvrda pritiskom na taster 'Enter' na formi za lozinku."""
        
        unos_izmena()
        
    def spisak_artikala(combo, radio_var, broj_komada, spin_var):
        """Dobijanje spiska artikala u zavinosti od radiobutton izbora."""
        
        combo.set("")
        broj_komada.configure(text="-")
        spin_var.set(value=0)
        combo.delete(0, END)
        
        if radio_var.get() == "3":
            spisak = artikli.artikli_df.naziv[
                artikli.artikli_df.kolicina < 10].to_list()
        elif radio_var.get() == "2":
            spisak = artikli.artikli_df.naziv[
                artikli.artikli_df.kolicina < 20].to_list()
        else:
            spisak = artikli.artikli_df.naziv.to_list()

        spisak.sort()
        combo["values"] = spisak
    
    def unos_izmena():
        """Otvaranje prozora za izmene nakon potvrđene lozinke."""

        def combo_statusa_dostupan(event):
            """Status porudžbine postaje dostupan i pokazuje vrednost za
            izabranu porudžbinu."""
            
            # Status dostupan.
            status_porudzbine_combo.configure(state="readonly")
            status_promeni_btn.configure(state="normal")
            
            # Dobijanje trenutnog statusa.
            izabrana_sifra = sifra_porudzbine_combo.get()
            trenutni_status = porudzbine.porudzbine_df.status[
                porudzbine.porudzbine_df.sifra == izabrana_sifra
            ].to_string(index=False)
            
            status_porudzbine_combo.set(trenutni_status)
        
        def menjanje_statusa():
            """Dodeljivanje novog statusa."""
            
            combo_sifra = sifra_porudzbine_combo.get()
            
            stari_status = porudzbine.porudzbine_df.status[
                porudzbine.porudzbine_df.sifra == combo_sifra
            ].to_string(index=False)
            
            if stari_status == status_porudzbine_combo.get():
                messagebox.showinfo(
                    title="Nepromenjen status",
                    message="Nema promene statusa, jer je izabrani status "
                            "ostao isti."
                )
            else:
                novi_status = status_porudzbine_combo.get()
                porudzbine.promena_statusa(combo_sifra, novi_status)
                
                messagebox.showinfo(
                    title="Promenjen status",
                    message=f"Porudžbini: {combo_sifra}\nstatus je "
                            f"promenjen u: \"{novi_status.upper()}\"."
                )
            
        def prikaz_kolicine_artikla(event):
            """Upisivanje koliko komada na stanju neki artikal trenutno
            ima."""
            
            komada_na_stanju = artikli.artikli_df.kolicina[
                artikli.artikli_df.naziv == biranje_artikla_cb.get()
            ].to_string(index=False)
            
            komada_kolicina_lbl.configure(text=komada_na_stanju)
        
        def uvecanje_stanja_artikla():
            """Uvecanje kolicine artikla za broj u spinboxu."""
            
            uvecanje = dodaj_var.get()
            
            if not biranje_artikla_cb.get():
                messagebox.showinfo(
                    title="Artikal nije izabran",
                    message="Niste izabrali nijedan artikla."
                )
            elif uvecanje == 0:
                messagebox.showinfo(
                    title="Nepromenjeno stanje",
                    message="Količina artikla nije se promenila,\njer je "
                            "količina za dodavanje ostala 0."
                )
            else:
                trenutno_stanje = artikli.artikli_df.kolicina[
                    artikli.artikli_df.naziv == biranje_artikla_cb.get()
                ].to_string(index=False)
                
                novo_stanje = uvecanje + int(trenutno_stanje)
                
                # Upisivanje novog stanja u tabelu 'artikli'.
                artikli.azuriranje_kolicine(novo_stanje,
                                            biranje_artikla_cb.get())
                
                # Prikaz novog stanja na formi.
                novo_stanje_iz_tabele = artikli.artikli_df.kolicina[
                    artikli.artikli_df.naziv == biranje_artikla_cb.get()
                ].to_string(index=False)
                komada_kolicina_lbl.configure(text=novo_stanje_iz_tabele)
                
                # Obaveštenje o uspešno izvršenom dodavanju količine
                # artikala na stanje.
                messagebox.showinfo(
                    title="Uspešno dodavanje",
                    message=f"Novo stanje artikla \""
                            f"{biranje_artikla_cb.get()}\"\nsada je "
                            f"{novo_stanje_iz_tabele}."
                )
                
                # Ažuriranje combobox liste, ukoliko novo stanje nije manje od
                # 20 ili 10.
                if dodavanje_var.get() == "2" and \
                        int(novo_stanje_iz_tabele) >= 20:
                    biranje_artikla_cb.set("")
                    
                    novi_spisak = artikli.artikli_df.naziv[
                        artikli.artikli_df.kolicina < 20].to_list()
                    novi_spisak.sort()
                    
                    biranje_artikla_cb["values"] = novi_spisak
                    komada_kolicina_lbl.configure(text="-")
                    dodaj_var.set(value=0)
                
                elif dodavanje_var.get() == "3" and \
                        int(novo_stanje_iz_tabele) >= 10:
                    biranje_artikla_cb.set("")

                    novi_spisak = artikli.artikli_df.naziv[
                        artikli.artikli_df.kolicina < 10].to_list()
                    novi_spisak.sort()

                    biranje_artikla_cb["values"] = novi_spisak
                    komada_kolicina_lbl.configure(text="-")
                    dodaj_var.set(value=0)


        if not lozinka_ent.get():
            messagebox.showinfo(
                title="Nema unosa",
                message="Niste uneli nijedan karakter za pristupnu lozinku."
            )
        elif lozinka_ent.get() != lozinka:
            messagebox.showinfo(
                title="Pogrešna lozinka",
                message="Niste uneli ispravnu lozinku."
            )
        else:
            # Zatvaranje prozora za unos lozinke.
            izmene_lozinka_tl.destroy()
            
            # Otvaranje prozora za izmene.
            izmene_tl = Toplevel(root)
            izmene_tl.title("Promena statusa i dodavnje artikala")
            izmene_tl.resizable(0, 0)
            izmene_tl.grab_set()
            
            izmene_naziv = ttk.Label(
                izmene_tl,
                text="Picerija \"Monty Python\"",
                background="royalblue",
                foreground="white",
                font=("Calibri", 32, "bold"),
                anchor=CENTER
            )
            izmene_naziv.grid(row=0, columnspan=2, sticky=EW, ipadx=50)

            izmene_naslov = ttk.Label(
                izmene_tl,
                text="IZMENE",
                background="orange",
                foreground="royalblue",
                font=("Calibri", 24, "bold"),
                anchor=CENTER
            )
            izmene_naslov.grid(row=1, columnspan=2, sticky=EW, pady=(0, 40),
                               ipadx=50)
            
            # LabelFrame za menjanje statusa porudžbine.
            izmene_status_frm = ttk.LabelFrame(
                izmene_tl,
                text="Menjanje statusa",
                style="lblfrm.TLabelframe"
            )
            izmene_status_frm.grid(column=0, row=2, padx=20, sticky=NSEW)
            
            sifra_porudzbine_lbl = ttk.Label(
                izmene_status_frm,
                text="Izaberite šifru porudžbine:",
                font=("Calibri", 20)
            )
            sifra_porudzbine_lbl.pack(padx=10, pady=(20, 0), anchor=W)
            
            sve_sifre = porudzbine.porudzbine_df.sifra.to_list()
            sve_sifre.sort()
            sifra_porudzbine_combo = ttk.Combobox(
                izmene_status_frm,
                font=("Calibri", 14, "bold"),
                width=26,
                state="readonly",
                values=sve_sifre
            )
            sifra_porudzbine_combo.pack(padx=10, anchor=W)
            
            status_frm = ttk.Frame(izmene_status_frm, height=75)
            status_frm.pack()
            
            status_porudzbine_lbl = ttk.Label(
                izmene_status_frm,
                text="Izaberite status porudžbine:",
                font=("Calibri", 20)
            )
            status_porudzbine_lbl.pack(padx=10, pady=(20, 0), anchor=W)
            
            statusi = ["Kreirana", "U pripremi", "Poslata", "Isporučena"]
            status_porudzbine_combo = ttk.Combobox(
                izmene_status_frm,
                font=("Calibri", 14, "bold"),
                width=26,
                values=statusi,
                state="disabled"
            )
            status_porudzbine_combo.pack(padx=10, anchor=W)
            
            sifra_porudzbine_combo.bind("<<ComboboxSelected>>",
                                        combo_statusa_dostupan)

            status_promeni_btn = ttk.Button(
                izmene_status_frm,
                text="Promeni",
                style="velika.TButton",
                state="disabled",
                command=menjanje_statusa
            )
            status_promeni_btn.pack(expand=True, padx=30, pady=30, anchor=SE)
            
            # LabelFrame za dodavanje artikala.
            izmene_artikli_frm = ttk.LabelFrame(
                izmene_tl,
                text="Dodavanje artikala",
                style="lblfrm.TLabelframe"
            )
            izmene_artikli_frm.grid(column=1, row=2, padx=20, sticky=NSEW)
            
            izbor_artikala_lbl = ttk.Label(
                izmene_artikli_frm,
                text="Izbor artikala po broju komada:",
                font=("Calibri", 20)
            )
            izbor_artikala_lbl.pack(padx=10, pady=(20, 10), anchor=W)
            
            broj_artikala_rb = {"Svi artikli": "1", "Manje od 20": "2",
                                "Manje od 10": "3"}
            dodavanje_var = StringVar(izmene_artikli_frm)
            
            for (tekst, vrednost) in broj_artikala_rb.items():
                ttk.Radiobutton(
                    izmene_artikli_frm,
                    text=tekst,
                    variable=dodavanje_var,
                    value=vrednost,
                    style="sb.TRadiobutton",
                    command=lambda : spisak_artikala(
                        biranje_artikla_cb,
                        dodavanje_var,
                        komada_kolicina_lbl,
                        dodaj_var
                    )).pack(padx=10, anchor=NW)
            dodavanje_var.set("1")
            
            biranje_artikla_lbl = ttk.Label(
                izmene_artikli_frm,
                text="Izaberite artikal sa spiska:",
                font=("Calibri", 20)
            )
            biranje_artikla_lbl.pack(padx=10, pady=(20, 0), anchor=W)
            
            pocetni_spisak = sorted(artikli.artikli_df.naziv)
            biranje_artikla_cb = ttk.Combobox(
                izmene_artikli_frm,
                font=("Calibri", 14, "bold"),
                width=26,
                state="readonly",
                values=pocetni_spisak
            )
            biranje_artikla_cb.pack(padx=10, anchor=W)
            biranje_artikla_cb.bind("<<ComboboxSelected>>",
                                    prikaz_kolicine_artikla)

            komada_naslov_lbl = ttk.Label(
                izmene_artikli_frm,
                text="Komada na stanju:",
                font=("Calibri", 20)
            )
            komada_naslov_lbl.pack(padx=10, pady=(20, 0), anchor=W)
            
            komada_kolicina_lbl = ttk.Label(
                izmene_artikli_frm,
                text="-",
                font=("Calibri", 14, "bold"),
                foreground="royalblue"
            )
            komada_kolicina_lbl.pack(padx=10, anchor=W)
            
            kolicina_dodavanja_lbl = ttk.Label(
                izmene_artikli_frm,
                text="Količina za dodavanje:",
                font=("Calibri", 20)
            )
            kolicina_dodavanja_lbl.pack(padx=10, pady=(20, 0), anchor=W)
            
            dodaj_var = IntVar(value=0)
            izmene_dodavanje_reg = izmene_artikli_frm.register(
                validacija_unosa)
            kolicina_dodavanja_sb = ttk.Spinbox(
                izmene_artikli_frm,
                from_=0,
                to=50,
                textvariable=dodaj_var,
                font=("Calibri", 14, "bold"),
                foreground="royalblue",
                width=4,
                validate="key",
                validatecommand=(izmene_dodavanje_reg, "%P")
            )
            kolicina_dodavanja_sb.pack(padx=10, anchor=W)
            
            stanje_dodaj_btn = ttk.Button(
                izmene_artikli_frm,
                text="Dodaj",
                style="velika.TButton",
                command=uvecanje_stanja_artikla
            )
            stanje_dodaj_btn.pack(padx=30, pady=30, anchor=E)
            
            izmene_zatvori_btn = ttk.Button(
                izmene_tl,
                text="Zatvori",
                style="velika.TButton",
                command=izmene_tl.destroy
            )
            izmene_zatvori_btn.grid(column=1, row=3, padx=50, pady=20,
                                    sticky=E)
    
    # Pristupna lozinka (potrebna, jer pristup izmenama ne treba da imaju
    # svi korisnici, već samo oni koji su za njih ovlašćeni).
    lozinka = "MP-pice"
    
    izmene_lozinka_tl = Toplevel(root)
    izmene_lozinka_tl.title("Pristup izmenama")
    izmene_lozinka_tl.attributes("-topmost", "true")
    izmene_lozinka_tl.resizable(0, 0)
    izmene_lozinka_tl.grab_set()
    
    lozinka_lbl = ttk.Label(
        izmene_lozinka_tl,
        text="Unesite lozinku za pristup izmenama:",
        font=("Calibri", 18, "bold")
    )
    lozinka_lbl.grid(row=0, columnspan=2, padx=20, pady=10, sticky=W)
    
    lozinka_ent = ttk.Entry(izmene_lozinka_tl, width=37, font=("Calibri", 14),
                            show="*")
    lozinka_ent.grid(row=1, columnspan=2, padx=20, sticky=W)
    lozinka_ent.focus()
    
    lozinka_potvrdi_btn = ttk.Button(
        izmene_lozinka_tl,
        text="Potvrdi",
        style="velika.TButton",
        command=unos_izmena
    )
    lozinka_potvrdi_btn.grid(column=0, row=2, padx=20, pady=20, sticky=E)
    
    lozinka_izadji_btn = ttk.Button(
        izmene_lozinka_tl,
        text="Izađi",
        style="velika.TButton",
        command=izmene_lozinka_tl.destroy
    )
    lozinka_izadji_btn.grid(column=1, row=2, padx=20, pady=20, sticky=E)
    
    izmene_lozinka_tl.bind("<Return>", return_key_event)


def izvestaji():
    """Razni izveštaji koji daju uvid u podatke baze podataka."""
    
    def izbor_izvestaja(var_get):
        """Biranje izveštaja koji želimo da dobijemo i njegov prikaz."""
        
        if var_get == "1":
            cene_svih_porudzbina = porudzbine.porudzbine_df.ukupno.to_list()
            
            ukupan_promet = 0
            for cena in cene_svih_porudzbina:
                ukupan_promet += cena
            
            promet_tl = Toplevel(izvestaji_tl)
            promet_tl.title("Ukupan promet")
            promet_tl.attributes("-topmost", "true")
            promet_tl.resizable(0, 0)
            promet_tl.grab_set()
            
            promet_naziv = ttk.Label(
                promet_tl,
                text="Picerija \"Monty Python\"",
                background="royalblue",
                foreground="white",
                font=("Calibri", 32, "bold"),
                anchor=CENTER
            )
            promet_naziv.pack(fill=X, ipadx=50)

            promet_naslov = ttk.Label(
                promet_tl,
                text="UKUPAN PROMET",
                background="orange",
                foreground="royalblue",
                font=("Calibri", 24, "bold"),
                anchor=CENTER
            )
            promet_naslov.pack(fill=X, ipadx=50, pady=(0, 40))
            
            promet_tekst_lbl = ttk.Label(
                promet_tl,
                text="Ukupan promet picerije \"Monty Python\" je:",
                font=("Calibri", 20)
            )
            promet_tekst_lbl.pack(padx=50, pady=(0, 10), anchor=W)
            
            promet_iznos_lbl = ttk.Label(
                promet_tl,
                text=f"{ukupan_promet} dinara",
                font=("Calibri", 20, "bold")
            )
            promet_iznos_lbl.pack(padx=50, anchor=W)
            
            promet_zatvori_btn = ttk.Button(
                promet_tl,
                text="Zatvori",
                style="velika.TButton",
                command=promet_tl.destroy
            )
            promet_zatvori_btn.pack(padx=30, pady=30, anchor=E)
        
        elif var_get == "2":
            stavke.najprodavaniji_artikli(5)
        elif var_get == "3":
            stavke.najprodavaniji_artikli(20)
        elif var_get == "4":
            stavke.artikal_najveci_prihod()
        elif var_get == "5":
            porudzbine.visina_cena_porudzbina()
        elif var_get == "6":
            porudzbine.visina_cena_porudzbina(False)
        elif var_get == "7":
            artikli.visina_cena_artikala()
        else:
            artikli.visina_cena_artikala(False)
    
    izvestaji_tl = Toplevel(root)
    izvestaji_tl.title("Izveštaji")
    izvestaji_tl.resizable(0, 0)
    izvestaji_tl.grab_set()
    
    izvestaji_naziv = ttk.Label(
        izvestaji_tl,
        text="Picerija \"Monty Python\"",
        background="royalblue",
        foreground="white",
        font=("Calibri", 32, "bold"),
        anchor=CENTER
    )
    izvestaji_naziv.pack(fill=X, ipadx=50)
    
    izvestaji_naslov = ttk.Label(
        izvestaji_tl,
        text="IZVEŠTAJI",
        background="orange",
        foreground="royalblue",
        font=("Calibri", 24, "bold"),
        anchor=CENTER
    )
    izvestaji_naslov.pack(fill=X, ipadx=50, pady=(0, 40))
    
    izvestaji_izbor_frm = ttk.Frame(
        izvestaji_tl,
        style="okvir.TFrame",
        relief="ridge"
    )
    izvestaji_izbor_frm.pack(fill=X, padx=10)
    
    # Radiobutton.
    izvestaji_opcije = {
        "Ukupan promet": "1",
        "Najprodavaniji artikli (prvih 5)": "2",
        "Najprodavaniji artikli (prvih 20)": "3",
        "Procentualni prihod po artiklu (prvih 5)": "4",
        "Najskuplje porudžbine (prvih 5)": "5",
        "Najjeftinije porudžbine (prvih 5)": "6",
        "Najskuplji artikli (prvih 10)": "7",
        "Najjeftiniji artikli (prvih 10)": "8"
    }
    izvestaji_var = StringVar(izvestaji_izbor_frm)
    
    for (tekst, vrednost) in izvestaji_opcije.items():
        if tekst == "Ukupan promet":
            pady_val = (25, 5)
        elif tekst == "Najjeftiniji artikli (prvih 10)":
            pady_val = (5, 30)
        else:
            pady_val = 5
        
        ttk.Radiobutton(
            izvestaji_izbor_frm,
            text=tekst,
            variable=izvestaji_var,
            value=vrednost,
            style="gray.TRadiobutton"
        ).pack(padx=50, pady=pady_val, anchor=NW)
    izvestaji_var.set("1")
    
    izvestaji_primeni_btn = ttk.Button(
        izvestaji_tl,
        text="Primeni",
        style="velika.TButton",
        command=lambda : izbor_izvestaja(izvestaji_var.get())
    )
    izvestaji_primeni_btn.pack(side=LEFT, padx=80, pady=30, anchor=E)
    
    izvestaji_zatvori_btn = ttk.Button(
        izvestaji_tl,
        text="Zatvori",
        style="velika.TButton",
        command=izvestaji_tl.destroy
    )
    izvestaji_zatvori_btn.pack(padx=20, pady=30, anchor=W)


glavni_naslov_lbl1 = ttk.Label(
    root,
    text="Picerija ",
    background="royalblue",
    foreground="white",
    font=("Calibri", 32, "bold"),
    anchor=E,
    width=10
)
glavni_naslov_lbl1.grid(column=0, row=0, sticky=E)

glavni_naslov_lbl2 = ttk.Label(
    root,
    text=" \"Monty Python\"",
    background="royalblue",
    foreground="orange",
    font=("Calibri", 32, "bold"),
    anchor=W,
    width=17
)
glavni_naslov_lbl2.grid(column=1, row=0, sticky=W)

#Učitavanje slike.
image = Image.open("pics/Monty-Python-bw.jpg")

#Prilagođavanje veličine slike.
image_resize = image.resize((600, 337))
mpbw = ImageTk.PhotoImage(image_resize)

#Postavljanje slike.
monty_python_pic = ttk.Label(root, image=mpbw)
monty_python_pic.grid(column=0, columnspan=2, row=1)

#Okvir za glavne opcije - za svaku postoji dugme.
glavne_opcije_frm = ttk.Frame(
    root,
    style="okvir.TFrame",
    relief="ridge"
)
glavne_opcije_frm.grid(column=0, columnspan=2, row=2, pady=20)

meni_btn = ttk.Button(
    glavne_opcije_frm,
    text="Meni",
    style="velika.TButton",
    width=20,
    command=prikaz_artikala
)
meni_btn.grid(column=0, row=0, padx=(20, 10), pady=(25, 5), sticky=EW)

meni_lbl = ttk.Label(
    glavne_opcije_frm,
    text="Pogledajte šta imamo u ponudi.",
    font=("Cambria", 14),
    background="gainsboro"
)
meni_lbl.grid(column=1, row=0, padx=(10, 20), pady=(25, 5), sticky=W)

porucivanje_btn = ttk.Button(
    glavne_opcije_frm,
    text="Poručivanje",
    style="velika.TButton",
    width=20,
    command=porucivanje
)
porucivanje_btn.grid(column=0, row=1, padx=(20, 10), pady=5)

porucivanje_lbl = ttk.Label(
    glavne_opcije_frm,
    text="Naručite online neku od naših pica.",
    font=("Cambria", 14),
    background="gainsboro"
)
porucivanje_lbl.grid(column=1, row=1, padx=(10, 20), pady=5, sticky=W)

placanje_btn = ttk.Button(
    glavne_opcije_frm,
    text="Načini plaćanja",
    style="velika.TButton",
    width=20,
    command=nacini_placanja
)
placanje_btn.grid(column=0, row=2, padx=(20, 10), pady=5)

placanje_lbl = ttk.Label(
    glavne_opcije_frm,
    text="Načini na koje možete platiti.",
    font=("Cambria", 14),
    background="gainsboro"
)
placanje_lbl.grid(column=1, row=2, padx=(10, 20), pady=5, sticky=W)

pracenje_btn = ttk.Button(
    glavne_opcije_frm,
    text="Praćenje porudžbine",
    style="velika.TButton",
    width=20,
    command=pracenje_porudzbine
)
pracenje_btn.grid(column=0, row=3, padx=(20, 10), pady=5)

pracenje_lbl = ttk.Label(
    glavne_opcije_frm,
    text="Pogledajte status vaše porudžbine.",
    font=("Cambria", 14),
    background="gainsboro"
)
pracenje_lbl.grid(column=1, row=3, padx=(10, 20), pady=5, sticky=W)

izmene_btn = ttk.Button(
    glavne_opcije_frm,
    text="Izmene",
    style="velika.TButton",
    width=20,
    command=izmene
)
izmene_btn.grid(column=0, row=4, padx=(20, 10), pady=5)

izmene_lbl = ttk.Label(
    glavne_opcije_frm,
    text="Status pošiljke i dodavanje artikala.",
    font=("Cambria", 14),
    background="gainsboro"
)
izmene_lbl.grid(column=1, row=4, padx=(10, 20), pady=5, sticky=W)

izvestaji_btn = ttk.Button(
    glavne_opcije_frm,
    text="Izveštaji",
    style="velika.TButton",
    width=20,
    command=izvestaji
)
izvestaji_btn.grid(column=0, row=5, padx=(20, 10), pady=(5, 25))

izvestaji_lbl = ttk.Label(
    glavne_opcije_frm,
    text="Izveštaji i njihov grafički prikaz.",
    font=("Cambria", 14),
    background="gainsboro"
)
izvestaji_lbl.grid(column=1, row=5, padx=(10, 20), pady=(5, 25), sticky=W)

zatvaranje_aplikacije = ttk.Button(
    root,
    text="Zatvori",
    style="velika.TButton",
    command=zatvaranje
)
zatvaranje_aplikacije.grid(column=1, row=3, padx=20, pady=20, sticky=E)

root.mainloop()
