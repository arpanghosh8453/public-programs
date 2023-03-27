import os, time
import openai # you need to install the openai package by using `pip install openai` in the terminal
from openai.error import RateLimitError

openai.api_key = os.getenv("OPENAI_API_KEY") # Please replace `os.getenv("OPENAI_API_KEY")` with your api key within quotes after the = sign. 

INPUT_FILE = "C:/Users/thisi/Downloads/Novel-Chinese.txt" # replace your input file location, please use the / instead of \ in the path
OUTPUT_FILE = "C:/Users/thisi/Downloads/Novel-English.txt" # replace your output file location, please use the / instead of \ in the path
STARTLINE = 15146 # Please enter from which like you want to start the translation. 
ENDLINE = 15250 # Please enter which line in the the file you want to stop
#ENDLINE = 69823
DEFAULT_ITERATION = 30 # Do not change
DEFAULT_RETERDATION = 5 # Do not change


start = STARTLINE
iteration = DEFAULT_ITERATION
total_token_cost = 0

with open(INPUT_FILE , encoding="utf8") as chinease_file:
  content = chinease_file.readlines()

while start < ENDLINE:
  end = start + iteration
  end = min(end, ENDLINE)

  current_chinease_text = content[start:end]

  current_prompt = "Translate the following page from the novel called My Wife Is From a Thousand Years Ago from Chinese to English while fixing issues related to syntax and grammar, idiomatic expressions, ambiguity, named entities, and technical terminology. Do not forget to proofread it and make it coherent.\n\n-VERY IMPORTANT: Swear words such as 'F***' must be written in full like 'fuck' as this will be used to let blind people read the novel via TTS, correct those. Also remove the following whenever encountered:\n- YOU MUST REMOVE mentions of: 'Novel: My Wife Comes from a Thousand Years Ago'\n- YOU MUST REMOVE mentions of: 'Author: Hua Still Hasn't Blossomed'\n- REMOVE advertisement and LINKS such as: 'UU Reading www.uukanshu.com', or passages that are not related to the novel like these. THIS IS A MUST!!!\n- Also remove any indentations from the translation.\n- You translate 'Eldest miss' to 'Erniang'. Fix that.\n- Translate 'Donggua' to 'Watermelon'. This refers to the name of a pet cat, use that as reference when editing and do not change the translation. THIS IS VERY IMPORTANT.\n- Do not translate 'sword' as 'dart'.\n- If the translated sentence starts with 'Chapter', keep it as is.\n- Translate Chinese honorifics to English, such as 'gege' to 'brother', and so on: \n\n"+"".join(current_chinease_text)
  try:
    response = openai.Completion.create(
      model="text-davinci-003", # Change the model if you want to. different rate limit may apply for different models
      prompt=current_prompt,
      temperature=0,
      max_tokens=2000, # Do not change
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
  except RateLimitError as ERR:
    print(ERR, "Waiting for 30 seconds...")
    time.sleep(30)

  english_result = response["choices"][0]["text"]
  finish_code = response["choices"][0]["finish_reason"]
  token_cost =  response["usage"]["total_tokens"]

  total_token_cost += token_cost

  if finish_code == "stop":
    print("Success : Translated successfully - lines",start,"to",end,"|","Token cost :",token_cost)
    with open(OUTPUT_FILE , "a", encoding="utf8") as english_file:
      english_file.write("\n"+english_result)
    start += iteration
    iteration = DEFAULT_ITERATION
  else:
    print("Failed : Abruptly ended due to long length. retying the same with fewer lines...","|","Token cost :",token_cost)
    iteration -= DEFAULT_RETERDATION

print("Program Complete | Total token cost :", total_token_cost )