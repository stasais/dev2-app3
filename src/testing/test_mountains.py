from dev2il_devops_app.mountains import highest_mountain
def test_highest_mountain():
    mountains = [
        {'name': 'K2', 'height': 8611},
        {'name': 'Kangchenjunga', 'height': 8586},
        {'name': 'Lhotse', 'height': 8516},
        {'name': 'Makalu', 'height': 8485},
        {'name': 'Cho Oyu', 'height': 8188}
    ]
    assert highest_mountain(mountains) == {'name': 'K2', 'height': 8611}

    mountains = []
    assert highest_mountain(mountains) is None

    mountains = [{'name': 'Mount Everest', 'height': 8848}]
    assert highest_mountain(mountains) == {'name': 'Mount Everest', 'height': 8848}

    