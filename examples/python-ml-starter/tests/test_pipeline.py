from python_ml.pipeline import summarize


def test_summarize_values():
    summary = summarize([1, 2, 3])

    assert summary == {
        "count": 3,
        "mean": 2,
        "minimum": 1,
        "maximum": 3,
    }
