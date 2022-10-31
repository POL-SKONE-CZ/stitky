import deepl
import codecs

auth_key = "391b96da-8804-493f-bf1b-8922d9d85040:fx"  # Replace with your key
translator = deepl.Translator(auth_key)

fr=codecs.open("test.html", 'r')
result = translator.translate_text(fr.read(), target_lang="SK", source_lang="CS", split_sentences="nonewlines", tag_handling="html")
fr.close()
f = open("output.html", "w")
f.write(result.text)
f.close()