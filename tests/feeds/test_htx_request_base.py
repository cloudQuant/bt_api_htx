from unittest.mock import AsyncMock
import pytest
from bt_api_base.containers.requestdatas.request_data import RequestData
from bt_api_htx.feeds.request_base import HtxRequestData


def test_htx_defaults_exchange_name() -> None:
    request_data = HtxRequestData(public_key="public-key", private_key="secret-key")

    assert request_data.exchange_name == "HTX___SPOT"


def test_htx_request_allows_missing_extra_data(monkeypatch) -> None:
    request_data = HtxRequestData(
        public_key="public-key",
        private_key="secret-key",
        exchange_name="HTX___SPOT",
    )

    monkeypatch.setattr(
        request_data,
        "http_request",
        lambda method, url, headers, body, timeout: {"status": "ok", "data": []},
    )

    result = request_data.request("GET /market/tickers")

    assert isinstance(result, RequestData)
    assert result.get_extra_data() == {}
    assert result.get_input_data() == {"status": "ok", "data": []}


def test_htx_accepts_api_key_and_api_secret_aliases() -> None:
    request_data = HtxRequestData(api_key="public-key", api_secret="secret-key")

    assert request_data.public_key == "public-key"
    assert request_data.private_key == "secret-key"
