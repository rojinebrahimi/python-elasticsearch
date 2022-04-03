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
      "must": [],
      "filter": [
        {
          "bool": {
            "filter": [
              {
                "bool": {
                  "must_not": {
                    "bool": {
                      "should": [
                        {
                          "exists": {
                            "field": "ip2location.isp"
                          }
                        }
                      ],
                      "minimum_should_match": 1
                    }
                  }
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "query_string": {
                        "fields": [
                          "request"
                        ],
                        "query": "*mp\\4"
                      }
                    }
                  ],
                  "minimum_should_match": 1
                }
              }
            ]
          }
        }
      ]
    }
  },
  "script": {
  "inline": "ctx._source[\"ip2location.isp\"] = 'unknown'"
  }
}



es.update_by_query(body=query, doc_type='_doc', index='my_index')
