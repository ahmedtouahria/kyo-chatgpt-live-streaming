from rest_framework.views import APIView
from .utils import chatGPT_interact  
from rest_framework.response import Response       
import openai

openai.api_key = "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"


class ChatGptResponseView(APIView):
    def post(self,request,*args):
        text = request.data.get("text")
        try:
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )       
        except Exception as e:
            return Response({"success":False,"response":str(e)})
            
        return Response({"success":True,"response":response},status=200)