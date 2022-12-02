# Fetch Rewards Coding Assessment - Machine Learning Engineer

## Files
* image_pixel_coordinate.py
* main.py
* Dockerfile
* requirements.txt

## How to run
### In python
1. Run main.py
2. Run the following code in pyhton environment.

```
import requests, json

url="http://localhost:8000/api"
data = json.dumps({"dimension":(4, 4), "corner points":  [(1, 1), (4, 1), (1, 4), (4, 4)]})
r = requests.post(url, data)
print(r.json())
```

### In Docker
1. Build the image 
```
docker image build -t mle_test .
```
2. Run the container
```
docker run mle_test
```
3. Test with curl
```
curl -X POST http://localhost:8000/api -d "{\"dimension\": [4,4],\"corner points\":[[1, 1], [4, 1], [1, 4],[4, 4]]}"
```
