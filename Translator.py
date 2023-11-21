from bs4 import BeautifulSoup
import openai

openai.api_key = 'YOUR_API_KEY'

def translate_text(text, target_language):
    prompt = f"Translate the following English text to {target_language}: '{text}'"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    translated_text = response.choices[0].text.strip()
    return translated_text

def translate_html(input_html, target_language='es'):
    soup = BeautifulSoup(input_html, 'html.parser')
    translated_html = ""

    for tag in soup.find_all():
        if tag.name in ['style', 'script']:
            # Skip the contents of style and script tags
            continue

        if tag.string:
            original_text = tag.string.strip()
            translated_text = translate_text(original_text, target_language)
            tag.string.replace_with(translated_text)

    translated_html = str(soup)
    return translated_html

if __name__ == "__main__":
    input_file = 'index.html'
    output_file = 'translated_index.html'
    target_language = 'es'  # Enter the desired language here

    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    translated_html = translate_html(html_content, target_language)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_html)

    print(f'Translation completed. Translated HTML saved to {output_file}')
    