from rest_framework.views import APIView
from .utils import chatGPT_interact  
from rest_framework.response import Response       
import openai

openai.api_key = "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"


class ChatGptResponseView(APIView):
    def post(self,request,*args):
        text = request.data.get("text")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )       
        return Response({"success":True,"response":response},status=200)