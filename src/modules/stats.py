from pathlib import Path
from rich import print


def compression_stats(original: Path, compressed: Path):
    """calcola il rapporto di compressione"""
    size_original = original.stat().st_size
    size_compress = compressed.stat().st_size
    saved_ratio = (size_original - size_compress) * 100 / size_original
    print(
        f"dimensione nuova immagine  [bold green]{(size_compress/1000):.0f}kB[/bold green] "
    )
    print(f"hai ridotto l'immagine di  [bold red]{saved_ratio:.2f}% [/bold red]")
