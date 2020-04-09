from elasticsearch import Elasticsearch
import pprint

es = Elasticsearch(HOST="http://localhost", PORT=9200)
pp = pprint.PrettyPrinter(indent=2)


res = es.search(index="profile", body={"from": 0, "size": 10, "query": {
    "multi_match": {"query": "predictability of revenues", "fields": ["name^5", "intro^4", "location^5", "job^3", "about^3", "education^2", "skills"]}}})
pp.pprint(res)
