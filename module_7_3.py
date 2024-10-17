class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                info = file.read().lower()
                for sym in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    info = info.replace(sym, ' ')
            all_words[file_name] = info.split()
        return all_words

    def find(self, word):
        places = {}
        for value, key in self.get_all_words().items():
            if word.lower() in key:
                places[value] = key.index(word.lower())+1
        return places

    def count(self, word):
        counters = {}
        total_count = 0
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counters[value] = words_count
        return counters

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего