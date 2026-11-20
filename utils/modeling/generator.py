import torch


class ProGenerator():
    def __init__(model_class, model_config, from_path):
        self.model = model_class(**model_config)
        state_dict = torch.load(from_path)
        self.model.load_state_dict(state_dict)

        # TODO: fuse model heads

    def generate_from_noise(noise: torch.Tensor, nfe: int):
        pass

    def generate(n_samples: int, nfe: int):
        pass
