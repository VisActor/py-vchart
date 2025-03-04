from ..render import engine


class ChartMixin:
    def add_js_funcs(self, *fns):
        for fn in fns:
            self.js_functions.add(fn)
        return self

    def add_js_events(self, *fns):
        for fn in fns:
            self.js_events.add(fn)
        return self

    def load_javascript(self):
        return engine.load_javascript(self)
