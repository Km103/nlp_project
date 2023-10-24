import re

def preprocess_text(text):
    # Remove chapter names (e.g., "Chapter 1")
    text = re.sub(r'Chapter\s+\d+', '', text)

    text = re.sub(r'CHAPTER\s+\d+', '', text)

    # Remove figures (e.g., "Figure 1")
    text = re.sub(r'Figure\s+\d+', '', text)

    # Remove tables (e.g., "Table 1")
    text = re.sub(r'Table\s+\d+', '', text)

    # Remove page numbers
    text = re.sub(r'\d+', '', text)

    # removing the watermarks
    text = re.sub(r'Free eBooks at Planet eBook.com', '', text)

    #removing special characters
    text=re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Remove extra whitespace, tabs, and newlines
    text = ' '.join(text.split())

    return text