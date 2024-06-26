# QR code Preprocessor and Decoder

This project is a QR code preprocessor and decoder implemented in Python using computer vision techniques and the OpenCV library. The goal of the project is to preprocess the QR code image provided until it's able to be decoded by a decoder provided by Eng/ Ahmad Salama.

## Features
- Reads QR codes provided it
- Applies pre-processing techniques on the qr code to enhance image quality
- Generic pre-processing is applied to the test cases
- Extract the QR code and remove quite zones
- Decodes the pre-processed QR code and print the decoded string
- Decodes only Version 1 QR codes
- Can decode alphanumeric encoded QR Codes
- Involves using reed solomon error correction technique to correct any missing data.
## Installation

1. Clone the repository:
   ````shell
   git clone https://github.com/MinaGeo/CV-Project

2. Navigate to the project directory:

   ````shell
   cd QR-Code-Preprocessor-and-Decoder

3. Install the required dependencies:

   ````shell
   pip install opencv-python
   pip install matplotlib
   pip install --upgrade reedsolo
	

## Usage
- Only works on QR Version 1.

- The program will pre-process the provided QR code, extract the QR code ; removing the quite zones, decodes it, applies reed solomon error correction, and display the decoded string.

## Contributing

Contributions to this project are welcome. If you have any ideas, suggestions, or bug fixes, please open an issue or submit a pull request.

When contributing, please ensure that your code follows the existing coding style and conventions. Add appropriate tests for any new features or bug fixes.

## Acknowledgments

- The project was inspired by the challenge of preprocessing and decoding QR Codes using computer vision techniques.
- The OpenCV library was used extensively for QR Code pre-processing and computer vision operations.
- The decoder acts implemented manually by Eng/Ahmad Salama performs all necessary algorithm and techniques to extract important information from the QR code.
- The reed solomon error correction technique was applied to retrieve any missing data bytes in the qr code.

## Contact

For any questions or inquiries, please contact [mina.george.girgis@gmail.com](mailto:your-email@example.com).

