'''Ksheera Village Milk Co-operative payment calculator. Money and analyser readings use Decimal to avoid binary floating-point drift. Run: python milkrate.py """
from decimal import Decimal, ROUND_HALF_UP
from dataclasses import dataclass
from typing import Iterable

CENT = Decimal("0.01")
STEP = Decimal("0.1")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
BONUS_THRESHOLD = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")

@dataclass(frozen=True)
class RateCard:
    base: Decimal
    fat_step: Decimal
    snf_step: Decimal

OFF_SEASON = RateCard(Decimal("30.00"), Decimal("0.40"), Decimal("0.30"))
SEASONAL = RateCard(Decimal("32.00"), Decimal("0.45"), Decimal("0.30"))

def as_decimal(value):
    """Convert text/numeric input to Decimal without importing float error."""
    return value if isinstance(value, Decimal) else Decimal(str(value))

def get_rate_card(month):
    """Select April-June seasonal card; use original card in other months."""
    return SEASONAL if month in (4, 5, 6) else OFF_SEASON

def nearest_steps(reading, standard):
    """Return nearest 0.1 percentage-point step, with halves rounded away from zero."""
    steps = (as_decimal(reading) - standard) / STEP
    return int(steps.quantize(Decimal("1"), rounding=ROUND_HALF_UP))

def rate_per_litre(fat, snf, card=OFF_SEASON):
    """Calculate rate per litre and round to the nearest paisa."""
    rate = (card.base
            + Decimal(nearest_steps(fat, STANDARD_FAT)) * card.fat_step
            + Decimal(nearest_steps(snf, STANDARD_SNF)) * card.snf_step)
    return rate.quantize(CENT, rounding=ROUND_HALF_UP)

def payout(litres, fat, snf, card=OFF_SEASON):
    """Calculate one entry's payment, rounded to two decimal places."""
    quantity = as_decimal(litres)
    return (quantity * rate_per_litre(fat, snf, card)).quantize(
        CENT, rounding=ROUND_HALF_UP)

def ten_day_total(entries, month):
    """Return (litres total, milk payment, bonus, final payment) for entries."""
    card = get_rate_card(month)
    total_litres = Decimal("0")
    milk_total = Decimal("0.00")
    for litres, fat, snf in entries:
        q = as_decimal(litres)
        total_litres += q
        milk_total += payout(q, fat, snf, card)
    bonus = (total_litres * BONUS_PER_LITRE).quantize(
        CENT, rounding=ROUND_HALF_UP) if total_litres > BONUS_THRESHOLD else Decimal("0.00")
    return total_litres, milk_total, bonus, milk_total + bonus

def validate_entry(farmer_id, litres_text, fat_text, snf_text, shift):
    """Validate and convert one clerk/analyser entry; raise ValueError if invalid."""
    if not farmer_id.strip():
        raise ValueError("Farmer ID is required")
    if shift not in ("M", "E"):
        raise ValueError("Shift must be M (morning) or E (evening)")
    try:
        litres, fat, snf = map(Decimal, (litres_text.strip(), fat_text.strip(), snf_text.strip()))
    except Exception as exc:
        raise ValueError("Enter numeric values using a decimal point") from exc
    if not litres.is_finite() or not fat.is_finite() or not snf.is_finite():
        raise ValueError("Values must be finite numbers")
    if litres <= 0:
        raise ValueError("Litres must be greater than zero")
    if not Decimal("2.0") <= fat <= Decimal("7.0"):
        raise ValueError("Fat must be between 2.0 and 7.0 percent")
    if not Decimal("6.0") <= snf <= Decimal("10.0"):
        raise ValueError("SNF must be between 6.0 and 10.0 percent")
    return farmer_id.strip(), litres, fat, snf, shift

def _self_test():
    """Run repeatable assertions for core, seasonal and bonus requirements."""
    assert rate_per_litre("3.5", "8.5") == Decimal("30.00")
    assert rate_per_litre("4.2", "8.7") == Decimal("33.40")
    assert payout("8.5", "4.2", "8.7") == Decimal("283.90")
    assert rate_per_litre("3.1", "8.3") == Decimal("27.80")
    assert rate_per_litre("4.25", "8.63", SEASONAL) == Decimal("35.90")
    assert rate_per_litre("4.25", "8.63", OFF_SEASON) == Decimal("33.50")
    entries_500 = [("250", "3.5", "8.5"), ("250", "3.5", "8.5")]
    assert ten_day_total(entries_500, 4)[2] == Decimal("0.00")
    entries_501 = [("250", "3.5", "8.5"), ("251", "3.5", "8.5")]
    assert ten_day_total(entries_501, 4)[2] == Decimal("250.50")
    for args in [("F1", "-1", "3.5", "8.5", "M"),
                 ("F1", "10", "7.1", "8.5", "M"),
                 ("F1", "ten", "3.5", "8.5", "M")]:
        try:
            validate_entry(*args)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid input was accepted")

if __name__ == "__main__":
    _self_test()
    print("All tests passed.")
    samples = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
    for litres, fat, snf in samples:
        rate = rate_per_litre(fat, snf)
        print(f"{litres:5} L fat {fat} snf {snf} rate {rate:6.2f} pay {payout(litres, fat, snf):8.2f}")
    example = [("250", "3.5", "8.5"), ("251", "3.5", "8.5")]
    print("Seasonal ten-day summary (501 L):", ten_day_total(example, 4))
