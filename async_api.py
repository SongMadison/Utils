test_data = {
  "displayName": "Conversation Task Example",
  "analysisInput": {
    "conversations": [
      {
        "conversationItems": [
          {
            "text": "Hello, you’re chatting with Rene. How may I help you?",
            "id": "1",
            "role": "Agent",
            "participantId": "Agent_1"
          },
    ]
  },
  "tasks": [
    {
      "taskName": "Conversation Task 1",
      "kind": "ConversationalSummarizationTask",
      "parameters": {
        "summaryAspects": [
          "chapterTitle", "narrative", "issue", "resolution"  # can be a subject
        ]
      }
    }
  ]
}

import aiohttp
import asyncio
import json

LANGUAGE_KEY="<your own language resource key>"
async def post_data(url, data):  
    headers = {'Content-Type': 'application/json', "Ocp-Apim-Subscription-Key": LANGUAGE_KEY}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=json.dumps(data), headers=headers) as response:
            print("Status:", response.status)
            print("response:", response)
            return response

async def fetch(session, url):
    headers = {'Content-Type': 'application/json', "Ocp-Apim-Subscription-Key": LANGUAGE_KEY}
    async with session.get(url, headers=headers) as response:
        print("Status:", response.status)
        return await response.text()

async def get_data(response):
    async with aiohttp.ClientSession() as session:
        result = await fetch(session, response.headers['operation-location'])
        return result


url= "https://sonwang-ta-dev.cognitiveservices.azure.com/language/analyze-conversations/jobs?api-version=2022-10-01-preview"
post_result = await post_data(url, test_data)
print(post_result)
#await get_data(post_result)
import time
while True:
    x = await get_data(post_result)
    if json.loads(x)["status"] =="running" or json.loads(x)["status"] == "notStarted":
        time.sleep(5)
    else:
        break