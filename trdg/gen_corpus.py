import os
import random

def sentence_from_words(in_file_path, out_file_path, num_words=4):
    # length = len_scorpus/numwords
    with open(out_file_path, 'a+') as out_file:
        with open(in_file_path, 'r') as in_file:
            words = in_file.readlines()
            print(len(words))
            # print(words)
            for i in range(0, len(words)-3, num_words):
                sentences = ""
                for j in range(i, i+num_words):
                    sentences+=words[j].strip() + " "
                sentences += "\n"
                out_file.write(sentences)
            in_file.close()
        out_file.close()

def random_sentence_from_words(in_file_path, out_file_path, num_words=3, num_sentences=20000):
    with open(out_file_path, 'a+') as out_file:
        with open(in_file_path, 'r') as in_file:
            words = in_file.readlines()
            for i in range(num_sentences):
                sentences = ""
                for j in range(num_words):
                    sentences += random.choice(words)
                sentences += "\n"
                out_file.write(sentences)

def random_sentence_from_words_with_special_char(in_file_path, out_file_path, special_file_path, num_words=2, num_special=4, num_sentences=20000):
    with open(out_file_path, 'a+') as out_file:
        with open(in_file_path, 'r') as in_file:
            words = in_file.readlines()
            with open(special_file_path, 'r') as special_file:
                speacial_chars = special_file.readlines()[0].split("")
            for i in range(num_sentences):
                sentences = ""
                for j in range(num_words):
                    sentences += random.choice(words)
                for k in range(num_special):
                    sentences += random.choice(speacial_chasr)
                sentences += "\n"
                out_file.write(sentences)


if __name__=="__main__":
    in_file_path = "./texts/underthesea_viet22k.txt"
    out_file_path = "./texts/vutt_corpus.txt"
    special_file_path = "./texts/special_chars.txt"
    sentence_from_words(in_file_path, out_file_path)