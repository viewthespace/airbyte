#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#

from pytest import fixture


@fixture
def config():
    return {"api_token": "<Your API Key>", "date_from": "2021-07-01", "public_hash_id": ""}
