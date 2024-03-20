from elasticsearch import Elasticsearch
from Tools import Csv_transformer


class elasticsearch:
    def __init__(self, api_key, elasticsearch_endpoint) -> None:

        self.api_key = api_key
        self.elasticsearch_endpoint = elasticsearch_endpoint
        

    def connecting_to_elastic(self):
        """
        This function, will connect in the elastic client.

        """

        client = Elasticsearch(
        self.elasticsearch_endpoint,
        api_key = self.api_key
        )
  
        return client
    

    def datas_to_upload(self, csv_name : str) -> list:
        """
        This function, will open the csv file and parse this.

        csv_name >>> string    
        """

        documents = Csv_transformer.Csv()
        csv_file = documents.Open_csv(csv_name)
        documents_to_upload = documents.analysing_datas(csv_listed=csv_file) 

        return documents_to_upload


    def uploading(self, client : Elasticsearch , datas: list):

        for index, doc in enumerate(datas):

            client.index(index="uploaded_with_python", body=doc, id=index)
            print(f'{index} has been uploaded')


    def Main(self):
        """
        This function, will put all the other function together
        
        """
        client = self.connecting_to_elastic()
        csv_datas = self.datas_to_upload("2022-03-14-Qakbot-with-Cobalt-Strike-and-VNC-module.csv")
        self.uploading(client=client, datas=csv_datas)
        



Elastic = elasticsearch(api_key="Your Api key HERE", elasticsearch_endpoint="The elasticsearch endpoint HERE")

Elastic.Main()