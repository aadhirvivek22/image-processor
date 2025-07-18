from PIL import Image
from utils import process_folder

class Compressor:
    def compress(self, input_path, output_path, output_format, quality, resize=None, strip_metadata=False): 
        image = Image.open(input_path)
        self.save_image(image, output_path, output_format, quality)


    @staticmethod
    def save_image(image, output_path, output_format, quality):
        image.save(output_path, quality=quality, format=output_format)
    

if __name__ == "__main__":
    paths = process_folder("dataset", "output")
    compressor = Compressor()
    for path in paths:
        compressor.compress(path[0], path[1], "JPEG", 50, resize=(800, 600), strip_metadata=True)  