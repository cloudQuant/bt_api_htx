from __future__ import annotations

from bt_api_base.gateway.registrar import GatewayRuntimeRegistrar
from bt_api_base.plugins.protocol import PluginInfo
from bt_api_base.registry import ExchangeRegistry

from bt_api_htx import __version__
from bt_api_htx.registry_registration import register_htx


def register_plugin(
    registry: type[ExchangeRegistry], runtime_factory: type[GatewayRuntimeRegistrar]
) -> PluginInfo:
    """Register HTX assets, feeds, and streams in the plugin host."""
    register_htx(registry)

    return PluginInfo(
        name="bt_api_htx",
        version=__version__,
        core_requires=">=0.15,<1.0",
        supported_exchanges=(
            "HTX___SPOT",
            "HTX___MARGIN",
            "HTX___USDT_SWAP",
            "HTX___COIN_SWAP",
            "HTX___OPTION",
        ),
        supported_asset_types=("SPOT", "MARGIN", "SWAP", "OPTION"),
    )
