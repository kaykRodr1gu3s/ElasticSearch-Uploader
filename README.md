# ElasticSearch-Uploader

## Index

1 [overview](#Overview)

2 [Requirements](#Requirements)


---

### Overview

This project, analyse and upload a csv file to [elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html) through api key with python.

---

### Requirements 

#### Elasticsearch API

  For you get your API key, you need to login and create a deployment. When your deployment is ready, follow these steps for you get your API:
  

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

#### Python libraries

For the code work, you must need to install some python libraries. They are:


```
pip install elasticsearch
pip install pandas
```
