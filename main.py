import argparse
import time
from functions import *

def process_file(input_file_type: str, input_file_path: str):
    # takes file_type and file_path as input parameter and returns audio file in mp3 format
    start_time = time.time()
    # prechecks
    text_file_path, audio_file_path = pre_checks(input_file_path=input_file_path)

    if input_file_type == "image":
        full_text = process_image(input_file_path, text_file_path)

    if input_file_type == "pdf":
        full_text = process_pdf(input_file_path, text_file_path)

    convert_text_audio(full_text, audio_file_path)

    print(f"Done! - It took {round(time.time()-start_time, 2)} secs")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("file_type", help="Enter the file type - image, pdf")
    parser.add_argument("file_path", help="Enter the file path")
    args = parser.parse_args()

    process_file(input_file_type=args.file_type, 
                 input_file_path=args.file_path)
