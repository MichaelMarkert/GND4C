Custom Exporter Script to generate complex JSON with repeating elements for GND4C workflows from an OpenRefine project via the Templating Export. 
The folder contains 
- a demo dataset (person entities from the wikibase instance FactGrid (https://database.factgrid.de/wiki/Main_Page) to import to OpenRefine, 
- a JSON template of all processed elements (not a JSON schema!), and 
- a file with the script for Export=>Templating... containing all four elements needed for the Export form. Do not copy the comments ("//") as they are visible in the exported .txt-file!

Make sure that the "recordID"- resp. identifier-column does not contain duplicates before export.

<img width="907" alt="Bildschirmfoto 2023-02-28 um 08 25 31" src="https://user-images.githubusercontent.com/101104547/221783270-eb05f01d-4ccf-40a0-82bc-fc1fb8809cc7.png">
