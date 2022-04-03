# Python script to update/add non-exists fields from indices

from elasticsearch import Elasticsearch

es = Elasticsearch(
    ["http://address:9200"],
    http_auth=("elastic", "password"),
    timeout=30, max_retries=15, retry_on_timeout=True
)

query = {
  "query": {
    "bool": {
      "must_not": {
        "exists": {
          "field": "my_field"
        }
      }
    }
  },
  "script": {
    "inline": "ctx._source.my_field = 'unknown'"
  }
}

es.update_by_query(body=query, doc_type='_doc', index='my_index')

