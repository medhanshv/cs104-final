import sys

languages = ['english', 'hindi', 'punjabi']

def indirect_translations(translations):
    for language_a in languages:
        for language_b in languages:
            for language_c in languages:
                if language_a != language_b and language_b != language_c and language_a != language_c:
                    for word_a in translations[f'{language_a}_{language_b}'].keys():
                        if word_a not in translations[f'{language_a}_{language_c}'].keys():
                            word_b = translations[f'{language_a}_{language_b}'][word_a]
                            if word_b in translations[f'{language_b}_{language_c}'].keys():
                                word_c = translations[f'{language_b}_{language_c}'][word_b]
                                translations[f'{language_a}_{language_c}'][word_a] = word_c
                                translations[f'{language_c}_{language_a}'][word_c] = word_a

def load_translations():
    translations = {}
    translations['english_hindi'] = {}
    translations['english_punjabi'] = {}
    translations['hindi_english'] = {}
    translations['hindi_punjabi'] = {}
    translations['punjabi_english'] = {}
    translations['punjabi_hindi'] = {}
    with open('translations.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(',')
            language_a = parts[0]
            language_b = parts[2]
            word_a = parts[1]
            word_b = parts[3]
            translations[f'{language_a}_{language_b}'][word_a] = word_b
            translations[f'{language_b}_{language_a}'][word_b] = word_a
    return translations

def query_1(language):
    translations = load_translations()
    vocab = set()
    for other in languages:
        if language != other:
            for elem in set(translations[f'{language}_{other}'].keys()):
                vocab.add(elem)
    vocab = list(vocab)
    vocab.sort(reverse=True)
    print(vocab)
    return translations

def query_2(language_a, language_b):
    translations = load_translations()
    indirect_translations(translations)
    keys = list(translations[f'{language_a}_{language_b}'].keys())
    keys.sort()
    lot = [(key, translations[f'{language_a}_{language_b}'][key]) for key in keys]
    print(lot)
    return translations

def query_3(language_a, language_b, word):
    translations = load_translations()
    indirect_translations(translations)
    if word in translations[f'{language_a}_{language_b}'].keys():
        print(translations[f'{language_a}_{language_b}'][word])
    else:
        print("UNK")
    return translations
        
if __name__ == "__main__":
    query_type = int(sys.argv[1])
    
    if query_type == 1:
        language = sys.argv[2]
        translations = query_1(language)
    elif query_type == 2:
        language_a = sys.argv[2]
        language_b = sys.argv[3]
        translations = query_2(language_a, language_b)
    elif query_type == 3:
        language_a = sys.argv[2]
        language_b = sys.argv[3]
        word = sys.argv[4]
        translations = query_3(language_a, language_b, word)
