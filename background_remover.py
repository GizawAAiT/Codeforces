from rembg import remove
from PIL import Image

input_path = "imange.png"
output_path = "output_imange.png"

inp = Image.open(input_path)
output = remove(inp)

output.save(output_path)
Image.open(output_path)
