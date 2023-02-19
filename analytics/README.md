# Analtics for EVRAZ MISIS ANIME

[Example](./notebooks/example.ipynb)

## Installation

```bash
pip install .
```

## Usage

```python
from evraz_anime_analytics.predict import predict
from evraz_anime_analytics.helper import load_data, preprocess_data

data = load_data("path/to/data.pqt")
data = preprocess_data(data)
predict(data)
```
