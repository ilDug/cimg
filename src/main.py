import typer
import sys

from modules.compress import compress_png
from modules.stats import compression_stats

from pathlib import Path
from typing import Annotated
from pillow_heif import register_heif_opener
from PIL import Image
from rich import print

app = typer.Typer()


# ////////////////////////////////////////////////////////////////////////////
@app.command()
def compress(
    image: Annotated[
        str,
        typer.Argument(help="il percorso all'immagine da comprimere"),
    ],
    output: Annotated[
        str, typer.Argument(help="il percorso dove salvare l'immagine")
    ] = None,
    size: Annotated[
        int,
        typer.Option(
            "--size",
            "-s",
            help="la dimensione massima richiesta in px dell'immagine in output",
        ),
    ] = 768,
    quality: Annotated[
        int,
        typer.Option(
            "--quality",
            "-q",
            help="l'indice di qualità del salvataggio dell'immagine (default 70)",
        ),
    ] = 70,
):
    """
    cimg compress -s 768 -q 70  input_image.png  [output_image.png] || [ > stdout ]

    Comprime un'immagine con le dimensioni e la qualità volute.

    Passare l'immagine come stdin e salvarla con lo stdout:

    """
    if image is None:
        # se non viene passato un file con < oppure il pipe |
        # legge lo stdin dal buffer.
        image = sys.stdin.buffer.read()
    else:
        # se viene passato un riferimento al file come stringa
        # carica il path e legge i bytes da esso
        source = Path(image)
        image = source.read_bytes()

    compress_png(image, output, max_size=size, quality=quality)

    # calcola les statistiche solo se sono passate le immagni come path
    if output is not None and image is not None:
        dest = Path(output)
        compression_stats(source, dest)
    else:
        print("Compressione terminata")


# ////////////////////////////////////////////////////////////////////////////
@app.command()
def convert(
    image: Annotated[
        str,
        typer.Argument(help="il percorso all'immagine da comprimere"),
    ],
    output: Annotated[
        str, typer.Argument(help="il percorso dove salvare l'immagine")
    ] = None,
):
    """
    cimg convert input_image.heic  [output_image.png] || [ > stdout ]

    Converte l'immagine da formati tipo HEIC a JPEG.

    NON ACCETTA stdin, ma può essere salvata con lo stdout:

    """

    register_heif_opener()
    source = Path(image)
    with Image.open(source) as img:
        if output is None:
            # print oto stdout
            img.save(sys.stdout, optimize=True, format="jpeg")
            print("Coversione terminata")

        else:
            # sovrascrive il file sorgente
            img.save(output, optimize=True, format="jpeg")
            print(
                f"Coversione terminata, salvato il file: [bold green]{output}[/bold green]"
            )


# ////////////////////////////////////////////////////////////////////////////
@app.callback()
def main():
    print("cimg version 0.2.0")


###############################################################################
if __name__ == "__main__":
    # typer.run(main)
    app()
