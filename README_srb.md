# 1. Naslov projekta
    ONLINE PORUDŽBINE ZA RESTORAN (PICERIJU)

# 2. Kratak opis projekta
Projekat je urađen kao sastavni deo prakse kursa "Python Developer - 
Advanced" u kompaniji **ITOiP** (IT Obuka i Praksa - https://itoip.rs).

Sistem za upravljanje porudžbinama i plaćanjem za fiktivnu piceriju.

Aplikacija je urađena u Pythonu, uz pomoć PostgreSQL sistema za upravljanje 
bazama podataka.

Tabele koje su urađene kao primer nalaze se u arhivi 'tables.zip'.

# 3. Sadržaj README.md fajla
#### 1. Naslov projekta
#### 2. Kratak opis projekta
#### 3. Sadržaj README.md fajla
#### 4. Baza podataka i struktura tabela
#### 5. Opis i korišćenje aplikacije

# 4. Baza podataka i struktura tabela
Naziv baze podataka: "picerija-porucivanje"

Tabele:

    artikli
        naziv               (varchar (30), primary key, not null)
        vrsta               (varchar (29))          # vrsta artikla
        sastav              (text, not null)        # sastav artikla
        kolicina            (integer, not null)     # broj dosutpnih artikala
        cena                (integer, not null)     # cena pojedinačnog artikla

    porudzbine
        sifra               (varchar (10), prmary key, not null)
        adresa              (varchar (30), not null)    # adresa isporuke
        telefon             (varchar (10), not null)    # kontakt telefon
        placanje            (varchar (10), not null)    # način plaćanja
        status              (varchar (25), not null)    # status porudžbine
        ukupno              (integer, not null)         # ukupna cena

    stavke
        broj stavke         (serial, primary key, not null)
        sifra               (varchar (10), not null)    # sifra porudžbine
        stavka              (varchar (30), not null)    # pojedinacna stavka
        komada              (integer, not null)         # količina stavke

    transakcije
        sifra               (varchar (10), primary key, not null)
        uplatilac           (varchar (25), not null)    # puno ime uplatioca
        racun               (varchar (20), not null)    # broj bankovnog računa
        iznos               (integer, not null)         # iznos transakcije
# 5. Opis i korišćenje aplikacije

## 5.1. Glavni ekran

Glavni ekran se sastoji od naziva picerije, slike i dugmadi za izbor akcije 
u aplikaciji. Svako dugme pored sebe ima i kratko objašnjenje, osim dugmeta 
'Zatvori' na dnu ekrana, koje služi za zatvaranje aplikacije.

## 5.2 Meni

Pritiskom na dugme 'Meni' na glavnom ekranu, otvara se novi prozor u kojem 
se nalazi izbor artikala po kategorijama.

U levom delu ekrana nalazi se dugmad za različite kategorije artikala. To 
su: 'Pice', 'Salate', 'Sendviči', 'Deserti' i 'Napici'. Pritiskom na neko 
dugme dobijamo spisak artikala iz te kategorije koje možemo poručiti. 
Spisak tabelarnog tipa sastoji se od naziva artikla, njegovog sastava i 
cene. Prilikom otvaranja ekrana učitava se kategorija 'Pice' kao osnovne 
vrste artikala koji se nude.

Na dnu ovog ekrana postoji dugme 'Poruči', koje nas vodi u odeljak za 
poručivanje i dugme 'Izađi' koje zatvara ekran. Dugme 'Poruči' takođe 
zatvara ovaj ekran i otvara novi, kojem se može pritupiti i sa glavnog ekrana.

## 5.3 Poručivanje

#### 5.3.1 Vrsta artikala, spisak artikala i korpa

Pritiskom na dugme 'Poručivanje' otvaramo deo koji se odnosi na kreiranje 
porudžbine. Kao što je već rečeno, dugme 'Poruči' iz prethodnog prozora 
takođe nas dovodi u deo za poručivanje.

Na novom ekranu koji se otvara, ispod naslova, nalaze se kratka objašnjenja 
o poručivanju, tj. o vremenu isporuke, načinu ubacivanja artikala u korpu i 
brisanja iz nje, kao i o slovima na kraju naziva pica, koja označavaju 
veličinu njenog prečnika.

Na sličan način kao i na prethodnom ekranu i ovde imamo izbor kategorija 
ponuđenih artikala, samo što se ovde taj izbor vrši pomoću izbora jedne od 
opcija. Taj izbor vrste artikala nam je ponuđen s leve strane.

