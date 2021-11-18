#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#
import pytest as pytest

from airbyte_cdk.models import SyncMode
from source_mailgun.source import Domains, Events, IncrementalMailgunStream
from . import TEST_CONFIG


@pytest.mark.parametrize(
    "stream, cursor_field",
    [
        (IncrementalMailgunStream(), []),
        (Domains(), []),
        (Events(TEST_CONFIG), "timestamp"),
    ]
)
def test_cursor_field(stream, cursor_field):
    assert stream.cursor_field == cursor_field


@pytest.mark.parametrize(
    "stream, current_stream_state, latest_record, expected_state",
    [
        (IncrementalMailgunStream(), None, None, {}),

        (Events(TEST_CONFIG), None, None, {"timestamp": 0}),
        (Events(TEST_CONFIG), {"timestamp": 1000}, {"timestamp": 2000}, {"timestamp": 2000}),
        (Events(TEST_CONFIG), {"timestamp": 2000}, {"timestamp": 1000}, {"timestamp": 2000}),
    ]
)
def test_get_updated_state(stream, current_stream_state, latest_record, expected_state):
    inputs = {"current_stream_state": current_stream_state, "latest_record": latest_record}
    assert stream.get_updated_state(**inputs) == expected_state


@pytest.mark.parametrize(
    "stream, inputs, expected_stream_slice",
    [
        (IncrementalMailgunStream(), {"sync_mode": SyncMode.incremental}, [None]),
        (Events(TEST_CONFIG), {"stream_state": {"timestamp": 1000}}, [{"timestamp": 1000}]),
    ]
)
def test_stream_slices(stream, inputs, expected_stream_slice):
    assert stream.stream_slices(**inputs) == expected_stream_slice


@pytest.mark.parametrize(
    "stream, support_incremental",
    [
        (Domains(), False),
        (Events(TEST_CONFIG), True),
    ]
)
def test_supports_incremental(stream, support_incremental):
    assert stream.supports_incremental == support_incremental


@pytest.mark.parametrize(
    "stream, source_defined_cursor",
    [
        (Domains(), True),
        (Events(TEST_CONFIG), True),
    ]
)
def test_source_defined_cursor(stream, source_defined_cursor):
    assert stream.source_defined_cursor == source_defined_cursor


@pytest.mark.parametrize(
    "stream, state_checkpoint_interval",
    [
        (Domains(), None),
        (Events(TEST_CONFIG), None),
    ]
)
def test_stream_checkpoint_interval(stream, state_checkpoint_interval):
    assert stream.state_checkpoint_interval == state_checkpoint_interval