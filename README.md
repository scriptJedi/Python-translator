# Python-translator

1. Install Python if you haven't already.

```bash
brew install python3
```

2. Install the OpenAI API.
  *(If you are using pip3, otherwise replace pip3 with pip)
```bash
pip3 install openai
```


3. Install dependencies.
  *(If you are using pip3, otherwise replace pip3 with pip)
```bash
pip3 install openai==0.27.0
pip3 install httpcore==0.13.3
```

4. Run the script.

```bash
python3 translator.py
```

You can also specify a target language as a command-line argument.

```bash
python3 translator.py --target_language french
```
In this example, the translation will be in French.

Feel free to use this template and improve it as you see fit.

Added translator_p the same translation, but with logging and a 25 second interval to get around the openAI limitation

```bash
python3 translator_t.py --target_language ukrainian
```
