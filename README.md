# HTX (Huobi)

HTX (Huobi) exchange plugin for bt_api, supporting Spot and Derivatives trading.

[![PyPI Version](https://img.shields.io/pypi/v/bt_api_htx.svg)](https://pypi.org/project/bt_api_htx/)
[![Python Versions](https://img.shields.io/pypi/pyversions/bt_api_htx.svg)](https://pypi.org/project/bt_api_htx/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/cloudQuant/bt_api_htx/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudQuant/bt_api_htx/actions)
[![Docs](https://readthedocs.org/projects/bt-api-htx/badge/?version=latest)](https://bt-api-htx.readthedocs.io/)

---

## English | [中文](#中文)

### Overview

This package provides **HTX (Huobi) exchange plugin for bt_api** for the [bt_api](https://github.com/cloudQuant/bt_api_py) framework. It offers a unified interface for interacting with **HTX (Huobi)** exchange.

### Features

- Spot and derivatives trading
- REST and WebSocket APIs
- Comprehensive market data
- Order management
- Balance tracking

### Installation

```bash
pip install bt_api_htx
```

Or install from source:

```bash
git clone https://github.com/cloudQuant/bt_api_htx
cd bt_api_htx
pip install -e .
```

### Quick Start

```python
from bt_api import BtApi

# Initialize
api = BtApi(
    exchange_kwargs={
        "HTX___SPOT": {
            "api_key": "your_api_key",
            "secret": "your_secret",
        }
    }
)

# Get ticker data
ticker = api.get_tick("HTX___SPOT", "btcusdt")
print(ticker)
```

### Supported Operations

| Operation | Status |
|-----------|--------|
| Ticker | ✅ |
| OrderBook | ✅ |
| Trades | ✅ |
| Bars/Klines | ✅ |
| Orders | ✅ |
| Balances | ✅ |
| Positions | ✅ |

### Online Documentation

| Resource | Link |
|----------|------|
| English Docs | https://bt-api-htx.readthedocs.io/ |
| Chinese Docs | https://bt-api-htx.readthedocs.io/zh/latest/ |
| GitHub Repository | https://github.com/cloudQuant/bt_api_htx |
| Issue Tracker | https://github.com/cloudQuant/bt_api_htx/issues |

### Requirements

- Python 3.9+
- bt_api_base >= 0.15

### Architecture

```
bt_api_htx/
├── src/bt_api_htx/     # Source code
│   ├── containers/     # Data containers
│   ├── feeds/          # API feeds
│   ├── gateway/       # Gateway adapter
│   └── plugin.py      # Plugin registration
├── tests/             # Unit tests
└── docs/             # Documentation
```

### License

MIT License - see [LICENSE](LICENSE) for details.

### Support

- Report bugs via [GitHub Issues](https://github.com/cloudQuant/bt_api_htx/issues)
- Email: yunjinqi@gmail.com

---

## 中文

### 概述

本包为 [bt_api](https://github.com/cloudQuant/bt_api_py) 框架提供 **HTX (Huobi) exchange plugin for bt_api**。它提供了与 **火币交易所** 交易所交互的统一接口。

### 功能特点

- 现货和衍生品交易
- REST 和 WebSocket API
- 全面的市场数据
- 订单管理
- 余额跟踪

### 安装

```bash
pip install bt_api_htx
```

或从源码安装：

```bash
git clone https://github.com/cloudQuant/bt_api_htx
cd bt_api_htx
pip install -e .
```

### 快速开始

```python
from bt_api import BtApi

# 初始化
api = BtApi(
    exchange_kwargs={
        "HTX___SPOT": {
            "api_key": "your_api_key",
            "secret": "your_secret",
        }
    }
)

# 获取行情数据
ticker = api.get_tick("HTX___SPOT", "btcusdt")
print(ticker)
```

### 支持的操作

| 操作 | 状态 |
|------|------|
| Ticker | ✅ |
| OrderBook | ✅ |
| Trades | ✅ |
| Bars/Klines | ✅ |
| Orders | ✅ |
| Balances | ✅ |
| Positions | ✅ |

### 在线文档

| 资源 | 链接 |
|------|------|
| 英文文档 | https://bt-api-htx.readthedocs.io/ |
| 中文文档 | https://bt-api-htx.readthedocs.io/zh/latest/ |
| GitHub 仓库 | https://github.com/cloudQuant/bt_api_htx |
| 问题反馈 | https://github.com/cloudQuant/bt_api_htx/issues |

### 系统要求

- Python 3.9+
- bt_api_base >= 0.15

### 架构

```
bt_api_htx/
├── src/bt_api_htx/     # 源代码
│   ├── containers/     # 数据容器
│   ├── feeds/          # API 源
│   ├── gateway/        # 网关适配器
│   └── plugin.py       # 插件注册
├── tests/             # 单元测试
└── docs/             # 文档
```

### 许可证

MIT 许可证 - 详见 [LICENSE](LICENSE)。

### 技术支持

- 通过 [GitHub Issues](https://github.com/cloudQuant/bt_api_htx/issues) 反馈问题
- 邮箱: yunjinqi@gmail.com
