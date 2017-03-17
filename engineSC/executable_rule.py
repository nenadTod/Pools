class ExecutableRule:

    def __init__(self, priority, checker, executor):
        self.priority = priority
        self.checker = checker
        self.executor = executor

    def try_execute(self):
        if self.checker.evaluate():
            self.executor.execute()
            return True

        return False
