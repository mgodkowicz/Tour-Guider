# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['PlaceSchemaTest::test_create_place_without_guide 1'] = {
    'data': {
        'createPlace': {
            'place': {
                'city': 'Wrocław',
                'description': 'description',
                'duration': '0:05:00',
                'name': 'NewPlace'
            }
        }
    }
}

snapshots['PlaceSchemaTest::test_create_place_with_guide 1'] = {
    'data': {
        'createPlace': {
            'place': {
                'city': 'Wrocław',
                'cost': 15.0,
                'description': 'description',
                'duration': '0:05:00',
                'guides': [
                    {
                        'duration': '0:10:00',
                        'name': 'Guide',
                        'place': {
                            'name': 'NewPlace'
                        },
                        'text': 'guidetext'
                    }
                ],
                'name': 'NewPlace'
            }
        }
    }
}
