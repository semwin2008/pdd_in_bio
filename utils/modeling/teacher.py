import torch.nn as nn

"""
teacher models:
- proteina
- boltz
- FrameFlow
"""




class Teacher(nn.Module):
    def __init__(self,):
        self.backbone: torch.nn.Module
        self.head: torch.nn.Module

    def forward(self,):
        pass


class ProteinaTeacher(Teacher):
    pass


