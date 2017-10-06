# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TripSchemaTest::test_create_user 1'] = {
    'data': {
        'createUser': {
            'user': {
                'username': 'TestUser2'
            }
        }
    }
}

snapshots['TripSchemaTest::test_get_all_users 1'] = {
    'data': {
        'allUsers': [
            {
                'id': '1',
                'username': 'TestUser'
            }
        ]
    }
}

snapshots['TripSchemaTest::test_get_user 1'] = {
    'data': {
        'user': {
            'id': '1',
            'username': 'TestUser'
        }
    }
}

snapshots['TripSchemaTest::test_valid_login 1'] = {
    'data': {
        'login': {
            'user': {
                'username': 'TestUser'
            }
        }
    }
}
