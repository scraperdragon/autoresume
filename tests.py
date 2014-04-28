import autoresume

def test_exists():
    autoresume.AutoResume()

def test_has_a_name():
    assert autoresume.AutoResume().name == 'page'
    assert autoresume.AutoResume(name='name').name == 'name'

def test_saves_to_db():
    unnamed = autoresume.AutoResume()
    named = autoresume.AutoResume(name='named')
    unnamed.save_state(4)
    named.save_state(5)
    assert unnamed.state == 4
    assert named.state == 5
