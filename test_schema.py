
from models.schemas import ChatRequest, ChatResponse

# User question
request = ChatRequest(
    question="What is my CPU?"
)

print("User Question:")
print(request.question)


# AI response
response = ChatResponse(
    answer="Your CPU is Intel i5-12450H"
)

print("AI Answer:")
print(response.answer)
