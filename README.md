To build docker container:
```bash
docker build -t ops .
```

To run container:
```bash
docker run -it --rm ops
```


To test:
```bash
pytest test.py
```