from elasticsearch import Elasticsearch

es = Elasticsearch(
    ["http://address:9200"],
    http_auth=("elastic", "password") 
)

query = {
   "query": {
    "term": {
      "my_field": "bar"
    }
  }
}

es.delete_by_query(body=query, doc_type='_doc', index='my_index')
