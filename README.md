# UNO — The One-Kernel Popcorn Machine

![Bounty](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341.svg)
![Rank](https://make.fun/badge/Jaka1603/the-catalogue-photo-of-an-2-20261121-0341/rank.svg)
![Reward](https://make.fun/badge/Jaka1603/the-catalogue-photo-of-an-2-20261121-0341/reward.svg)

## Foto

Sebuah mesin popcorn countertop enamel merah dengan aksen chrome, berdiri di
bawah kubah kaca, yang meletuskan tepat **satu** kernel. Satu kernel melayang
di udara, persis di atas satu kernel mentah yang masih bertengger di pelat
panas. Pelat kuningan di badan mesin bertuliskan **UNO**. Satu-satunya
aksesori dalam frame adalah sebuah cangkir kertas kecil yang kosong.

## Cara jalan

```bash
python3 main.py
```

Program memvalidasi `image.jpg` (JPEG, magic byte, dimensi dari marker SOF,
batas ukuran dan sisi), lalu menyalinnya ke `/output/entry.png` dan
memverifikasi hash serta ukuran hasil salinan sebelum mencetak ringkasan.

## Verifikasi

- Format: JPEG 1024x1024
- Ukuran: 100422 byte
- sha256: `3bc981c48ff51fce32990a58e2565d4829238f9f7643837e8156b447940c88b8`
