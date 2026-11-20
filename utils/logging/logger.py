import tensorboard


class Logger:
    def __init__(self, config):
        experiment_name: str
        logger_path: str
        self.path = logger_path + experiment_name

        # TODO: create tensorboard writer

        raise NotImplementedError
    
    def add(self, ):
        raise NotImplementedError
