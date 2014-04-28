import autoresume

def test_exists():
    autoresume.AutoResume()

def test_has_a_name():
    autoresume.AutoResume().name = 'page'
    autoresume.AutoResume(name='name').name = 'name'
