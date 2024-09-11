from groq import Groq

# Initialize the Groq client
client = Groq(api_key='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')

# Store the conversation history
conversation_history = [
    {
        "role": "system",
        "content": "You are a super AI with AGI capability."
    }
]


# Function to get the LLM response
def llm_response(user_query):
    # Add the user's query to the conversation history
    conversation_history.append({
        "role": "user",
        "content": user_query
    })

    # Get the response from the model
    chat_completion = client.chat.completions.create(
        messages=conversation_history,  # Pass the full conversation history
        model='llama-3.1-70b-versatile'
    )

    # Extract the assistant's response
    # Assuming `chat_completion.choices[0].message` is an object with a `content` attribute
    assistant_response = chat_completion.choices[0].message.content

    # Add the assistant's response to the conversation history
    conversation_history.append({
        "role": "assistant",
        "content": assistant_response
    })

    return assistant_response


# Main interaction loop
while True:
    user_query = input("Edem: ")

    if user_query.lower() == "quit":  # Case-insensitive check for "quit"
        break

    # Get and print the assistant's response
    response = llm_response(user_query)
    print("Assistance:", response)
