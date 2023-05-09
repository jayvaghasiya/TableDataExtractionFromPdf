# TableDataExtractionFromPdf

This is a Python tool that can detect and locate tables inside a page using DNN, and then parse the table to extract a dataframe.

## Environment Setup

To use this tool, you need to set up the environment by following these steps:

1. Create a new conda environment called "table":
   ```
   conda create -n table
   ```
2. Install PyTorch, torchvision, and torchaudio:
   ```
   conda install pytorch==1.10.0 torchvision==0.11.0 torchaudio==0.10.0 cpuonly -c pytorch
   ```
3. Install detectron2:
   ```
   python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
   ```
4. Install packaging:
   ```
   conda install packaging=21.3
   ```
5. Install Tesseract OCR:
   ```
   sudo apt update
   sudo apt install tesseract-ocr
   sudo apt install libtesseract-dev
   ```

## Running the Example

To run the tool and extract table data, use the following command:

```
python extract_table_data.py --input_file keppel-corporation-limited-annual-report-2018.pdf -o sample.xlsx
```

Replace "keppel-corporation-limited-annual-report-2018.pdf" with the name of your PDF file, and "sample.xlsx" with the name of the output Excel file that you want to create.

## License

This tool is licensed under the MIT License. Feel free to use, modify, and distribute it as you see fit.