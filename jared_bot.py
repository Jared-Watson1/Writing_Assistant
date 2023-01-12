import openai, os, random
from dotenv import load_dotenv
from manage_data import addToDataFile

load_dotenv()
ada = "text-ada-001"
davinci = "text-davinci-003"
curie = "text-curie-001"

openai.api_key = os.getenv("OPENAI_API_KEY")

def generateOutline(prompt, length):
    mainIdeas = generateMainIdeas(prompt)
    prompt = f"Create an outline for a paper which consists of an {length} paragraphs with an introduction, body, and a conclusion.  Make each body paragraph their own section.  The main idea of each body paragraph are these ideas respectively: {mainIdeas}" 
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=1500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    answer = response['choices'][0]['text']
    print(answer)
    with open("outline.txt", 'w') as f:
        f.write(answer)

def generateMainIdeas(topic, number=5):
    if number > 2:
        number -= 2 # generate main ideas for 'x' many paragraphs minus the intro and conclusion
    response = openai.Completion.create(
    model=davinci,
    prompt=f"Generate {number} topics about {topic}",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    answer = response['choices'][0]['text']    
    return answer

topicGenerator = False
while topicGenerator:
    topic = input("Enter a topic: ")
    if len(topic) < 2:
        quit()
    number = int(input("Enter the number of ideas: "))
    if number < 2:
        quit()

    mainIdeas = generateMainIdeas(topic, number).strip()
    print(mainIdeas)
    valid = input("Valid y/n: ")
    if valid == 'y':
        addToDataFile(f"Generate {number} topics about {topic}", mainIdeas, file="data/main_idea_generator.jsonl")
    elif valid == 'n':
        pass 
    else:
        quit()

