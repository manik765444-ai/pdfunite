# main.py

import os
from PyPDF2 import PdfMerger
import sys

def merge_pdfs(pdf_list, output_path):
    """
    Merge multiple PDF files into a single PDF.

    Args:
        pdf_list (list of str): List of paths to input PDF files.
        output_path (str): Path where the merged PDF will be saved.

    Raises:
        FileNotFoundError: If any of the input PDF files cannot be found.
        ValueError: If the list of PDFs is empty.
        Exception: For any other errors that occur during the merging process.
    """
    if not pdf_list:
        raise ValueError("The list of PDF files is empty. Please provide at least one PDF to merge.")
    
    merger = PdfMerger()

    try:
        for pdf in pdf_list:
            if not os.path.isfile(pdf):
                raise FileNotFoundError(f"The file '{pdf}' does not exist.")
            merger.append(pdf)

        merger.write(output_path)
        print(f"PDFs merged successfully into '{output_path}'.")
    except Exception as e:
        print(f"An error occurred while merging PDFs: {e}")
        raise
    finally:
        merger.close()


def get_pdf_files_from_directory(directory):
    """
    Get a list of all PDF files in the given directory.

    Args:
        directory (str): Path to the directory to scan for PDFs.

    Returns:
        list of str: List of PDF file paths in the directory.

    Raises:
        FileNotFoundError: If the directory does not exist.
        ValueError: If there are no PDF files in the directory.
    """
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")

    pdf_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.pdf')]

    if not pdf_files:
        raise ValueError(f"No PDF files found in the directory '{directory}'.")

    return pdf_files


if __name__ == "__main__":
    # Command-line interface for the PDF merger
    try:
        if len(sys.argv) < 3:
            print("Usage: python main.py <directory_with_pdfs> <output_pdf_path>")
            sys.exit(1)

        input_directory = sys.argv[1]
        output_file = sys.argv[2]

        # Get the list of PDF files from the specified directory
        pdf_files = get_pdf_files_from_directory(input_directory)

        # Merge the PDFs into a single output file
        merge_pdfs(pdf_files, output_file)

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except ValueError as val_error:
        print(f"Error: {val_error}")
    except Exception as gen_error:
        print(f"An unexpected error occurred: {gen_error}")