import pandas as pd

geotitle = pd.read_csv("code/encoded_title.csv")
geoabstract= pd.read_csv("code/encoded_scholar.csv")
paper_info = pd.read_excel("code/Pub_overview.xlsx")
abstracts = pd.read_excel("code/Pub_abstract.xlsx")
abstracts = abstracts.dropna(subset=['abstract'])
casestudy_title = paper_info[paper_info['publication_title'].str.lower().str.contains("case stud")|paper_info['publication_title'].str.lower().str.contains("case stud")]
casestudy_abstract = abstracts[abstracts['abstract'].str.lower().str.contains("case stud")|abstracts['abstract'].str.lower().str.contains("case stud")]
casestudy_uri = set(casestudy_title["publication_uri"].tolist()+casestudy_abstract["publication_uri"].tolist())
casestudy_api = set(casestudy_title["publication_api"].tolist()+casestudy_abstract["publication_api"].tolist())
geoall = pd.concat([geotitle,geoabstract])
middle_table = geoall.set_index("paperId").join(paper_info.set_index("publication_uri"), how='inner')
unsdg = pd.read_excel("code/Pub_unsdg.xlsx")
topics = pd.read_excel("code/Pub_subject_journal_wos.xlsx")
middle_table = middle_table.join(unsdg.set_index("publication_uri"), how='inner',lsuffix='_left', rsuffix='_right')
middle_table = middle_table.join(topics.set_index("publication_uri"), how='inner',lsuffix='_left', rsuffix='_right')
final_table = middle_table[['lon', 'lat', 'word', 'publication_title',
       'people_uri', 'year', 'name', 'publication_api', 'keyword']].drop_duplicates()
final_table.to_excel("final.xlsx")