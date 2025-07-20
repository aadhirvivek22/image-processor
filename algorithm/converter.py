from PIL import Image

class Converter:
    def convert(self, input_path, output_path, output_format):
        image = Image.open(input_path)
        image.save(output_path, format=output_format.upper(), optimize=True)