# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TripSchemaTest::test_get_all_reviews 1'] = {
    'data': {
        'allReviews': [
            {
                'content': 'Great Trip!',
                'rate': 5,
                'title': 'Trip 002'
            }
        ]
    }
}

snapshots['TripSchemaTest::test_get_one_review 1'] = {
    'data': {
        'review': {
            'content': 'Great Trip!',
            'rate': 5,
            'title': 'Trip 003'
        }
    }
}

snapshots['TripSchemaTest::test_create_trip_review 1'] = {
    'data': {
        'createTripReview': {
            'review': {
                'content': 'good',
                'user': {
                    'id': '2',
                    'username': 'Peter'
                }
            },
            'trip': {
                'name': 'Trip 001'
            }
        }
    }
}

snapshots['TripSchemaTest::test_create_place_review 1'] = {
    'data': {
        'createPlaceReview': {
            'place': {
                'name': 'Place 002'
            },
            'review': {
                'content': 'good',
                'user': {
                    'id': '2',
                    'username': 'Peter'
                }
            }
        }
    }
}
