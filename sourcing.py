import pandas as pd
from elasticsearch import Elasticsearch

FILENAME = 'Resources/people.csv'
es = Elasticsearch(HOST="http://localhost", PORT=9200)

df = pd.read_csv(FILENAME)
df = df.replace({pd.np.nan: None})

people = {}

for name, intro, location, job, about, education, skills, url in zip(df['Name'], df['Intro'], df['Location'], df['Job'],
                                                                     df['About'], df['Education'], df['Skills'],
                                                                     df['URL']):
    people["name"] = name
    people["intro"] = intro
    people["location"] = location
    people["job"] = job
    people["about"] = about
    people["education"] = education
    people["skills"] = skills
    people["url"] = url

    print(es.index(index="profile", doc_type="profile", body=people))
