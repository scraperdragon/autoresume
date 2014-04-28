class AutoResume(object):
    def __init__(self, name='page'):
        self.name = name
        self.backend = ScraperwikiBackend()

    def save_state(self, value):
        self.backend.save(self.name, value)

    @property
    def state(self):
        return self.backend.state(self.name)


class ScraperwikiBackend(object):
    def save(self, name, value):
        import scraperwiki
        scraperwiki.sql.save_var(name, value)

    def state(self, name):
        import scraperwiki
        return scraperwiki.sql.get_var(name)
