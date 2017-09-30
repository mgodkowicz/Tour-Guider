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
                'title': 'Trip 000'
            }
        ]
    }
}

snapshots['TripSchemaTest::test_get_one_review 1'] = {
    'data': {
        'review': {
            'content': 'Great Trip!',
            'rate': 5,
            'title': 'Trip 001'
        }
    }
}
