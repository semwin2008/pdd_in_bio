from torch.utils.data import Dataset, DataLoader


class ProDataset():
    self.train: Iterable
    self.valid: Iterable


class ProDataLoader():
    self.train: nn.DataLoader
    self.valid: nn.DataLoader
