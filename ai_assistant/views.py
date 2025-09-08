import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


class ChatAssistantView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user_message = request.data.get("message", "")

        if not user_message:
            return Response({"error": "Нет сообщения"}, status=400)

        # 🔹 LLM (OpenAI через LangChain)
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", "Ты помощник сервиса бронирования комнат. Отвечай чётко и по делу."),
            ("user", "{message}")
        ])

        chain = prompt | llm
        response = chain.invoke({"message": user_message})

        return Response({"answer": response.content})
