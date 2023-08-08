# Streamlit-App zur Recherche von GND-Provenienzmerkmalen

## Überblick
Diese Anwendung ist ein Python-Script in zwei Versionen: Einer nicht mehr geupdateten Streamlit-Version und einem Jupyter-Notebook. Zweite Version wird bevorzugt, da sie einfacher geteilt und gepflegt werden kann. 
Die Suche wird via lobid.org auf die GND durchgeführt. Aus den GND-Datensätzen werden die URLs für die Bildquellen geparst und dann die zugehörigen Bilder aus derzeit zwei Quellen geharvestet: dem GBV-Provenienz-Wiki (https://provenienz.gbv.de/) und der Deutschen Fotothek (https://www.deutschefotothek.de/). Um den Prozess etwas zu beschleunigen, werden alle Bilder verkleinert im Unterordner "static" gecacht und bei neuen Suchen daraus geladen. Eine Suche nach mehreren Hundert Provenienzmerkmalen dauert lokal zumindest bei der ersten Abfrage der Bilddaten einige Minuten. <br>
Derzeit gibt es zwei Abfragemodi: Eine reguläre Suche mit Begriffen sowie eine direkte Abfrage von GND-IDs, die als kommagetrennte Liste in den Suchschlitz kopiert werden können.
