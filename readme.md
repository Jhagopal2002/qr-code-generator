# QR Code Generator

This is a simple Python project I made to generate QR codes from text and URLs.

I created two different versions while learning how the qrcode library works in Python.

## What this project does

- Generates a QR code from a URL
- Saves the QR code as a PNG image
- Shows a basic way to create a QR code
- Includes a customized QR code with different colors

## Files in this project

### qr-code-1.py

This is the basic version of the QR code generator.

It takes my LinkedIn profile URL and creates a QR code using the `qrcode` library.

The generated QR code is saved as:

`LinkedIn Profile-1.png`

### qr-code-2.py

This is a slightly advanced version.

In this version I used `QRCode()` to control things like:

- QR code version
- Error correction
- Box size
- Border
- QR code colors

The generated QR code is saved as:

`LinkedIn Page-2.png`

## Technologies Used

- Python
- qrcode
- Pillow

## Installation

First, install the required libraries:

```bash
pip install -r requirements.txt