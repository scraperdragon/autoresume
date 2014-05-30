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

def test_raw_iterating():
    resumer = autoresume.AutoResume('raw_iter')
    resumer.reset()
    assert list(x for x in resumer.iter(range(5))) == [0, 1, 2, 3, 4]
    assert list(x for x in resumer.iter(range(10))) == [5, 6, 7, 8, 9]

def test_iterating():
    resumer = autoresume.AutoResume('iter')
    resumer.reset()
    assert list(x for x in resumer.magic(range(5), "x{}x")) == ['x0x', 'x1x', 'x2x', 'x3x', 'x4x']
    assert list(x for x in resumer.magic(range(10), "y{}y")) == ['y5y', 'y6y', 'y7y', 'y8y', 'y9y']

def test_save_if_stopped():
    resumer = autoresume.AutoResume('stopped')
    resumer.reset()
    for x in resumer.iter(range(10)):
        if x==5:
            break
    qq = list(resumer.iter(range(10)))
    assert qq == [5, 6, 7, 8, 9], qq


def test_save_if_exception():
    resumer = autoresume.AutoResume('stopped')
    resumer.reset()

    try:
        for x in resumer.iter(range(10)):
            if x==5:
                raise IndexError
    except Exception:
        pass
    qq = list(resumer.iter(range(10)))
    assert qq == [5, 6, 7, 8, 9], qq
