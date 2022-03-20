#from glob import glob
import pdb
import json
import pandas as pd
import spacy
from tqdm import tqdm
from mordecai import Geoparser
geo = Geoparser()
df = pd.read_excel("Pub_abstract.xlsx")
df = df.dropna(subset=['abstract'])
parsed_list = []
titles = []
abstracts = []
paperIds = []
place_names = []
lons = []
lats = []
words = []
countrys = []
for i in tqdm(range(0,len(df))):
    try:
        abs = df['abstract'].iloc[i]
        doc = geo.geoparse(abs)
        for single_place in doc:
            lons.append(single_place["geo"]['lon'])
            lats.append(single_place["geo"]['lat'])
            words.append(single_place["word"])
            countrys.append(single_place["country_code3"])
            abstracts.append(abs)
            titles.append(df['publication_api'].iloc[i])
            paperIds.append(df["publication_uri"].iloc[i])
    except:
        print(abs)
        continue

pdb.set_trace()
df2 =  pd.DataFrame(data={"place_name": words,
                    "lon": lons,
"lat": lats, "word": words, "title": titles, "country": countrys, "paperId": paperIds})
df2.to_json('encoded_scholar.json', orient= 'records')




