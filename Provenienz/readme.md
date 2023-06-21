# Streamlit-App zur Recherche von GND-Provenienzmerkmalen

## Überblick
Das Script läuft nach Start im Terminal als Webserver im Browser. Die Suche wird via lobid.org auf die GND durchgeführt. Aus den GND-Datensätzen werden die URLs für die Bildquellen geparst und dann die zugehörigen Bilder aus derzeit zwei Quellen geharvestet: dem GBV-Provenienz-Wiki (https://provenienz.gbv.de/) und der Deutschen Fotothek (https://www.deutschefotothek.de/). Um den Prozess etwas zu beschleunigen, werden alle Bilder verkleinert im Unterordner "static" gecacht und bei neuen Suchen daraus geladen. Eine Suche nach Hunderten Provenienzmerkmalen dauert lokal beim ersten Mal meist mehrere Minuten.

## Installation
1. Alle im Script angegebenen Bibliotheken installieren
2. Im Scriptordner einen Unterordner "static" für den Bildcache anlegen
3. Streamlit-App starten mit dem Befehl streamlit run app.py mit einem Terminal im Ordner starten
