import deepl
import codecs
import glob

auth_key = ""  # Replace with your key
translator = deepl.Translator(auth_key)

for f in glob.glob('**/*.html', recursive=True):
    fr=codecs.open(f, 'r')
    result = translator.translate_text(fr.read(), target_lang="SK", source_lang="CS", split_sentences="nonewlines", tag_handling="html")
    fr.close()
    newFileName = f.replace(".html", ".sk.html")
    f = open(newFileName, "w")
    f.write(result.text)
    f.close()
    print("Succesfully created file: " + newFileName)