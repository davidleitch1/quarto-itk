#!/usr/bin/env python3
"""
Create white-canvas variants of Flexoki (cream #FFFCF0) chart PNGs for docx output.

media/*.png with a cream canvas -> _media_docx/*.png with the cream replaced by white.
Images without a cream canvas (screenshots etc.) are skipped; the docx-media.lua
filter falls back to the original when no variant exists.

Incremental: a variant is regenerated only if the source is newer.
Run from anywhere:  python3 scripts/make_docx_media.py
"""

import sys
from pathlib import Path

import numpy as np
from PIL import Image

CREAM = np.array([255, 252, 240])
TOL = 10  # per-channel tolerance for "is cream"

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "media"
DST = ROOT / "_media_docx"


def has_cream_canvas(im: Image.Image) -> bool:
    """True if any corner pixel is within TOL of Flexoki paper."""
    w, h = im.size
    rgb = im.convert("RGB")
    for xy in [(2, 2), (w - 3, 2), (2, h - 3), (w - 3, h - 3)]:
        px = np.array(rgb.getpixel(xy))
        if (np.abs(px - CREAM) <= TOL).all():
            return True
    return False


def whiten(im: Image.Image) -> Image.Image:
    """Replace pixels within TOL of cream with pure white, preserving alpha."""
    has_alpha = im.mode in ("RGBA", "LA") or "transparency" in im.info
    arr = np.array(im.convert("RGBA" if has_alpha else "RGB"))
    rgb = arr[..., :3].astype(int)
    mask = (np.abs(rgb - CREAM) <= TOL).all(axis=-1)
    arr[mask, 0] = 255
    arr[mask, 1] = 255
    arr[mask, 2] = 255
    return Image.fromarray(arr)


def main() -> None:
    DST.mkdir(exist_ok=True)
    made = skipped = fresh = 0
    for src in sorted(SRC.glob("*.png")):
        dst = DST / src.name
        if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime:
            fresh += 1
            continue
        try:
            im = Image.open(src)
            im.load()
        except Exception as e:  # corrupt/odd file: leave it to the fallback
            print(f"  skip (unreadable): {src.name}: {e}", file=sys.stderr)
            continue
        if not has_cream_canvas(im):
            skipped += 1
            continue
        whiten(im).save(dst)
        made += 1
        print(f"  whitened: {src.name}")
    print(f"done: {made} converted, {fresh} up to date, {skipped} no cream canvas")


if __name__ == "__main__":
    main()
