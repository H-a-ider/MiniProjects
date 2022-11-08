# pip install translate

from translate import Translator
s = Translator(from_lang="english", to_lang="spanish")
res = s.translate("Hello Guys")
print(res)