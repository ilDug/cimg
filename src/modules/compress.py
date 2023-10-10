from PIL import Image
import sys
import io


def compress_png(file: bytes, out_path: str = None, max_size=768, quality=70):
    """comprime il file e lo scrive nello stdout o in un file"""

    with Image.open(io.BytesIO(file)) as img:
        # Convert to RGBA to avoid issues with transparency
        img = img.convert("RGBA")

        # Get the size of the original image
        width, height = img.size

        # Calculate the aspect ratio of the original image
        aspect_ratio = width / height

        # Calculate the new width and height based
        # on the maximum size and aspect ratio
        if width > height:
            new_width = max_size
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = max_size
            new_width = int(new_height * aspect_ratio)

        # Resize the image while keeping its aspect ratio
        img = img.resize((new_width, new_height))

        # Save the compressed image as PNG
        if out_path is None:
            #  print to stdout
            img.save(sys.stdout, optimize=True, quality=quality, format="png")
        else:
            # sovrascrive il file sorgente
            img.save(out_path, optimize=True, quality=quality, format="png")
