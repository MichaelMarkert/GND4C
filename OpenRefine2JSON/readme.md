## *Deutsche Version*


## *English version*

Custom exporter script to generate complex JSON with nonrepeating and repeating elements for GND4C workflows from an OpenRefine project via the Templating Export. 
The folder contains 
- a demo dataset (person entities from the wikibase instance FactGrid (https://database.factgrid.de/wiki/Main_Page) to import to OpenRefine, 
- a JSON template of all processed elements (not a JSON schema!), and 
- a file containing all script blocks needed for Export=>Templating...

### Comment on the current state

- the script is work in progress
- for testing purposes every relevant element gets exported even when it is empty 

### Steps

1. Name all columns to export according to the script or change the script to fit the column names.
2. Make sure that the "recordID"- resp. dc:identifier-column does not contain duplicates before export using Facet => Customized facet => Duplicates facet. Every object needs to have an unique id!
3. Check the correct structure of more complex elements: 
    - "§" is used to mark "null"-values
    - ";" is used as a separator for labes and identifiers for an element
    - "|" is used as a separator between different values of repeating elements
    - Example: ` Technischer Zeichner;4059260-1|Animezeichner;§ `
    - Names can have up to six elements at the moment, if names are only made out of forname and surename, they need to be provided as ` surname;forname;§;§;§;§ ` 
5. Paste the script elements to the form in Export=>Templating. Do not copy the comments (marked with "//") as they are visible in the exported .txt-file.
6. Validate the exported json, e.g. using https://jsoncrack.com/editor or https://jsonformatter.org/
7. Import to the GND4C-toolbox using the Private Data Import (you need an account provided by the GND agency responsible for your institution).

<img width="907" alt="Bildschirmfoto 2023-02-28 um 08 25 31" src="https://user-images.githubusercontent.com/101104547/221783270-eb05f01d-4ccf-40a0-82bc-fc1fb8809cc7.png">
