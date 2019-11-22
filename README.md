# python_deep_learning_m2
``` 
curl -X GET \
  http://127.0.0.1:5000/ \
  -H 'Postman-Token: 1f78f028-b6fb-4638-9da1-6cf0bae6f024' \
  -H 'cache-control: no-cache'
```
Get Single Response for the comment

```
curl -X POST \
  http://localhost:5000/sentiment-analyse \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 135' \
  -H 'Content-Type: application/json' \
  -H 'Host: localhost:5000' \
  -H 'Postman-Token: 61461507-c14d-4df6-9b0c-307bd17dbbb4,d7b4e351-4efe-4a1e-87f5-1bb26a3bae0f' \
  -H 'User-Agent: PostmanRuntime/7.19.0' \
  -H 'cache-control: no-cache' \
  -d '{
	"message": "Just incredible.After a lengthy exchange on the blue Trump holds his nerve to roll it in and then win the frame to go"
}'
```


Get Multiple Response for the comment

```
curl -X POST \
  http://localhost:5000/sentiment-analyse-stream \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 45' \
  -H 'Content-Type: application/json' \
  -H 'Host: localhost:5000' \
  -H 'Postman-Token: 0b325a00-dd8b-4014-8976-dcb08c9617cc,52779434-b537-455c-9f91-b388ec3b837b' \
  -H 'User-Agent: PostmanRuntime/7.19.0' \
  -H 'cache-control: no-cache' \
  -d '{
	"time": "1",
	"writeFile": "current.txt"
}'
```
