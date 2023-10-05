import typer
import sys
from modules.compress import compress_png
from modules.stats import compression_stats
from pathlib import Path
from typing import Annotated, Optional


def main(
    image: Annotated[
        Optional[str],
        typer.Argument(help="il percorso all'immagine da comprimere"),
    ] = None,
    output: Annotated[
        Optional[str], typer.Argument(help="il percorso dove salvare l'immagine")
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
    cimg -s 768 -q 70  input_image.png  [output_image.png]

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
