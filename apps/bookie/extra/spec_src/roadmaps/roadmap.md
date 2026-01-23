Roadmap

# Glossary

Book: a collection of chapters containing text content
Chapter: a section within a book containing multiple paragraphs
Paragraph: a block of text content within a chapter

# Milestones

## MS1: A user creates a book

1.  The user requests to create a new book with a title and specified number of chapters.
2.  The system creates the book with the given title.
3.  For each chapter:
    1. The system creates a chapter with a generated title.
    2. For each paragraph in the chapter (default 5 paragraphs):
       1. The system generates a paragraph with lorem ipsum text.
          1. It uses a rule to count the number of bad words.
          2. The rule for a bad word is: any word that contains the letter a or b.
          3. It drops words from the paragraph so that there are not more than N bad words.
             1. The value from N comes from the settings.py file.
       2. The system adds the paragraph to the chapter.
    3. The system adds the chapter to the book.
4.  The system returns the completed book with all chapters and paragraphs.
