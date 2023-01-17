from jared_bot import generateOutline
from manage_data import outlineToDataFile

if __name__ == "__main__":
    prompt = "President Obama"
    # generateOutline(prompt, 3)
    outlineToDataFile(prompt + ". 5 sections")