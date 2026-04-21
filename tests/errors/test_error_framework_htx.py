"""Tests for ErrorFrameworkHtx."""

from __future__ import annotations

from bt_api_htx.errors import HtxErrorTranslator


class TestHtxErrorTranslator:
    """Tests for HtxErrorTranslator."""

    def test_error_map_exists(self):
        """Test ERROR_MAP is defined."""
        assert hasattr(HtxErrorTranslator, "ERROR_MAP")
