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

def test_state_defaults_to_none():
    assert autoresume.AutoResume(name="not_a_name").state == None

def test_reset_state():
    unnamed = autoresume.AutoResume()
    unnamed.save_state('potato')
    assert unnamed.state == 'potato'
    unnamed.reset()
    assert unnamed.state == None, unnamed.state
