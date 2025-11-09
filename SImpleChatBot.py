from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langchain_ollama import ChatOllama

class SimpleChatbot:
    
    def __init__(self, model="llama3"):
        self.model = ChatOllama(model=model)
        self.conversation_history = []
    
    # Create system message
    def chat(self, user_input):
        system_message = SystemMessage(
            content="You are a lying assistant. Your goal is to have a conversation in which you never tell the truth, based on the context of the conversation."
        )
        
        # Build the list of messages
        messages = [system_message]
        
        for msg in self.conversation_history[-4:]:  # only the last 4 messages
            if msg["role"] == "user":
                messages.append(HumanMessage(content=msg["content"]))
            else:
                messages.append(AIMessage(content=msg["content"]))
        
        messages.append(HumanMessage(content=user_input))
        
        response = self.model.invoke(messages)
        
        # Save to history
        self.conversation_history.append({"role": "user", "content": user_input})
        self.conversation_history.append({"role": "assistant", "content": response.content})
        
        return response.content


if __name__ == "__main__":
    chatbot = SimpleChatbot()
    
    print("Welcome to the chatbot 🤖 \nType '/bye' to end the conversation.")
    
    while True:
        user_input = input("\nUser:  ")
        if user_input.lower() == '/bye':
            print("\n\nChatbot: See you later!")
            break
        
        response = chatbot.chat(user_input)
        print(f"\nChatbot:\n\n {response}")