U srednjem delu ekrana imamo naziv, sastav i cenu artikala iz izabrane 
kategorije. Na desnoj strani je korpa u koju se ubacuju artikli i njihova 
količina koje želimo da poručimo. Na dnu ekrana nalazi se dugme za 
ubacivanje artikla u korupu, dugme za brisanje iz korpe, dugme za dovršetak 
poručivanja i dugme za zatvaranje ovog ekrana.

Da bi se neki artikal ubacio u korpu, on mora da se obeleži u srednjem delu 
ekrana. Pritiskom na dugme 'Ubaci', otvara se mali prozor koji nam, osim 
naziva artikla, omogućava i da povećamo količinu izabranog artikla.

Ispod same korpe pokazuje se ukupna cena artikala ubačenih u korpu.

Ukoliko nismo zadovoljni onim što se nalazi u korpi, može brisati 
pojedinačne stavke tako što ih obeležimo i pritisnemo dugme 'Izbriši'. Ako 
smo zadovoljni sadržajem korpe, pritiskom na dugme 'Poruči' otvaramo novi 
ekran u kojem se dovršava kreiranje porudžbine.

#### 5.3.2 Izbor plaćanja i unos neophodnih podataka

Novi prozor omogućava nam izbor o načinu plaćanja. Platiti se može 
gotovinom ili karticom prilikom preuzimanja porudžbine ili odmah online, 
takođe uz pomoć platne kartice.

U levom delu ekrana nalazi se izbor plaćanja. Ispod njega su detalji 
porudžbine u vidu naziva artikala i njihove količine, dok se ispod tih 
detalja nalazi i ukupna cena porudžbine.

Desni deo ekrana obezbeđen je za unos neophodnih podataka. Na vrhu se 
nalaze polja za unos adrese isporuke i kontakt telefon kojim se može 
stupiti u vezu sa poručiocem. Ovi podaci su potrebni za svaku vrstu izbora 
plaćanja. Za njima sledi programski generisana šifra porudžbine pomoću koje 
se može pratiti status porudžbine.

Ispod svega toga nalaze se polja za unos prilikom online plaćanja. Ona su 
nedostupna sve dok se ne izvrši izbor online plaćanja na levoj strani 
ekrana. U ta polja se unosi ime i prezime uplatioca, koje mora da se 
poklapa s brojem kartice s koje se vrši uplata. Odmah sledi polje koje 
služi za unošenje upravo tog broja bankovnog računa. Kao dodatno osiguranje 
koristi se i unos PIN-a poznatog korisniku računa, čije se cifre ne vide 
prilikom unosa. Ukoliko se sve tri vrednosti slažu i ima dovoljno novca na 
računu za uplatu porudžbine, moguće je izvršiti transakciju.

**NAPOMENA**: Ovde bi najbolje bilo ubaciti neki od postojećih API-ja koji 
omogućavaju stvarne transakcije. Međutim, oni su uglavnom komercijalni. 
Osim toga, služe za realne transakcije, koje za potrebe ovog projekat nisu 
ni neophodne ni poželjne. Zbog toga je ovde načinjen pojednostavljeni 
sistem uz pomoć podataka smeštenih u fajl 'podaci.py'. Dugme 'Generiši' u 
polja za online plaćanje ubacuje podatke koji se smatraju validnim, svaki 
drugi nasumični unos ili menjanje generisanih podataka smatraće se 
pogrešnim unosom i simulacija transkacije će biti odbijena. Takođe treba 
napomenuti da se prilikom transakcije ne skidaju sredstva sa računa, jer to 
nije posao ovog programa. Ta fiktivna sredstva postoje samo za potrebe 
prikaza ostalih funkcija i mogućnosti aplikacije.

Dugme 'Realizuj' služi za završetak kreiranja porudžbine.

Ukoliko je porudžbina odbijena, pojaviće se obaveštenje o tome šta nije 
bilo u redu. S druge strane, ako je ona prihvaćena, ovaj ekran se zatvara, 
a otvara se pozdravni ekran s obaveštenjem o uspešno kreiranoj porudžbini, 
na kojem se, osim obaveštenja i pozdrava, nalazi broj porudžbine koji služi 
za praćenje njenog statusa.

Na kraju, pošto je porudžbina uspešno kreirana, relevantni podaci se 
ubacuju u sve tabele. U tabeli 'artikli' vrši se korekcija količine 
artikala, podaci o porudžbini ubacuju se u tabelu 'porudzbine', detalji 
porudzbine unose se u tabelu 'stavke', informacije o transakciji (ukoliko 
je plaćanje bilo online) unose se u tabelu 'transakcije'.

