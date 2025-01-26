import deepl
import codecs
import glob

auth_key = ""  # Replace with your key
translator = deepl.Translator(auth_key)

for f in glob.glob('**/*.html', recursive=True):
    with codecs.open(f, 'r', encoding='utf-8') as fr:
        result = translator.translate_text(fr.read(), target_lang="SK", source_lang="CS", split_sentences="nonewlines", tag_handling="html")
    
    newFileName = f.replace(".html", ".sk.html")
    
    with open(newFileName, "w", encoding='utf-8') as fw:
        fw.write(result.text)
    
    print("Successfully created file: " + newFileName)