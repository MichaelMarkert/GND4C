import requests
import json
import xml.etree.ElementTree as ET
import pandas as pd
import streamlit as st
from PIL import Image
from bs4 import BeautifulSoup
from io import BytesIO

pd.set_option('display.max_colwidth', 30)
pd.set_option('display.max_columns', None)
#st.set_page_config(layout="wide")

st.markdown("""
            <style>
            h1 {
                font-size:2.5rem;
            }
            .block-container {
                padding-top: 0rem;
            }
            div.css-1y4p8pa {
                width: 100%;
                padding: 1rem 1rem 5rem;
                max-width: 60%;
            }
            </style>""", unsafe_allow_html=True)

try:
    with open('filelist.json', 'r', errors='ignore') as f:
        filelist = json.load(f)
except FileNotFoundError:
    filelist = []

#@st.cache
def search_gbv(searchterm):
    gnd_ids = []
    gnd_labels = []
    gbv_ids = []

    url = "https://lobid.org/gnd/search?q=" + searchterm + "&filter=type:ProvenanceCharacteristic&format=json&size=" + response_size

    response = requests.get(url)
    json_data = response.json()

    for item in json_data['member']:
        gnd_ids.append(item['gndIdentifier'])
        gnd_labels.append(item['preferredName'])

    df = pd.DataFrame({'gnd_id': gnd_ids, 'gnd_label': gnd_labels})

    def check_url(item):
        gbv_found = False
        try:
            #url = 'http://d-nb.info/gnd/' + item + '/about/marcxml'
            url = 'https://sru.bsz-bw.de/ognd!rec=2?version=1.1&query=pica.gnd+%3D+' + item + '&recordSchema=marcxmlk10os&version=1.1&maximumRecords=1'
            response = requests.get(url)

            xml_string = response.content
            root = ET.fromstring(xml_string)

            for datafield in root.findall(".//{http://www.loc.gov/MARC21/slim}datafield[@tag='670']"):
                subfield = datafield.find(".//{http://www.loc.gov/MARC21/slim}subfield[@code='u']")
                if subfield is not None:
                    # get the text content of the subfield element
                    link = subfield.text
                    # check if the link contains the target string
                    if "provenienz.gbv.de" in link:
                        gbv_found = True
                        return(link)
            if gbv_found == False:
                for datafield in root.findall(".//{http://www.loc.gov/MARC21/slim}datafield[@tag='670']"):
                    subfield = datafield.find(".//{http://www.loc.gov/MARC21/slim}subfield[@code='u']")
                    if subfield is not None:
                        # get the text content of the subfield element
                        link = subfield.text
                        # check if the link contains the target string
                        if "www.deutschefotothek.de" in link:
                            return(link)        

        except Exception as e:
            return None

    df['gbv'] = df['gnd_id'].apply(check_url)

    def download_and_resize_image(link):
        if link != None:   
            if "provenienz.gbv.de" in link:
                filepath = "static/" + link.replace('https://provenienz.gbv.de/Datei:','').replace('http://provenienz.gbv.de/Datei:','')
                if filepath not in filelist:
                    image_url = link.replace('https://provenienz.gbv.de/','https://provenienz.gbv.de/Special:FilePath/').replace('http://provenienz.gbv.de/','https://provenienz.gbv.de/Special:FilePath/')
                    response = requests.get(image_url)
                    try:
                        image = Image.open(BytesIO(response.content))

                        width, height = image.size
                        if width > height:
                            new_width = 300
                            new_height = int(height * (new_width / width))
                        else:
                            new_height = 300
                            new_width = int(width * (new_height / height))

                        resized_image = image.resize((new_width, new_height))
                    
                        resized_image.save(filepath)

                        filelist.append(filepath)
                    except:
                        filepath = "none"
                return filepath
            
            if "deutschefotothek.de" in link:
                try:
                    response = requests.get(link)
                    html_content = response.content
                    soup = BeautifulSoup(html_content, 'html.parser')   
                    download_link = soup.find('a', {'class': 'download'})
                    download_link = download_link['href']
                    filepath = "static/" + download_link.split("/")[-1]
                    if filepath not in filelist:
                        image_url = download_link
                        response = requests.get(image_url)
                        try:
                            image = Image.open(BytesIO(response.content))

                            width, height = image.size
                            if width > height:
                                new_width = 300
                                new_height = int(height * (new_width / width))
                            else:
                                new_height = 300
                                new_width = int(width * (new_height / height))

                            resized_image = image.resize((new_width, new_height))
                        
                            resized_image.save(filepath)

                            filelist.append(filepath)
                        except:
                            filepath = "none"
                    return filepath
                
                except Exception as e:
                    return None

    df['thumbnails'] = df['gbv'].apply(download_and_resize_image)

    df['thumb'] = df['gbv'].replace('https\:\/\/provenienz\.gbv\.de\/','https://provenienz.gbv.de/Special:FilePath/', regex=True).replace('http\:\/\/provenienz\.gbv\.de\/','https://provenienz.gbv.de/Special:FilePath/', regex=True)
    return df

# set up the Streamlit app

st.title("GND-Provenienmerkmale mit Bild")

col1, col2 = st.columns([2,1])

# create a text input for the search term
with col1:
    searchterm = st.text_input("Suchbegriffe", "Jena Stempel Universität")

with col2:
    response_size = st.selectbox('Maximalzahl der Treffer', [1, 10, 50, 250, 1000])

response_size = str(response_size)

# perform the search and display the results
df = search_gbv(searchterm)

def format_link(value):
    url = f"https://d-nb.info/gnd/{value}"
    return f'<a href="{url}" target="_blank">{value}</a>'

df['gnd_id'] = df['gnd_id'].apply(format_link)

def format_link(value):
    return f'<a href="{value}" target="_blank">URI des Merkmals</a>'

df['gbv'] = df['gbv'].apply(format_link)

if not df.empty:
    #df['thumbnails'] = df['thumb'].apply(lambda x: f'<img src="{x}" width="250"/>')
    df['thumbnails'] = df['thumbnails'].apply(lambda x: f'<img src="./app/{x}" width="250"/>')
    df['gnd_label'] = df['gnd_label'].str.wrap(50)

    st.write(df[['gnd_id', 'gnd_label', 'gbv', 'thumbnails']].to_html(render_links=True, escape=False).replace("\\n", "<br>"), unsafe_allow_html=True)
else:
    st.write("No results found for search term:", searchterm)

with open('filelist.json', 'w') as f:
    json.dump(filelist, f)