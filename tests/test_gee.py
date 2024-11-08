from climate_store.gee_interface import fetch_era5_data, PeriodRange


def test_gee_api(polygons):
    data = fetch_era5_data(
        polygons,
        PeriodRange(start_period="202201", end_period="202202"),
        band_names=["temperature_2m", "total_precipitation_sum"],
    )
    assert len(data) == 2 * 2 * len(polygons.features)
