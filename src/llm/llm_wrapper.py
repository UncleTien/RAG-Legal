import requests, json
from src.config.settings import settings

class OllamaClient:
    def __init__(self, host=None, model=None):
        self.host = host or settings.ollama_host
        self.model = model or settings.ollama_model

    def generate(self, prompt, max_tokens=1024, temperature=0.2):
        url = f"{self.host}/api/generate"
        payload = {'model': self.model, 'prompt': prompt, 'max_tokens': max_tokens, 'temperature': temperature}
        headers = {'Content-Type': 'application/json'}
        resp = requests.post(url, headers=headers, data=json.dumps(payload), timeout=120)
        resp.raise_for_status()
        data = resp.json()
        # Attempt to extract text from common keys
        if isinstance(data, dict):
            for k in ('response', 'output', 'text', 'result'):
                if k in data:
                    return data[k]
            # Ollama sometimes returns 'result' list
            return json.dumps(data, ensure_ascii=False)
        return str(data)

def generate_answer(question: str, context: str, system_prompt: str = None):
    prompt = ''
    if system_prompt:
        prompt += system_prompt + '\n\n'
    prompt += f"Context:\n{context}\n\nQuestion: {question}\n\nAnswer (Vietnamese, cite sources if possible):\n"
    client = OllamaClient()
    try:
        return client.generate(prompt)
    except Exception as e:
        return f"Error calling Ollama: {e}\nPrompt:\n{prompt}"
