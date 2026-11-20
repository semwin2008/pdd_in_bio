import torch.nn as nn
from teacher import Teacher


class Student(nn.Module):
    def __init__(self, teacher: Teacher, hidden_dim, L):
        self.backbone = teacher.backbone
        out_dim: int
        self.heads = nn.Linear(out_dim, hidden_dim * L)

    def forward(self, x):
        return self.heads(self.backbone(x))
