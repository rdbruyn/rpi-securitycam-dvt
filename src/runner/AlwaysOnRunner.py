from .Runner import Runner


class AlwaysOnRunner(Runner):
    def start(self):
        # no start condition
        pass

    def should_run(self):
        return True
