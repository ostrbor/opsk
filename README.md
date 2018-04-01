**Use in Docker container**

To build docker image:
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

**Use as package**
```bash
pip install git+https://github.com/ostrbor/opsk.git
```
```python
from opsk import lib
```
