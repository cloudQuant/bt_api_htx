from __future__ import annotations

from bt_api_base.balance_utils import simple_balance_handler as _htx_balance_handler
from bt_api_base.registry import ExchangeRegistry
from bt_api_htx.exchange_data import (
    HtxExchangeDataCoinSwap,
    HtxExchangeDataMargin,
    HtxExchangeDataOption,
    HtxExchangeDataSpot,
    HtxExchangeDataUsdtSwap,
)
from bt_api_htx.feeds import (
    HtxAccountWssDataCoinSwap,
    HtxAccountWssDataMargin,
    HtxAccountWssDataOption,
    HtxAccountWssDataSpot,
    HtxAccountWssDataUsdtSwap,
    HtxMarketWssDataCoinSwap,
    HtxMarketWssDataMargin,
    HtxMarketWssDataOption,
    HtxMarketWssDataSpot,
    HtxMarketWssDataUsdtSwap,
    HtxRequestDataCoinSwap,
    HtxRequestDataMargin,
    HtxRequestDataOption,
    HtxRequestDataSpot,
    HtxRequestDataUsdtSwap,
)


def _htx_spot_subscribe_handler(data_queue, exchange_params, topics, bt_api):
    exchange_data = HtxExchangeDataSpot()
    kwargs = dict(exchange_params.items())
    kwargs["wss_name"] = "htx_market_data"
    kwargs["exchange_data"] = exchange_data
    kwargs["topics"] = topics
    HtxMarketWssDataSpot(data_queue, **kwargs).start()
    if not bt_api._subscription_flags.get("HTX___SPOT_account", False):
        account_kwargs = dict(kwargs.items())
        account_kwargs["topics"] = [
            {"topic": "account"},
            {"topic": "orders"},
        ]
        HtxAccountWssDataSpot(data_queue, **account_kwargs).start()
        bt_api._subscription_flags["HTX___SPOT_account"] = True


def _htx_margin_subscribe_handler(data_queue, exchange_params, topics, bt_api):
    exchange_data = HtxExchangeDataMargin()
    kwargs = dict(exchange_params.items())
    kwargs["wss_name"] = "htx_margin_market_data"
    kwargs["exchange_data"] = exchange_data
    kwargs["topics"] = topics
    HtxMarketWssDataMargin(data_queue, **kwargs).start()
    if not bt_api._subscription_flags.get("HTX___MARGIN_account", False):
        account_kwargs = dict(kwargs.items())
        account_kwargs["topics"] = [
            {"topic": "account"},
            {"topic": "orders"},
        ]
        HtxAccountWssDataMargin(data_queue, **account_kwargs).start()
        bt_api._subscription_flags["HTX___MARGIN_account"] = True


def _htx_usdt_swap_subscribe_handler(data_queue, exchange_params, topics, bt_api):
    exchange_data = HtxExchangeDataUsdtSwap()
    kwargs = dict(exchange_params.items())
    kwargs["wss_name"] = "htx_usdt_swap_market_data"
    kwargs["exchange_data"] = exchange_data
    kwargs["topics"] = topics
    HtxMarketWssDataUsdtSwap(data_queue, **kwargs).start()
    if not bt_api._subscription_flags.get("HTX___USDT_SWAP_account", False):
        account_kwargs = dict(kwargs.items())
        account_kwargs["topics"] = [
            {"topic": "account"},
            {"topic": "orders"},
        ]
        HtxAccountWssDataUsdtSwap(data_queue, **account_kwargs).start()
        bt_api._subscription_flags["HTX___USDT_SWAP_account"] = True


def _htx_coin_swap_subscribe_handler(data_queue, exchange_params, topics, bt_api):
    exchange_data = HtxExchangeDataCoinSwap()
    kwargs = dict(exchange_params.items())
    kwargs["wss_name"] = "htx_coin_swap_market_data"
    kwargs["exchange_data"] = exchange_data
    kwargs["topics"] = topics
    HtxMarketWssDataCoinSwap(data_queue, **kwargs).start()
    if not bt_api._subscription_flags.get("HTX___COIN_SWAP_account", False):
        account_kwargs = dict(kwargs.items())
        account_kwargs["topics"] = [
            {"topic": "account"},
            {"topic": "orders"},
        ]
        HtxAccountWssDataCoinSwap(data_queue, **account_kwargs).start()
        bt_api._subscription_flags["HTX___COIN_SWAP_account"] = True


def _htx_option_subscribe_handler(data_queue, exchange_params, topics, bt_api):
    exchange_data = HtxExchangeDataOption()
    kwargs = dict(exchange_params.items())
    kwargs["wss_name"] = "htx_option_market_data"
    kwargs["exchange_data"] = exchange_data
    kwargs["topics"] = topics
    HtxMarketWssDataOption(data_queue, **kwargs).start()
    if not bt_api._subscription_flags.get("HTX___OPTION_account", False):
        account_kwargs = dict(kwargs.items())
        account_kwargs["topics"] = [
            {"topic": "account"},
            {"topic": "orders"},
        ]
        HtxAccountWssDataOption(data_queue, **account_kwargs).start()
        bt_api._subscription_flags["HTX___OPTION_account"] = True


def register_htx(registry: type[ExchangeRegistry]) -> None:
    registry.register_feed("HTX___SPOT", HtxRequestDataSpot)
    registry.register_exchange_data("HTX___SPOT", HtxExchangeDataSpot)
    registry.register_balance_handler("HTX___SPOT", _htx_balance_handler)
    registry.register_stream("HTX___SPOT", "subscribe", _htx_spot_subscribe_handler)

    registry.register_feed("HTX___MARGIN", HtxRequestDataMargin)
    registry.register_exchange_data("HTX___MARGIN", HtxExchangeDataMargin)
    registry.register_balance_handler("HTX___MARGIN", _htx_balance_handler)
    registry.register_stream("HTX___MARGIN", "subscribe", _htx_margin_subscribe_handler)

    registry.register_feed("HTX___USDT_SWAP", HtxRequestDataUsdtSwap)
    registry.register_exchange_data("HTX___USDT_SWAP", HtxExchangeDataUsdtSwap)
    registry.register_balance_handler("HTX___USDT_SWAP", _htx_balance_handler)
    registry.register_stream("HTX___USDT_SWAP", "subscribe", _htx_usdt_swap_subscribe_handler)

    registry.register_feed("HTX___COIN_SWAP", HtxRequestDataCoinSwap)
    registry.register_exchange_data("HTX___COIN_SWAP", HtxExchangeDataCoinSwap)
    registry.register_balance_handler("HTX___COIN_SWAP", _htx_balance_handler)
    registry.register_stream("HTX___COIN_SWAP", "subscribe", _htx_coin_swap_subscribe_handler)

    registry.register_feed("HTX___OPTION", HtxRequestDataOption)
    registry.register_exchange_data("HTX___OPTION", HtxExchangeDataOption)
    registry.register_balance_handler("HTX___OPTION", _htx_balance_handler)
    registry.register_stream("HTX___OPTION", "subscribe", _htx_option_subscribe_handler)
