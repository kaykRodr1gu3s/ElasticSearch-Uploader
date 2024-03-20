from elasticsearch import Elasticsearch



client = Elasticsearch(
   "endpoint",
  api_key="API"
)


simple_example_upload = [
    {'Name': "kayk", 'language': 'Python'}
    ]

client.index(index="simple_example_to_upload", body=simple_example_upload[0], id=0)