## 5.4. Načini plaćanja

Dugme 'Načini plaćanja', s glavnog ekrana, vodi nas u novi prozor u kome 
možemo da vidimo načine na koje je moguće platiti porudžbinu i kada se 
plaćanje izvršava. Osim ovih obaveštenja još jedino postoji dugme 'Zatvori' 
koje, kako mu i samo ime kaže, zatvara ovaj prozor.

## 5.5. Praćenje porudžbine

Pritiskom na dugme 'Praćenje porudžbine' na glavnom ekranu otvara se novi 
prozor koji zahteva da se unese šifra porudžbine koju želimo da pratimo. 
Jedino onaj ko zna širfu može nastaviti dalje.

Kada se unese ispravna šifra, otvara se novi prozor u kojem, ispod naslova, 
možemo videti status porudžbine. Mogući statusi su: 'Kreirana', 'U pripremi', 
'Poslata' i 'Isporučena'. Ispod statusa je šifra porudžbine koju želimo da 
pratimo. Nakon toga slede detalji o naručenim artiklima i njihovim 
količinama, da bi na kraju bila istaknuta cena porudžbine.

Dugme 'Zatvori', zatvara ovaj prozor.

## 5.6 Izmene

Pritiskanjem dugmeta 'Izmene' na glavnoj formi otvara se prozor za unos 
lozinke. Ovaj prozor je neophodan, jer izmenama koje se vrše ne treba da 
pristupaju svi korisnici, nego samo ona lica koja su za to ovlašćena. 
Budući da ovaj projekat ima ulogu prikazivanja mogućnosti načinjene 
aplikacije, trebalo bi reći da je lozinka 'MP-pice', kako bi se dobio uvid 
i u taj deo programa.

Nakon unesene ispravne lozinke i njene potvrde, otvara se novi prozor u 
kojem možemo vršiti dve vrste izmena.

#### 5.6.1 Menjanje statusa

U levom delu novog prozora moguće je izvršiti promenu statusa porudžbine. 
Padajući meni za izbor novog statusa i dugme 'Promeni', kojim se izmena 
vrši, nedostupni su dok se ne izabere šifra porudžbine.

Lista svih šifri porudžbina nalazi se u gornjem padajućem meniju. Prilikom 
izbora bilo koje šifre, padajući meni za izbor statusa i dugme za izmenu 
postaju dostupni. U padajući meni statusa upisuje se trenutni status 
porudžbine, koji se menja izborom nekog drugog od ponuđenih statusa.

#### 5.6.2 Dodavanje artikala

Desni deo ekrana služi za dodavanja artikala na stanje. Prvo postoji izbor 
svih artikala, samo onih artikala kojih ima manje od 20 na stanju ili izbor 
samo onih artikala kojih ima manje od 10 na stanju. Jasno je da ovaj 
poslednji služi da se brzo stekne uvid u to šta je hitno potrebno dodati.

Svaki od ovih izbora nudi listu artikala u skladu s njihovim brojnim 
stanjem. Izbor artikla sa spiska vrši se u padajućem meniju koji sledi. 
Nakon što se izabere artikal, pokazuje se njegovo trenutno brojno stanje - 
ispod teksta 'Komada na stanju:'.

Koliko artikala se dodaje na stanje upisuje se u Spinboxu na dnu. Ako smo 
zadovoljni unetim brojem, pritiskom na dugme 'Dodaj' možemo uneti upisanu 
količinu izabranog artikla na stanje.

Nakon izvršenog dodavanja na stanje, ažurira se tabela 'artikli' i spisak 
artikala ukoliko izabrani artikal prelazi zadate vrednosti od 20 i 10.

Dugme 'Zatvori' zatvara ovaj prozor.

## 5.6 Izveštaji

Na kraju, dugme 'Izveštaji', s glavnog ekrana, vodi nas u novi prozor u 
kojem imamo 8 izbora. Prvi izbor daje nam samo obaveštenje o ukupnom 
prometu picerije, u posebnom prozoru. Ostale opcije su grafički prikazi po 
opisanim kriterijumima.

Druga i treća opcija pokazuju prvih 5 i prvih 20 najprodavanijih artikala.

Četvrta opcija prikazuje procentualni prihod za prvih 5 artikala, koji su u 
toj kategoriji najbolji, uz procentualni prihod svih ostalih prodatih 
artikala zajedno.

Peti i šesti izbor daju nam po 5 porudžbina čije su novčane vrednosti 
najveće i najmanje.

Poslednje dve opcije daju nam uvid u 10 najskupljih i 10 najjeftinijih 
artikala.
