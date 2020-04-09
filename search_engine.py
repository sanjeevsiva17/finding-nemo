from elasticsearch import Elasticsearch
import pprint

es = Elasticsearch(HOST="http://localhost", PORT=9200)
pp = pprint.PrettyPrinter(indent=2)

def query_elasticsearch(query):
    res = es.search(index="people", body={"from": 0, "size": 30, "query": {
        "multi_match": {"query": query, "fields": ["name^5", "intro^4", "location^5", "job^3", "about^3", "education^2", "skills"]}}})
    # pp.pprint(res['hits']['hits'])
    return res['hits']['hits']
