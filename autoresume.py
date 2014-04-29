import scraperwiki


class AutoResumeError(Exception):
    pass


class NoSentinelError(AutoResumeError):
    """The saved value was not found in the iterator."""
    pass


class AutoResume(object):
    def __init__(self, name='page'):
        self.name = name
        self.backend = ScraperwikiBackend()

    def save_state(self, value):
        self.backend.save(self.name, value)

    def reset(self):
        self.backend.save(self.name, None)

    @property
    def state(self):
        return self.backend.state(self.name)

    def iter(self, iterator):
        prev_item = None
        sentinel = self.state
        found_sentinel = sentinel is None
        yielded = False
        for item in iterator:
            if found_sentinel:
                yielded = True
                try:
                    yield item
                except:
                    if prev_item:
                        self.save_state(prev_item)
                    raise
                prev_item = item
            elif item == sentinel:
                found_sentinel = True
                continue
        self.save_state(item)
        if not yielded and not found_sentinel:
            raise NoSentinelError(sentinel)

    def magic(self, iterator, template="{}"):
        for item in self.iter(iterator):
            yield template.format(item)


class ScraperwikiBackend(object):
    def save(self, name, value):
        if value is None:
            # TODO fix in dumptruck
            scraperwiki.sql.execute("delete from swvariables where name=?", name)
            scraperwiki.sql.commit()
        else:
            scraperwiki.sql.save_var(name, value)

    def state(self, name):
        return scraperwiki.sql.get_var(name)
