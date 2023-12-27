"""
A Python script to process the image and extract text from the spines of books. The basic flow would be:

Read the Image: Use OpenCV to load the image.
Preprocess the Image: Convert to grayscale, apply filters, or resize if necessary to improve OCR accuracy.
Text Extraction: Use Pytesseract to extract text from the processed image.

-Data Handling and Export to Excel
After extracting the text, you'll need to clean and organize it:

Clean the Text: Trim, remove unwanted characters, or fix common OCR errors.
Create a DataFrame: Use Pandas to create a DataFrame with the book titles.
Export to Excel: Use Pandas to export this data to an Excel sheet.

-Implementing a Search Functionality
For the search functionality, you can write a function that takes a user input (the book title or part of it) and searches the DataFrame:

User Input: Allow the user to input the search query.
Search: Search the DataFrame for the given title.
Display Results: Display the results back to the user.

"""
import os
import cv2 as cv # Computer vision library to process and edit our image
import sys
import pytesseract # OCR library to extract text from image
import pandas as pd


# Function to process the image and prepare for text extraction
def process_image(image_path):
    img = cv.imread(cv.samples.findFile(image_path)) # Import the image using cv2

    if img is None: # Safety stop incase image does not exist
        sys.exit("Could not read the image.")
    
    gray_scale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # Convert the image into grayscale
    high_contrast_img = cv.equalizeHist(gray_scale_img) # Increase contrast of image
    




    #d = pytesseract.image_to_data(gray_scale_img, output_type=pytesseract.Output.DICT) # Dectecting text in image to increase contrast in its area
    #print(d) 

    

    cv.imshow("Display window", high_contrast_img) # Display the image for test purposes

    k = cv.waitKey(0) # A way to exit the window

    if k == ord("s"): # If 's' key is pressed, save the image as the following .png file and close the window
        cv.imwrite("book_spines.png", high_contrast_img)
    



# Function to process image and extract text
def extract_titles(image_path):
    # Read and preprocess image
    # Extract text using pytesseract
    # Return list of titles
    process_image(image_path)


    pass

# Function to search titles in the DataFrame
def search_titles(dataframe, query):
    # Search for the query in the dataframe
    # Return matching titles
    pass

# Main function
def main():
    # Change current directory to the directory of the Python file
    script_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_directory)
    print("Current Working Directory:", os.getcwd())

    pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

    image_path = '../book_finder/book_spine_test.jpg'
    titles = extract_titles(image_path)
    
    # Create DataFrame and export to Excel
    df = pd.DataFrame(titles, columns=['Book Titles'])
    df.to_excel('../book_finder/book_titles.xlsx', index=False)

    # Search functionality
    query = input("Enter a book title to search: ")
    results = search_titles(df, query)
    print("Search Results:", results)

if __name__ == "__main__":
    main()
