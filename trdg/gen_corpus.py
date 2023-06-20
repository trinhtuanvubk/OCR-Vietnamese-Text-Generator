import os
import random

def sentence_from_words(in_file_path, out_file_path, num_words=1):
    # length = len_scorpus/numwords
    with open(out_file_path, 'a+') as out_file:
        with open(in_file_path, 'r') as in_file:
            words = in_file.readlines()
            for i in range(0, len(words)-3):
                sentences = ""
                for j in range(i, i+num_words):
                    sentences+=words[j].strip() + " "
                sentences = sentences.strip()
                sentences += "\n"
                out_file.write(sentences)
            in_file.close()
        out_file.close()

def random_sentence_from_words(in_file_path, out_file_path, num_words=2, num_sentences=20000):
    with open(out_file_path, 'a+') as out_file:
        with open(in_file_path, 'r') as in_file:
            words = in_file.readlines()
            for i in range(num_sentences):
                sentences = ""
                for j in range(num_words):
                    sentences += random.choice(words).strip() + " "
                sentences = sentences.strip()
                sentences += "\n"
                out_file.write(sentences)
            in_file.close()
        out_file.close()

def random_sentence_from_words_with_special_char(in_file_path, out_file_path, special_file_path, num_words=1, num_special=3, num_sentences=30000):
    with open(out_file_path, 'a+') as out_file:
        with open(in_file_path, 'r') as in_file:
            words = in_file.readlines()
            with open(special_file_path, 'r') as special_file:
                speacial_chars = special_file.readlines()[0]
            for i in range(num_sentences):
                sentences = ""
                # num_words = random.randint(1, num_words)
                # num_special = random.randint(1, num_special)
                for j in range(num_words):
                    sentences += random.choice(words).strip() + " "
                for k in range(num_special):
                    sentences += random.choice(speacial_chars) + " "
                sentences = sentences.strip()
                _sentences = sentences.split(" ")
                random.shuffle(_sentences)
                sentences = ' '.join(_sentences)
                sentences += "\n"
                out_file.write(sentences)
            in_file.close()
        out_file.close()
        
def random_sentence_from_special_char(out_file_path, special_file_path, num_special=20, num_sentences=20000):
    with open(out_file_path, 'a+') as out_file:
        with open(special_file_path, 'r') as special_file:
            speacial_chars = special_file.readlines()[0]
            for i in range(num_sentences):
                sentences = ""
                for k in range(num_special):
                    sentences += random.choice(speacial_chars) + " "
                sentences = sentences.strip()
                sentences += "\n"
                out_file.write(sentences)
            special_file.close()
        out_file.close()


if __name__=="__main__":
    in_file_path = "./texts/underthesea_viet22k_vi_dict.txt"
    out_file_path = "./texts/vutt_corpus5.txt"
    special_file_path = "./texts/special_chars.txt"
    # sentence_from_words(in_file_path, out_file_path)
    # random_sentence_from_words(in_file_path, out_file_path, num_sentences=60000)    
    # random_sentence_from_special_char(out_file_path, special_file_path, num_sentences=10000)
    # random_sentence_from_words_with_special_char(in_file_path, out_file_path, special_file_path, num_words=1, num_special=3, num_sentences=30000)
    # random_sentence_from_words_with_special_char(in_file_path, out_file_path, special_file_path, num_words=2, num_special=0, num_sentences=10000)
    random_sentence_from_words_with_special_char(in_file_path, out_file_path, special_file_path, num_words=2, num_special=1, num_sentences=50000) 
    