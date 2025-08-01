# Chainlit AI Assistant Setup

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure your LLM:**
   - Copy `.env.example` to `.env`
   - Add your API key for your chosen LLM provider

3. **Run the application:**
   ```bash
   chainlit run app.py
   ```

4. **Open your HTML page:**
   - Open `index.html` in your browser
   - The chatbot widget will be embedded and ready to use

## LLM Options

### OpenAI (Recommended)
```env
OPENAI_API_KEY=your_openai_api_key_here
MODEL_NAME=gpt-3.5-turbo
```

### Local LLM (Ollama)
```env
API_BASE_URL=http://localhost:11434/v1
MODEL_NAME=llama2
```

### Other OpenAI-compatible APIs
```env
API_BASE_URL=http://your-api-endpoint/v1
API_KEY=your_api_key
MODEL_NAME=your_model_name
```

## Features

- ✅ LLM integration with proper error handling
- ✅ Environment-based configuration
- ✅ Copilot widget for web embedding
- ✅ Typing indicators and step visualization
- ✅ Customizable welcome screen