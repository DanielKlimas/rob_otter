#
#                                                                        README
#
--------------------------------------------------------------------- Beschreibung -----------------------------------------------------------------------------------------
Bei diesem Programm werden mit Hilfe von "Scrapy" je nach konfiguration mehrere Google seiten nach .at Domänen durchsucht und alle in eine Datenbank gespeichert.
Sie können in der "webscraping.ini" Datei konfigurieren wie die Datenbank heißen soll, 
wie viele google seiten sie scrapen möchten und wie das .json output file von Scrapy heißen soll. 

Ebenso werden alle gefundenen Domänen auf mehrfaches Vorkommen überprüft und danach von jeder Seite ausgelesen mit welchem Generator diese erstellt wurde.
Hier können sie ebenso in der "webscraping.ini" Datei konfigurieren wie viele Sekunden sie das Programm auf ein response der Seite warten lassen wollen.

In die Datenbank werden nun ebenfalls zu den Domänen die Generatoren mit einem Timestamp zum Zeitpunkt des Auslesens des Generators gespeichert.

Am Ende wird eine Hochrechnung aufs Terminal geprintet, wo steht wie oft unter allen Domänen alle gefundenen Generatoren vorgekommen sind und wie viel Prozent das
von allen Gefundenen waren. Die Gesamtanzahl aller gefundenen Domänen ohne mehrfachem Vorkommen wird natürlich auch ausgegeben.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#
#
----------------------------------------------------------------------- AUSFÜHREN ------------------------------------------------------------------------------------------
Um Scrapy Auszuführen müssen sie lediglich im .ini file das .json file angeben welches sie möchten und danach mit "python wepscraping.py" einfach das Main Programm starten,
außerdem sollten sie sie das Modul "PrettyTable" zusätzlich installieren und natürlich "scrapy".

--> das erstellte .json file finden sie nach Ausführung im "/google_scraper/google_scraper/spiders/" directory
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#
#
------------------------------------------------------------------------ CLEANUP -------------------------------------------------------------------------------------------
Wenn sie die erstellte Datenbank und das .json file löschen wollen, lassen sie die Konfiguration im .ini file so dass die Dateien eingetragen sind die Sie löschen wollen 
und tippen sie "python remove_db_and_json.py".
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#
#
------------------------------------------------------------------------- Hints --------------------------------------------------------------------------------------------
Spezielle Generator Einträge:

O/A = Ohne Angabe (Generator wurde nicht eingetragen).
response error = Error beim besuchen der Site um den Generator String auszulesen, kann auch vom Timeout kommen.
unicode string = Unicode strings können vom Modul nicht gelesen werden, daher dieser eintrag nach dem auslesen des Generator Strings.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
