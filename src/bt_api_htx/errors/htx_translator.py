"""
HTX Error Translator

Translate HTX (Huobi) API error codes to unified error codes
"""

from __future__ import annotations

from bt_api_base.error import ErrorCategory, ErrorTranslator, UnifiedError, UnifiedErrorCode


class HtxErrorTranslator(ErrorTranslator):
    """
    HTX Error Translation

    HTX uses 'status' field in responses:
    - 'ok': Success
    - 'error': Error (with 'err-code' and 'err-msg' fields)

    Common error codes from HTX API documentation.
    """

    ERROR_MAP = {
        # Authentication errors
        "api-signature-not-valid": (UnifiedErrorCode.INVALID_SIGNATURE, "Invalid signature"),
        "api-signature-check-failed": (
            UnifiedErrorCode.INVALID_SIGNATURE,
            "Signature check failed",
        ),
        "api-key-invalid": (UnifiedErrorCode.INVALID_API_KEY, "Invalid API key"),
        "api-key-expired": (UnifiedErrorCode.SESSION_EXPIRED, "API key expired"),
        "api-key-ip-invalid": (UnifiedErrorCode.PERMISSION_DENIED, "IP not in whitelist"),
        "api-key-permission-invalid": (UnifiedErrorCode.PERMISSION_DENIED, "Permission denied"),
        # Account errors
        "account-frozen-balance-insufficient-error": (
            UnifiedErrorCode.INSUFFICIENT_BALANCE,
            "Insufficient balance",
        ),
        "account-api-trading-banned": (
            UnifiedErrorCode.PERMISSION_DENIED,
            "API trading banned for account",
        ),
        "account-invalid": (UnifiedErrorCode.INVALID_PARAMETER, "Invalid account"),
        # Order errors
        "order-orderstate-error": (UnifiedErrorCode.INVALID_ORDER, "Invalid order state"),
        "order-queryorder-invalid": (UnifiedErrorCode.ORDER_NOT_FOUND, "Order not found"),
        "order-update-error": (UnifiedErrorCode.ORDER_ERROR, "Order update failed"),
        "order-place-error": (UnifiedErrorCode.ORDER_ERROR, "Order placement failed"),
        "order-cancel-error": (UnifiedErrorCode.ORDER_CANCEL_FAILED, "Order cancellation failed"),
        # Trading errors
        "base-symbol-error": (UnifiedErrorCode.INVALID_SYMBOL, "Invalid trading pair"),
        "base-amount-error": (UnifiedErrorCode.INVALID_VOLUME, "Invalid amount"),
        "base-price-error": (UnifiedErrorCode.INVALID_PRICE, "Invalid price"),
        "base-symbol-trading-banned": (
            UnifiedErrorCode.MARKET_CLOSED,
            "Trading disabled for symbol",
        ),
        # System errors
        "gateway-internal-error": (UnifiedErrorCode.INTERNAL_ERROR, "Internal server error"),
        "system-busy": (UnifiedErrorCode.EXCHANGE_OVERLOADED, "System busy"),
        "maintenance": (UnifiedErrorCode.EXCHANGE_MAINTENANCE, "System under maintenance"),
        # Rate limiting
        "too-many-requests": (UnifiedErrorCode.RATE_LIMIT_EXCEEDED, "Rate limit exceeded"),
    }

    @classmethod
    def translate(cls, raw_error, venue: str = "HTX"):
        """Translate HTX error response to unified error

        Args:
            raw_error: Raw error response from HTX
            venue: Exchange venue name (default: "HTX")

        Returns:
            UnifiedError or None
        """
        if isinstance(raw_error, str):
            # String error messages
            return cls.translate_string_error(raw_error, venue)
        elif isinstance(raw_error, dict):
            # Dictionary error responses
            return cls.translate_dict_error(raw_error, venue)

        # Fallback: treat as generic error
        return cls._translate_fallback(raw_error, venue)

    @classmethod
    def translate_string_error(cls, error_msg: str, venue: str):
        """Translate string error messages"""
        # Common error patterns
        error_lower = error_msg.lower()

        if "invalid api key" in error_lower:
            return cls._create_unified_error(UnifiedErrorCode.INVALID_API_KEY, "Invalid API key", venue, error_msg)
        elif "invalid signature" in error_lower or "signature not valid" in error_lower:
            return cls._create_unified_error(UnifiedErrorCode.INVALID_SIGNATURE, "Invalid signature", venue, error_msg)
        elif "rate limit" in error_lower or "too many requests" in error_lower:
            return cls._create_unified_error(
                UnifiedErrorCode.RATE_LIMIT_EXCEEDED, "Rate limit exceeded", venue, error_msg
            )
        elif "insufficient balance" in error_lower:
            return cls._create_unified_error(
                UnifiedErrorCode.INSUFFICIENT_BALANCE, "Insufficient balance", venue, error_msg
            )
        elif "order not found" in error_lower:
            return cls._create_unified_error(UnifiedErrorCode.ORDER_NOT_FOUND, "Order not found", venue, error_msg)
        elif "symbol" in error_lower and ("invalid" in error_lower or "not found" in error_lower):
            return cls._create_unified_error(UnifiedErrorCode.INVALID_SYMBOL, "Invalid trading pair", venue, error_msg)
        elif "permission" in error_lower:
            return cls._create_unified_error(UnifiedErrorCode.PERMISSION_DENIED, "Permission denied", venue, error_msg)
        elif "maintenance" in error_lower:
            return cls._create_unified_error(
                UnifiedErrorCode.EXCHANGE_MAINTENANCE, "System under maintenance", venue, error_msg
            )

        # Fallback for unknown string errors
        return cls._create_unified_error(UnifiedErrorCode.INTERNAL_ERROR, error_msg, venue, error_msg)

    @classmethod
    def translate_dict_error(cls, error_dict: dict, venue: str):
        """Translate dictionary error responses

        HTX error format:
        {
            "status": "error",
            "err-code": "error-code",
            "err-msg": "error message"
        }
        """
        # Check status first
        status = error_dict.get("status", "")
        if status == "ok":
            return None  # Success

        # Extract error code and message
        err_code = error_dict.get("err-code", "")
        err_msg = error_dict.get("err-msg", "")

        if err_code in cls.ERROR_MAP:
            unified_code, default_msg = cls.ERROR_MAP[err_code]
            return cls._create_unified_error(unified_code, err_msg or default_msg, venue, f"{err_code}: {err_msg}")

        # Check for specific error patterns in message
        if err_msg:
            return cls.translate_string_error(err_msg, venue)

        # Fallback for unknown error codes
        return cls._create_unified_error(
            UnifiedErrorCode.INTERNAL_ERROR,
            f"Unknown error code: {err_code}",
            venue,
            f"{err_code}: {err_msg}",
        )

    @classmethod
    def _create_unified_error(cls, code, message, venue, original_error):
        """Create a unified error instance"""
        # Determine category based on code
        if code in [
            UnifiedErrorCode.INVALID_API_KEY,
            UnifiedErrorCode.INVALID_SIGNATURE,
            UnifiedErrorCode.SESSION_EXPIRED,
        ]:
            category = ErrorCategory.AUTH
        elif code in [
            UnifiedErrorCode.INVALID_SYMBOL,
            UnifiedErrorCode.INVALID_PRICE,
            UnifiedErrorCode.INVALID_VOLUME,
            UnifiedErrorCode.ORDER_NOT_FOUND,
            UnifiedErrorCode.ORDER_ERROR,
            UnifiedErrorCode.ORDER_CANCEL_FAILED,
            UnifiedErrorCode.MARKET_CLOSED,
        ]:
            category = ErrorCategory.ORDER
        elif code == UnifiedErrorCode.RATE_LIMIT_EXCEEDED:
            category = ErrorCategory.RATE_LIMIT
        elif code in [
            UnifiedErrorCode.INTERNAL_ERROR,
            UnifiedErrorCode.EXCHANGE_MAINTENANCE,
            UnifiedErrorCode.EXCHANGE_OVERLOADED,
        ]:
            category = ErrorCategory.SYSTEM
        else:
            category = ErrorCategory.BUSINESS

        return UnifiedError(
            code=code,
            category=category,
            venue=venue,
            message=message,
            original_error=original_error,
            context={"raw_response": original_error},
        )

    @classmethod
    def _translate_fallback(cls, raw_error, venue: str):
        """Fallback translation for unknown error formats"""
        return cls._create_unified_error(UnifiedErrorCode.INTERNAL_ERROR, "Unknown error", venue, str(raw_error))
