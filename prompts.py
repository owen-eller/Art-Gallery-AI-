from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

def get_art_gallery_prompt():
    """
    Returns a ChatPromptTemplate for the Art Gallery Chatbot.
    The model acts as a polite and informative gallery assistant.
    """
    human_prompt = HumanMessagePromptTemplate.from_template(
        "You are an expert art gallery assistant. Answer politely and provide interesting details about exhibitions, artists, or artworks. "
        "Keep the answer 2-3 sentences long.\n\nUser: {question}\nAssistant:"
    )
    return ChatPromptTemplate.from_messages([human_prompt])

