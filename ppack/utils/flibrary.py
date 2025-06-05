import os
from pathlib import Path


class flib:
    def __init__(self):
        self.root = Path.home()
        self.dataset = self.root / "Datasets"
        self.signal = self.root / "Signals"
        self.result = self.root / "Results"

    def read_paths(self, dataset):
        gt_folder = dataset + "-CSV"
        img_path = self.dataset / dataset
        gt_path = self.dataset / dataset / gt_folder
        signal_path = self.signal / dataset
        result_path = self.result / dataset

        return img_path, gt_path, signal_path, result_path
    
    def create_directory(path):
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            pass

    def delete_file(path):
        if os.path.isdir(path):
            os.remove(path)
        else:
            pass
