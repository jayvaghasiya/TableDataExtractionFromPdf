import deepdoctection as dd
from matplotlib import pyplot as plt
import cv2
import openpyxl
import argparse


def extract(args):
	analyzer = dd.get_dd_analyzer()  # instantiate the built-in analyzer similar to the Hugging Face space demo

	df = analyzer.analyze(path=args.input_file)  # setting up pipeline
	df.reset_state()  # Trigger some initialization

	doc = iter(df)
	page = next(doc)

	image = page.viz()
	cv2.imwrite("output.png", image)

	table = page.tables[0]
	table_data = table.csv


	# create a new workbook and select the active worksheet
	workbook = openpyxl.Workbook()
	worksheet = workbook.active


	for row in table_data:
		worksheet.append(row)

	workbook.save(args.output_file)

if __name__ == "__main__":
	# Parse command line arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--input_file", required=True, help="path to input file")
	parser.add_argument("-o", "--output_file", default="output.xlsx", help="path to output file")
	args = parser.parse_args()
	extract(args)
	print("success !")

