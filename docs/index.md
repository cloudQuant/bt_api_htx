# HTX (Huobi) Documentation

## English

Welcome to the HTX (Huobi) documentation for bt_api.

### Quick Start

```bash
pip install bt_api_htx
```

```python
from bt_api import BtApi

api = BtApi(
    exchange_kwargs={
        "HTX___SPOT": {
            "api_key": "your_api_key",
            "secret": "your_secret",
        }
    }
)
ticker = api.get_tick("HTX___SPOT", "btcusdt")
print(ticker)
```

## 中文

欢迎使用 bt_api 的 火币交易所 文档。

### 快速开始

```bash
pip install bt_api_htx
```

```python
from bt_api import BtApi

api = BtApi(
    exchange_kwargs={
        "HTX___SPOT": {
            "api_key": "your_api_key",
            "secret": "your_secret",
        }
    }
)
ticker = api.get_tick("HTX___SPOT", "btcusdt")
print(ticker)
```

## API Reference

See source code in `src/bt_api_htx/` for detailed API documentation.
