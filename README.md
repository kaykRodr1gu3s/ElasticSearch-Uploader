# ElasticSearch-Uploader

## Index

1 - [overview](#Overview)

2 - [Requirements](#Requirements)

3 - [Usage](#Usage)

4 - [Result on kibana dev tool](#Result-on-kibana-dev-tool)

---

### Overview

  This project analyse and upload a csv file to [elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html) through api key with python.

---

### Requirements 

+ #### Elasticsearch API
  
    For you get your API key, you need to login and create a deployment. When your deployment is ready, follow these steps for you get your API or click here:
    
  
    ![Imagem do WhatsApp de 2024-03-21 à(s) 17 00 20_38e681bf](https://github.com/kaykRodr1gu3s/Elasticsearch-Uploader/assets/110197812/c9ae114f-6b66-4394-bdef-3f1c9d87bdc1)
  
  
  click on search, when you do this, you will be redirected to outher section, click on **new**.
  
  
  ![image](https://github.com/kaykRodr1gu3s/Elasticsearch-Uploader/assets/110197812/eddaad96-b9a2-4a19-b040-1c5d431611c7)
  
  when you create your API, you will get your credencials as a json, you will get something like this:

  
  
  ```json
  {
    "id": "Your ID",
    "name": "my_demonstration_readme",
    "expiration": "Time to expire",
    "api_key": "Your API key",
    "encoded": "encoded",
    "beats_logstash_format": "beats_logstash"
  }
  ```
  
  I recommend that you save these datas in a .txt file or anywhere that you want, because you migth need this credencial sometimes.
  
  ---


+ #### Endpoint
    For you do the connection, you need a endpoint, to you get your endpoint, it's pretty easy. it's on the same tab that you get the API.
  
    When you create your API, just copy this text:
    
    ![Imagem do WhatsApp de 2024-03-21 à(s) 17 40 02_446582d8](https://github.com/kaykRodr1gu3s/Elasticsearch-Uploader/assets/110197812/a30c1bf2-4f04-43ab-9390-ee98766b2f21)
  
    Copy the `Elasticsearch endpoint:`
    
    
  + #### Python libraries
    
    For the code work, you must need to install some python libraries. They are:


  ```
  pip install elasticsearch
  pip install pandas
  ```



### Usage

  When you have your API and your  deployments reaady, let's go configure the API and the endpoint in the code.
  
  Your API and your endpoint need to be here:
  
  ```python
  
  Elastic = elasticsearch(api_key="Your Api key HERE", elasticsearch_endpoint="The elasticsearch endpoint HERE")
  
  ```
  
  The Api key need to go as the first argument on `Your Api key HERE`, and your endpoint is the second argument on `The elasticsearch endpoint HERE`.
  
  It's possible change the index that the will be saved on elasticsearch, just need this line of code:
  
  ```python
  client.index(index="uploaded_with_python", body=doc, id=index)
  ```
  for change the index, need the rename first argument ```index="uploaded_with_python"```, you need to change the argument ```index="readme_md_example"```
  

### Result on kibana dev tool

  To have sure that the data has been uploaded, go to dev tools, follow the steps to see how to find the dev tools:

  ![Imagem do WhatsApp de 2024-03-21 à(s) 16 46 24_abe3d9f1](https://github.com/kaykRodr1gu3s/Elasticsearch-Uploader/assets/110197812/1d57c26a-a6e7-41fa-8713-769c8409bce4)

  scroll down even to **Management** section, the Dev Tool is below the Dev Tools, click there and you will be on the Dev Tools terminal.
  


  A simple query for get the first data with the index 0 is:
  
```curl 

GET uploaded_with_python/_doc/0

```

  ![image](https://github.com/kaykRodr1gu3s/Elasticsearch-Uploader/assets/110197812/55eba2af-1fb8-4923-9ba0-13087ba92fb8)




