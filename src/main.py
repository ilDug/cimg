import typer
import sys
from compress import compress_png
from pathlib import Path
from typing import Optional
from stats import compression_stats


def main(
    image: Optional[str] = typer.Argument(
        None, help="il percorso all'immagine da comprimere"
    ),
    output: Optional[str] = typer.Argument(
        None, help="il percorso dove salvare l'immagine"
    ),
    size: int = typer.Option(
        768,
        "--size",
        "-s",
        help="la dimensione massima richiesta in px dell'immagine in output",
    ),
    quality: int = typer.Option(
        70,
        "--quality",
        "-q",
        help="l'indice di qualità del salvataggio dell'immagine (default 70)",
    ),
):
    """
    python compress-image.py -s 768 -q 70 < input_image.png > output.png

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


###############################################################################
if __name__ == "__main__":
    typer.run(main)
