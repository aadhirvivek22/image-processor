from compressor import Compressor
from utils import process_folder
from skimage.metrics import structural_similarity as ssim

class Optimizer:
    def __init__(self, compressor):
        self.compressor = Compressor()

    def optimize(self, input_path, output_path, output_format=None, quality=85):
        if not output_format:
            output_format = "JPEG"
        self.compressor.compress(input_path, output_path, output_format, quality)   
    