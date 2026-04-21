# HTX Exchange Feed
from __future__ import annotations

from bt_api_htx.feeds.coin_swap import (
    HtxAccountWssDataCoinSwap,
    HtxMarketWssDataCoinSwap,
    HtxRequestDataCoinSwap,
)
from bt_api_htx.feeds.margin import (
    HtxAccountWssDataMargin,
    HtxMarketWssDataMargin,
    HtxRequestDataMargin,
)
from bt_api_htx.feeds.option import (
    HtxAccountWssDataOption,
    HtxMarketWssDataOption,
    HtxRequestDataOption,
)
from bt_api_htx.feeds.request_base import HtxRequestData
from bt_api_htx.feeds.spot import (
    HtxAccountWssDataSpot,
    HtxMarketWssDataSpot,
    HtxRequestDataSpot,
)
from bt_api_htx.feeds.usdt_swap import (
    HtxAccountWssDataUsdtSwap,
    HtxMarketWssDataUsdtSwap,
    HtxRequestDataUsdtSwap,
)

__all__ = [
    "HtxRequestData",
    # Spot
    "HtxRequestDataSpot",
    "HtxMarketWssDataSpot",
    "HtxAccountWssDataSpot",
    # Margin
    "HtxRequestDataMargin",
    "HtxMarketWssDataMargin",
    "HtxAccountWssDataMargin",
    # USDT Swap
    "HtxRequestDataUsdtSwap",
    "HtxMarketWssDataUsdtSwap",
    "HtxAccountWssDataUsdtSwap",
    # Coin Swap
    "HtxRequestDataCoinSwap",
    "HtxMarketWssDataCoinSwap",
    "HtxAccountWssDataCoinSwap",
    # Option
    "HtxRequestDataOption",
    "HtxMarketWssDataOption",
    "HtxAccountWssDataOption",
]
