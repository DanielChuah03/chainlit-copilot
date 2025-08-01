import chainlit as cl
import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client (works with OpenAI, local LLMs, or any OpenAI-compatible API)
client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Configuration
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1000"))

@cl.on_chat_start
async def start():
    await cl.Message(
        content="Hello! I'm your AI assistant. How can I help you today?"
    ).send()

@cl.on_message
async def on_message(message: cl.Message):
    # Show typing indicator
    async with cl.Step(name="Thinking...") as step:
        try:
            # Call the LLM
            response = await client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": message.content}
                ],
                max_tokens=MAX_TOKENS,
                temperature=0.7
            )
            
            # Get the response content
            response_content = response.choices[0].message.content
            step.output = response_content
            
        except Exception as e:
            error_msg = f"Error: {str(e)}\n\nPlease check your API configuration in the .env file."
            step.output = error_msg
            response_content = error_msg
    
    # Send the response
    await cl.Message(content=response_content).send()