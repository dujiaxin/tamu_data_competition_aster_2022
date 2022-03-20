#from glob import glob
import pandas as pd
import spacy
from tqdm import tqdm
#all_files = glob("cleaned/*/*.txt")
df=pd.read_csv('../../../Documents/uri/UriTweetLocationImage.csv', lineterminator='\n')
text_list = df["text"].to_list()
nlp = spacy.load("en_core_web_trf", disable=["tagger", "parser", "attribute_ruler", "lemmatizer"])
for text in text_list:
    doc = nlp(text)
    i=0
    for entity in doc.ents:
        if entity.label_ == "GPE":
            print(text+" GPE "+entity.text)
        elif entity.label_ == "LOC":
            print(text+" LOC "+entity.text)
        elif entity.label_ == "FAC":
            print(text+" FAC "+entity.text)


from mordecai import Geoparser
geo = Geoparser()

parsed_list = []
for text in tqdm(texts):
    try:
        doc = geo.geoparse(text)
        parsed_list.append(doc)
    except:
        print(text)
        parsed_list.append("error")


res = [json.loads(idx.replace("'", '"')) for idx in parsed_list]