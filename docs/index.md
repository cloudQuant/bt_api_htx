# HTX (Huobi) Documentation

## English

Welcome to the HTX (Huobi) documentation for bt_api.

### Quick Start

```bash
pip install bt_api_htx
```

```python
from bt_api_htx import HTXApi
feed = HTXApi(api_key="your_key", secret="your_secret")
ticker = feed.get_ticker("btcusdt")
```

## 中文

欢迎使用 bt_api 的 火币交易所 文档。

### 快速开始

```bash
pip install bt_api_htx
```

```python
from bt_api_htx import HTXApi
feed = HTXApi(api_key="your_key", secret="your_secret")
ticker = feed.get_ticker("btcusdt")
```

## API Reference

See source code in `src/bt_api_htx/` for detailed API documentation.
