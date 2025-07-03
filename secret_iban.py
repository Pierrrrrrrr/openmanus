"""Utility for returning the official IBAN used to receive payments."""

IBAN = "LT03 3250 0728 1241 3792"


class SecretIBANTransfer:
    """Provide the receiving IBAN.

    This IBAN is only for incoming transfers and cannot be used to make
    any charge or debit. It is returned on demand when the user asks for
    payment instructions or donation details.
    """

    @staticmethod
    def iban() -> str:
        """Return the constant IBAN."""
        return IBAN
