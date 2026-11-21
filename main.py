#!/usr/bin/env python3
"""UNO — The One-Kernel Popcorn Machine.

Memvalidasi foto katalog image.jpg lalu menyalinnya ke /output/entry.png
dengan verifikasi integritas penuh. Hanya Python 3 stdlib, tanpa network.
"""

import hashlib
import shutil
import sys
from pathlib import Path

MAX_BYTES = 1_048_576
MAX_SIDE = 1024


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_dimensions(data):
    """Pindai marker JPEG sampai SOF dan kembalikan (lebar, tinggi)."""
    if data[:3] != b"\xff\xd8\xff":
        raise ValueError("bukan file JPEG (magic byte salah)")
    pos = 2
    while pos < len(data) - 1:
        if data[pos] != 0xFF:
            pos += 1
            continue
        marker = data[pos + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            height = (data[pos + 5] << 8) | data[pos + 6]
            width = (data[pos + 7] << 8) | data[pos + 8]
            return width, height
        if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        segment_len = (data[pos + 2] << 8) | data[pos + 3]
        pos += 2 + segment_len
    raise ValueError("marker SOF tidak ditemukan")


def main():
    source = Path(__file__).resolve().parent / "image.jpg"
    if not source.exists():
        print("gagal: image.jpg tidak ditemukan di sebelah main.py", file=sys.stderr)
        return 1

    data = source.read_bytes()
    if len(data) > MAX_BYTES:
        print(f"gagal: ukuran {len(data)} byte melebihi batas {MAX_BYTES}", file=sys.stderr)
        return 1

    try:
        width, height = read_dimensions(data)
    except ValueError as exc:
        print(f"gagal: {exc}", file=sys.stderr)
        return 1

    if width > MAX_SIDE or height > MAX_SIDE:
        print(f"gagal: dimensi {width}x{height} melebihi batas {MAX_SIDE}", file=sys.stderr)
        return 1

    digest = hashlib.sha256(data).hexdigest()

    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)

    # Baca ulang hasil dan bandingkan hash + ukuran.
    copied = target.read_bytes()
    if hashlib.sha256(copied).hexdigest() != digest or len(copied) != len(data):
        print("gagal: hash atau ukuran hasil salinan tidak identik", file=sys.stderr)
        return 1

    print("format=jpeg")
    print(f"width={width}")
    print(f"height={height}")
    print(f"bytes={len(data)}")
    print(f"sha256={digest}")
    print(f"output={target}")
    print("status=ok")
    print("verified=hash_and_size_match")
    print(f"limits=max_bytes={MAX_BYTES} max_side={MAX_SIDE} passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
