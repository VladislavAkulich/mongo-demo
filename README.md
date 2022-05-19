# Simple flask service

## Pre-requisites

- install python 3.9 verison
- install and start mongo db
- install and start **chegura** app
- use script*insert_data_into_mongo.py*before first use (it create**test** collection in a**local**db)
- install service dependencies

## Run app

```
python main/app.py

```


## Performance

Need to install**locust**tool and run tasks from perf_tests folder

```
locust -f perf_tests/<file_name>.py

```