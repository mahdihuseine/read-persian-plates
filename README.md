# Persian License Plate Recognition and Conversion

This project demonstrates a simple implementation for recognizing Persian license plates and converting the recognized text into English. It uses the HezarAI CRNN model for Persian text recognition and includes functionality for converting Persian characters and numbers to their English equivalents.

## Features

- **Persian License Plate Recognition**: Utilizes the `hezarai/crnn-fa-64x256-license-plate-recognition` model to recognize Persian license plate text.
- **Persian to English Conversion**: Converts Persian numbers and characters into their English equivalents.
- **Text File Output**: Saves the recognized and converted text into a `.txt` file with the same name as the input image.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install the required dependencies:
   ```bash
   pip install hezarai
   ```

3. Ensure the input image (e.g., a Persian license plate image) is available in the project directory.

## Usage

1. Place the license plate image (e.g., `fa.bmp`) in the project directory.

2. Run the script:
   ```bash
   python script_name.py
   ```

3. The script will:
   - Recognize the text in the image.
   - Convert Persian characters and numbers to English.
   - Save the recognized and converted text in a `.txt` file.

   For example, if the input image is `fa.bmp`, the output will be saved in `fa_english.txt`.

## Example

Input Image: `fa.bmp`

Recognized Text: `۱۲۳ب۴۵۶`

Converted Text: `123B456`

Output File: `fa_english.txt` will contain:
```
123B456
```

## File Overview

- **`script_name.py`**: The main script for performing license plate recognition and text conversion.
- **`README.md`**: This documentation file.

## Notes

- The script assumes that the input image is a Persian license plate.
- Ensure the input image is properly preprocessed for better recognition accuracy.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to HezarAI for providing the `crnn-fa-64x256-license-plate-recognition` model for Persian text recognition.
