# <center> STUDIO SOL TEST API


## Project architecture:

|Folder|Description|
|:--:|:----:|:-----:|:------:|
|core|Essential functions|
|models|Relational entities|
|routers|API routes|
|services|Operating functions layer|

## Setup:

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

## Logic test explanation

In `alpha_string.py` file, in `server` folder, i applied the following logic:

1. First, I consider that for every set of Roman letters there is, necessarily, a non-Roman letter separating each sequence.
    - So, for the following string: `AXXBLX`, the separator letter is `A` and `B`.

2. Given a sequence with pattern: $(S_ks_nS_{k+1}s_{n+1})^*$, where:
    - $S_{k}$ is k-th roman letters set;
    - $s_n$ is a separator letter and, $S_k$ and $S_{k+1}$;
    
    1. if $S_{k}$ $\in$ $[I, V, X, L, C, D, M, IV, IX, XL,  XC, CD, CM]$
        - then $S_{k}$ 