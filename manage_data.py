import json

dataFile = 3
dataFile = "data/outline_data" + str(dataFile) + ".jsonl"

def addToDataFile(prompt, completion, file=dataFile):
    with open(file, "a") as f:
        data = {"prompt": prompt + "\nEND", "completion": completion + " END"}
        f.write(json.dumps(data) + "\n")

def outlineToDataFile(prompt, file="outline.txt"):
    with open(file, 'r') as f:
        data = f.read()
    addToDataFile(prompt, data)

# outlineToDataFile("crypto currency. 6 sections")
