import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
'''from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status'''



# Create your views here.
@csrf_exempt ## This decorator is used to allow the view to accept POST requests. DEVELOPMENT ONLY
def handleMessageDM(request):

  testPromptResponses = [{'prompt' : 'hello', 'response': 'Hello, <user>! How may I assist you today?'},
                         {'prompt' : ['who','what','are','you','for'], 'response': 'I am a Trading Assistant made to make your Trading experience better.'}]

  if request.method == 'POST':
    data = json.loads(request.body)
    messageText = data.get('text', '')
    replyText = f"Hi, <user>! Unfortuantely, I'm not too sure how to answer that yet. (handled by Devin)"

    for promptResponse in testPromptResponses:
      # Check if the message text contains any of the prompts.
      if type(promptResponse['prompt']) == list:
        if any(prompt in messageText.lower() for prompt in promptResponse['prompt']):
          replyText = promptResponse['response'] + ' (handled by Devin)'
          break
      else:
        if promptResponse['prompt'] in messageText.lower():
          replyText = promptResponse['response'] + ' (handled by Devin)'
          break

    return JsonResponse({'reply': replyText,
                         'sender' : 'server',
                         }, status=200)
  return JsonResponse({'error': 'invalid request'}, status=400)

@csrf_exempt ## This decorator is used to allow the view to accept POST requests. DEVELOPMENT ONLY
def handleMessageAL(request):

  testPromptResponses = [{'prompt' : 'hello', 'response': 'Hello, <user>! How may I assist you today?'},
                         {'prompt' : ['who','what','are','you','for'], 'response': 'I am a Trading Assistant made to make your Trading experience better.'}]

  if request.method == 'POST':
    data = json.loads(request.body)
    messageText = data.get('text', '')
    replyText = f"Hi, <user>! Unfortuantely, I'm not too sure how to answer that yet. (handled by Annalisa)"

    for promptResponse in testPromptResponses:
      # Check if the message text contains any of the prompts.
      if type(promptResponse['prompt']) == list:
        if any(prompt in messageText.lower() for prompt in promptResponse['prompt']):
          replyText = promptResponse['response'] + ' (handled by Annalisa)'
          break
      else:
        if promptResponse['prompt'] in messageText.lower():
          replyText = promptResponse['response'] + ' (handled by Annalisa)'
          break

    return JsonResponse({'reply': replyText,
                         'sender' : 'server',
                         }, status=200)
  return JsonResponse({'error': 'invalid request'}, status=400)

@csrf_exempt ## This decorator is used to allow the view to accept POST requests. DEVELOPMENT ONLY
def handleMessageW(request):

  testPromptResponses = [{'prompt' : 'hello', 'response': 'Hello, <user>! How may I assist you today?'},
                         {'prompt' : ['who','what','are','you','for'], 'response': 'I am a Trading Assistant made to make your Trading experience better.'}]

  if request.method == 'POST':
    data = json.loads(request.body)
    messageText = data.get('text', '')
    replyText = f"Hi, <user>! Unfortuantely, I'm not too sure how to answer that yet. (handled by Wags)"

    for promptResponse in testPromptResponses:
      # Check if the message text contains any of the prompts.
      if type(promptResponse['prompt']) == list:
        if any(prompt in messageText.lower() for prompt in promptResponse['prompt']):
          replyText = promptResponse['response'] + ' (handled by Wags)'
          break
      else:
        if promptResponse['prompt'] in messageText.lower():
          replyText = promptResponse['response'] + ' (handled by Wags)'
          break

    return JsonResponse({'reply': replyText,
                         'sender' : 'server',
                         }, status=200)
  return JsonResponse({'error': 'invalid request'}, status=400)

