import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from plt_temp import create_dataframe


def test_create_dataframe():
    hours = [
        "2026-01-01T02:00",
        "2026-01-01T00:00",
        "2026-01-01T01:00",
    ]

    temps = [20.0, 10.0, 15.0]

    df = create_dataframe(hours, temps)

    assert list(df.columns) == ["time", "temperature_c"]
    assert len(df) == 3
    assert df["time"].is_monotonic_increasing

    assert list(df["temperature_c"]) == [10.0, 15.0, 20.0]
