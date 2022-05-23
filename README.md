# <center> STUDIO SOL TEST API


### Without Docker
1. Requirements:
    - [Python 3.10](https://www.python.org/downloads/)

2. Dependencies:
    - In project folder, run:
    ```shell
    pip install -r requirements.txt
    ```
3. Run server:
    - In project folder, run
    ```shell
    sh app.sh
    ```

### With Docker

- In project folder, run:

```shell
sudo docker-compose up --build
```

API Rest URL:
```
http://localhost:5000/api/rest
```

API GraphQL URL:
```
http://localhost:5000/api/graphql
```

API Documentation:
- [Swagger Doc](http://localhost:5000/api/doc)
- [Red Doc](http://localhost:5000/api/docs)