import json

def addToDataFile(prompt, completion, file="data/outline_data_prepared.jsonl"):
    with open(file, "a") as f:
        data = {"prompt": prompt + "\nEND", "completion": completion + " END"}
        f.write(json.dumps(data) + "\n")

def outlineToDataFile(prompt, file="outline.txt"):
    with open(file, 'r') as f:
        data = f.read()
    addToDataFile(prompt, data)

outlineToDataFile("Bernie Medoff fraud. 5 sections")
