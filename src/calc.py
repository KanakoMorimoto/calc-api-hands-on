from decimal import Decimal, getcontext, InvalidOperation
from typing import Union

getcontext().prec = 28

Number = Union[Decimal, str]


def to_decimal(value: object) -> Decimal:
    """Parse input (str/int/float/Decimal) to Decimal. Raises ValueError on invalid."""
    try:
        if isinstance(value, Decimal):
            return value
        return Decimal(str(value))
    except (InvalidOperation, TypeError) as e:
        raise ValueError(f"invalid number: {value}") from e


def multiply(a: object, b: object) -> Decimal:
    da = to_decimal(a)
    db = to_decimal(b)
    return da * db


def divide(a: object, b: object) -> Number:
    da = to_decimal(a)
    db = to_decimal(b)
    if db == Decimal('0'):
        return "Infinity"
    return da / db
