from PIL import Image, ImageDraw, ImageFont

image = Image.new('RGB', (400, 200), color=(255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
text = "Exemple de text"

# Recomanat:
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

x = (image.width - text_width) // 2
y = (image.height - text_height) // 2

draw.text((x, y), text, font=font, fill=(0, 0, 0))
image.save("sample.png")