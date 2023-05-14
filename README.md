### Getting started:
- From project dir: `docker build --tag keyvalue .`
- `docker network create flask_network`
- `docker run --network flask_network --name keyvalue -d -p 5000:5000 keyvalue`
- The app should now be running on localhost:5000. 
If that doesn't open on your browser, you can check the running docker container for the right address.

### Testing:
- This simple app exposes 3 endpoints:
  - `/store-value`, which takes either a `POST` or `PATCH` request with payload in the format 
  ```
  {
    "meta": {
        "key": "blah",
        "value": 4
    }
  }
  ```
  and stores it in the database.
- `/get-value/<k>`, which takes a `GET` request to get a key in the data store with key `k`
- `/delete-key/<k>`, which takes a `DELETE` request to delete a key in the data store with key `k`