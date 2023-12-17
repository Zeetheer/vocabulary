import json


class Vocabulary:
    def __init__(self, language):
        self.language = language
        with open("vocabulary.json", "r", encoding="UTF8") as vocajson:
            self.voca = json.load(vocajson)

    def save(self):
        with open("vocabulary.json", "w", encoding="UTF8") as jvocajson:
            json.dump(self.voca, jvocajson, ensure_ascii=False, indent=4)

    def add(self, word, mean):
        self.jvoca = self.voca["jvocabulary"]
        self.jvoca[word] = mean
        self.save()

    def modify(self, word, mean):
        self.mjvoca = self.voca["jvocabulary"]
        if word in self.mjvoca:
            self.mjvoca[word] = mean
            self.save()

    def delete(self, word):
        self.djvoca = self.voca["jvocabulary"]
        if word in self.djvoca:
            del self.djvoca[word]
            self.save()
        else:
            if self.language.lower() == 'korean':
                print(
                    f"해당 \'{word}\' 단어가 단어장에 등록되어 있지 않습니다. 그래서 해당 \'{word}\' 단어를 삭제하지 못했습니다")
            else:
                print(
                    f"The corresponding \'{word}\' word is not registered in the vocabulary. So progran couldn't delete that \'{word}\' word")
