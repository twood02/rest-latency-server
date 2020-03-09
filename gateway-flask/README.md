## Stage 1

### Step 1:

Start the server

```
./server_osx 
```

### Step 2:
Start the python app.

```
python3 ./restful.py
```
The Gatewway then will run on http://127.0.0.1:5000/


### Step 3:

Hit

```
curl localhost:5000
```
Result:

```
<html><body>I RESTed for 39 time units.</body></html>
```

---
## Stage 2
### Step 1 & 2:
Do Step 1 and Step 2 like the steps in stage 1 mentioned above. 

### Step 3:
At the command line, hit 

```
curl -X POST localhost:5000/someEndPoint -d '{"numRequests": 3 }'
```

You can change the numRequests value.

Result:
```
<html><body>I made 3 requests and it took 72 milliseconds.</body></html>
```