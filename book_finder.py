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
import cv2
import pytesseract
import pandas as pd

# Function to process image and extract text
def extract_titles(image_path):
    # Read and preprocess image
    # Extract text using pytesseract
    # Return list of titles\
    
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


    image_path = '/path_to_image.jpg'
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
