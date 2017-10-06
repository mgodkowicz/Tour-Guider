# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['PlaceSchemaTest::test_create_place_without_guide 1'] = {
    'data': {
        'createPlace': {
            'ok': True,
            'place': {
                'duration': '0:00:50',
                'id': '2',
                'name': 'New Place'
            }
        }
    }
}

snapshots['PlaceSchemaTest::test_create_place_with_guide 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 25,
                    'line': 2
                }
            ],
            'message': 'Unknown argument "placeData" on field "createPlace" of type "Mutation".'
        },
        {
            'locations': [
                {
                    'column': 15,
                    'line': 6
                }
            ],
            'message': 'Unknown argument "guideData" on field "createPlace" of type "Mutation".'
        },
        {
            'locations': [
                {
                    'column': 13,
                    'line': 2
                }
            ],
            'message': 'Field "createPlace" argument "newPlace" of type "PlaceCreateInput!" is required but not provided.'
        }
    ]
}

snapshots['PlaceSchemaTest::test_edit_place 1'] = {
    'data': {
        'editPlace': {
            'ok': True,
            'place': {
                'id': '1',
                'name': 'Edited name 2'
            }
        }
    }
}

snapshots['PlaceSchemaTest::test_delete_place 1'] = {
    'data': {
        'deletePlace': {
            'ok': True,
            'place': {
                'name': 'Place'
            }
        }
    }
}
