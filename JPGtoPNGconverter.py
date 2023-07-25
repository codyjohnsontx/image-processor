import sys
import os
from PIL import Image

# Check if enough command-line arguments are provided (at least 3, including script name)
if len(sys.argv) >= 3:
    # Assign command-line arguments to variables
    import_folder = sys.argv[1]
    output_folder = sys.argv[2]

    # Check if the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through the files in the input folder
    for filename in os.listdir(import_folder):
        filepath = os.path.join(import_folder, filename)

        # Check if the file is a JPEG image
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            try:
                # Open the JPEG image using PIL
                img = Image.open(filepath)

                # Convert the image to PNG format and save it in the output folder
                png_filepath = os.path.join(output_folder, os.path.splitext(filename)[0] + ".png")
                img.save(png_filepath, "PNG")

                print(f"Converted {filename} to PNG.")
            except Exception as e:
                print(f"Error converting {filename}: {str(e)}")
        else:
            print(f"Skipping {filename}. It is not a JPEG image.")

else:
    print("Please provide both input and output folder paths as arguments.")
