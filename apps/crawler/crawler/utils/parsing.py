import re
from decimal import Decimal, InvalidOperation
from typing import Optional

_NON_NUMBER_RE = re.compile(r"[^0-9,.-]+")


def normalize_whitespace(text: Optional[str]) -> str:
    if not text:
        return ""
    return " ".join(text.split())


def parse_decimal(text: Optional[str]) -> Optional[Decimal]:
    if not text:
        return None

    cleaned = _NON_NUMBER_RE.sub("", text)
    if not cleaned:
        return None

    if "," in cleaned and "." in cleaned:
        if cleaned.rfind(",") > cleaned.rfind("."):
            cleaned = cleaned.replace(".", "")
            cleaned = cleaned.replace(",", ".")
        else:
            cleaned = cleaned.replace(",", "")
    else:
        cleaned = cleaned.replace(",", ".")

    try:
        return Decimal(cleaned)
    except InvalidOperation:
        return None


def parse_int(text: Optional[str]) -> Optional[int]:
    if not text:
        return None

    cleaned = re.sub(r"[^0-9-]+", "", text)
    if not cleaned:
        return None

    try:
        return int(cleaned)
    except (InvalidOperation, ValueError):
        return None
