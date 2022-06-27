import hypothesis.strategies as st
import pytest
from hypothesis import given

import strategies as abtem_st
from utils import gpu


@given(data=st.data())
@pytest.mark.parametrize('lazy', [True, False])
@pytest.mark.parametrize('device', ['cpu', gpu])
@pytest.mark.parametrize('measurement', [
    abtem_st.images,
    abtem_st.line_profiles,
    abtem_st.diffraction_patterns,
    abtem_st.polar_measurements
])
def test_hyperspy(data, measurement, lazy, device):
    measurement = data.draw(measurement(lazy=lazy, device=device))
    hyperspy_signal = measurement.to_hyperspy()
