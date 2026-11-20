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
        return self.head(self.backbone)


class ProteinaTeacher(Teacher):
    pass

class BoltzTeacher(Teacher):
    pass

class FrameFlowTeacher(Teacher):
    pass



