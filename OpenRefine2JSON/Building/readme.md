## *Deutsche Version*


## *English version*

Custom exporter script to generate complex JSON with nonrepeating and repeating elements for GND4C workflows from an OpenRefine project via the Templating Export. 
The folder contains 
- a JSON template of all processed elements (not a JSON schema!), and 
- a file containing all script blocks needed for Export=>Templating...

### Comment on the current state

- template and script are work in progress - some elements were not used up to now (like GND identifiers for affiliations) so they are not represented in the exporter script
- for testing purposes every relevant element gets exported even when it is empty 

### Steps

1. Name all columns to export according to the script or change the script to fit the column names.
2. Make sure that the "recordID"- resp. dc:identifier-column does not contain duplicates before export using Facet => Customized facet => Duplicates facet. Every object needs to have an unique id!
3. Paste the script elements to the form in Export=>Templating. Do not copy the comments (marked with "//") as they are visible in the exported .txt-file.
4. Validate the exported json, e.g. using https://jsoncrack.com/editor or https://jsonformatter.org/
5. Import to the GND4C-toolbox using the Private Data Import (you need an account provided by the GND agency responsible for your institution).