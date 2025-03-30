from typing import List

def solution(sentences: List, words: List) -> List:
    result = []

    for sentence, word in zip(sentences, words):
        word_idx = sentence.lower().find(word)

        if word_idx != -1:
            result.append(
                sentence.lower().replace(word, word[::-1].capitalize())
                if sentence[word_idx].isupper()
                else sentence.replace(word, word[::-1])
            )
        else:
            result.append(sentence)

    return result


if __name__ == "__main__":
    ss = ['lower case sentence', 'upper case Sentence', 'another Sentence here', '', 'final Sentence yay']
    ws = ['sentence', 'sentence', 'sentence', 'empty', 'sentence']

    print(solution(ss, ws))