from bs4 import BeautifulSoup
import openai
import argparse
import time
import logging

logging.basicConfig(level=logging.INFO)

openai.api_key = 'API_KEY_HERE'

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
            continue

        if tag.string:
            original_text = tag.string.strip()
            translated_text = translate_text(original_text, target_language)
            tag.string.replace_with(translated_text)

            logging.info(f'Translated: {original_text} -> {translated_text}')

            time.sleep(20)

    translated_html = str(soup)
    return translated_html

def main():
    parser = argparse.ArgumentParser(description='Translate HTML content.')
    parser.add_argument('--input_file', type=str, default='index.html', help='Path to the input HTML file')
    parser.add_argument('--output_file', type=str, default='translated_index.html', help='Path to the output HTML file')
    parser.add_argument('--target_language', type=str, default='es', help='Target language for translation')

    args = parser.parse_args()

    logging.info(f'Starting translation for {args.input_file} to {args.target_language}')

    with open(args.input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    translated_html = translate_html(html_content, args.target_language)

    with open(args.output_file, 'w', encoding='utf-8') as file:
        file.write(translated_html)

    logging.info(f'Translation completed. Translated HTML saved to {args.output_file}')

if __name__ == "__main__":
    main()
