import torch.nn

class Distiller():
    def __init__(self, student, teacher, optimizer, noise_scheduler, save_path='/models/'):
        self.student_ = student
        self.teacher_ = teacher
        self.optimizer_ = optimizer
        self.noise_scheduler_ = noise_scheduler
        self.save_path_ = save_path

    def _save_to(name: str):
        state_dict = self.student.load_state_dict()
        torch.save(state_dict, self.save_path_ + name)

    def distill(n_epochs: int, ):
        criterion = nn.MSELoss()
