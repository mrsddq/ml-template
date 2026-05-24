from statistics import mean


def summarize(values):
    """Return a minimal numeric summary for an iterable of values."""
    numbers = list(values)
    if not numbers:
        raise ValueError("values must not be empty")

    return {
        "count": len(numbers),
        "mean": mean(numbers),
        "minimum": min(numbers),
        "maximum": max(numbers),
    }
