# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TripSchemaTest::test_create_trip_properties 1'] = {
    'data': {
        'createTrip': {
            'trip': {
                'cost': 46.5,
                'duration': '1:30:00',
                'name': 'trip',
                'places': [
                    {
                        'cost': 15.5,
                        'duration': '0:30:00',
                        'name': '0',
                        'rate': 0.0
                    },
                    {
                        'cost': 15.5,
                        'duration': '0:30:00',
                        'name': '1',
                        'rate': 0.0
                    },
                    {
                        'cost': 15.5,
                        'duration': '0:30:00',
                        'name': '2',
                        'rate': 0.0
                    }
                ],
                'rate': 0.0
            }
        }
    }
}

snapshots['TripSchemaTest::test_create_trip_with_places 1'] = {
    'data': {
        'createTrip': {
            'trip': {
                'name': 'trip',
                'places': [
                    {
                        'name': '0'
                    },
                    {
                        'name': '1'
                    },
                    {
                        'name': '2'
                    }
                ]
            }
        }
    }
}

snapshots['TripSchemaTest::test_get_all_trips 1'] = {
    'data': {
        'allTrips': [
            {
                'description': 'description',
                'name': 'Wycieczka po rynku',
                'places': [
                    {
                        'name': '0'
                    },
                    {
                        'name': '1'
                    },
                    {
                        'name': '2'
                    },
                    {
                        'name': '3'
                    },
                    {
                        'name': '4'
                    },
                    {
                        'name': '5'
                    },
                    {
                        'name': '6'
                    },
                    {
                        'name': '7'
                    },
                    {
                        'name': '8'
                    },
                    {
                        'name': '9'
                    }
                ]
            }
        ]
    }
}

snapshots['TripSchemaTest::test_get_trip_with_reviews 1'] = {
    'data': {
        'trip': {
            'description': 'description',
            'name': 'Wycieczka po rynku',
            'places': [
                {
                    'name': '0'
                },
                {
                    'name': '1'
                },
                {
                    'name': '2'
                },
                {
                    'name': '3'
                },
                {
                    'name': '4'
                },
                {
                    'name': '5'
                },
                {
                    'name': '6'
                },
                {
                    'name': '7'
                },
                {
                    'name': '8'
                },
                {
                    'name': '9'
                }
            ],
            'reviews': [
                {
                    'rate': 5,
                    'title': 'Trip 005'
                }
            ]
        }
    }
}
