from PIL import Image
from .utils import process_folder

class Compressor:
    def compress(self, input_path, output_path, output_format, quality, resize=None, strip_metadata=False): 
        image = Image.open(input_path)
        print(quality)
        print(output_format)
        self.save_image(image, output_path, output_format=output_format, quality=quality)


    @staticmethod
    def save_image(image, output_path, output_format, quality):
        image.save(output_path, quality=quality, format=output_format, optimize=True)
    

if __name__ == "__main__":
    paths = process_folder("dataset", "output")
    compressor = Compressor()
    output_format = None
    for path in paths:
        if not output_format:
            output_format = path[2].upper() if (path[2] and path[2].upper()!="JPG") else "JPEG"
        compressor.compress(path[0], path[1] + "." + path[2].lower(), output_format, 75)  
        output_format = None