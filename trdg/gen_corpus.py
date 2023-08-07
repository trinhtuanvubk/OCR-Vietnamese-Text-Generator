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
                if len(sentences.split(" ")) > 5:
                    sentences = " ".join(sentences.split(" ")[:-1])
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
        
def random_sentence_from_special_char(out_file_path, special_file_path, num_special=10, num_sentences=100000):
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

def random_sentence_number(out_file_path, num_sentences=100):
    with open(out_file_path, 'a+') as out_file:
        for i in range(num_sentences):
            number_chars="0123456789"
            # number_list=number_chars.split("")

            sentence = ''
            sentence+=str(random.randint(0,9999))
            # # sentence+=str(random.choice(["/", "-", " "]))
            sentence+=" "
            sentence+=str(random.randint(0,9999))
            # sentence+=str(random.choice(["/","-", " "]))
            sentence+=" "
            sentence+=str(random.randint(0,9999))
            # range_ = random.randint(4,12)
            # for k in range(range_):
            #     sentence+=str(random.choice(number_chars))
            pos = random.randint(1, len(sentence))
            sentence = sentence[:pos] + '5' + sentence[pos:]
            sentence += "\n"
            out_file.write(sentence)
                
        out_file.close()

def random_DK_number(out_file_path, num_sentences=25000):
    with open(out_file_path, 'a+') as out_file:
        for i in range(num_sentences):
            number_chars="0123456789"
            eng_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789012345678901234567890123456789"
            sentence = ''
            range_ = random.randint(8,16)
            for k in range(range_):
                sentence+=str(random.choice(eng_chars))

            sentence += "\n"
            out_file.write(sentence)
                
        out_file.close()

def random_DK_plate(out_file_path, num_sentences=25000):
    with open(out_file_path, 'a+') as out_file:
        for i in range(num_sentences):
            number_chars="0123456789"
            eng_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            sentence = ''
            sentence+= str(random.randint(1, 100))
            sentence+= random.choice(eng_chars)
            sentence+="-"
            sentence+= str(random.randint(100,10000))
            sentence+= random.choice("0123456789..........")
            sentence+= str(random.randint(1,100))

            # range_ = random.randint(8,16)
            # for k in range(range_):
            #     sentence+=str(random.choice(eng_chars))

            sentence += "\n"
            out_file.write(sentence)
                
        out_file.close()

def random_date_month_year(out_file_path, num_sentences=25000):
    with open(out_file_path, 'a+') as out_file:
        for i in range(num_sentences):
            number_chars="0123456789"
            eng_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            sentence = 'ngày (date) '
            date = (random.randint(1, 32))
            if date < 10:
                date = f"0{date} "
            else:
                date = f"{date} "
            sentence+=date
            sentence+="tháng "
            month = (random.randint(1, 13))
            if month < 10:
                month = f"0{month} "
            else:
                month = f"{month} "
            sentence+=month
            sentence+="năm "
            sentence+=str(random.randint(1990,2100))
            sentence += "\n"
            out_file.write(sentence)
                
        out_file.close()


def random_passport_code(out_file_path, num_sentences=25000):
    with open(out_file_path, 'a+') as out_file:
        _len=random.randint(18,21)
        number_chars="0123456789"
        eng_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        total="ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890123456789<<"
        for i in range(num_sentences):
            sentence = 'P<'
            ran1=random.randint(1,6)
            for j in range(ran1):
                sentence+=str(random.choice(eng_chars))
            sentence+="<<"
            ran2=random.randint(1,6)
            for k in range(ran2):
                sentence+=str(random.choice(eng_chars))
            sentence+="<"
            ran3=random.randint(1,6)
            for l in range(ran3):
                sentence+=str(random.choice(eng_chars))
            for m in range(_len - len(sentence)):
                sentence+="<"
            sentence += "\n"
            out_file.write(sentence)

            sentence= str(random.choice(eng_chars))
            ran4=random.randint(8,13)
            for n in range(ran4):
                sentence+=str(random.choice(total))
            ran5=random.randint(1,4)
            for u in range(ran5):
                sentence+=str("<")
            for v in range(_len - len(sentence)):
                sentence+=random.choice(number_chars)
            sentence += "\n"
            out_file.write(sentence)
            
        out_file.close()



def random_id_code(out_file_path, num_sentences=25000):
    with open(out_file_path, 'a+') as out_file:
        _len=random.randint(18,22)
        number_chars="0123456789"
        eng_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        total="ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890123456789<<"
        for i in range(num_sentences):
            sentence = 'ID'
            for j in range(3):
                sentence+=str(random.choice(eng_chars))
            ran2=random.randint(12,15)
            for k in range(ran2):
                sentence+=str(random.choice(number_chars))
            sentence+="<<"
            for m in range(_len - len(sentence)):
                sentence+=str(random.choice(number_chars))
            sentence += "\n"
            out_file.write(sentence)

            _len=random.randint(18,22)
            sentence= ''
            ran4=random.randint(8,13)
            for n in range(ran4):
                sentence+=str(random.choice(total))
            ran5=random.randint(1,4)
            for u in range(_len-len(sentence)-ran5):
                sentence+=str("<")
            for v in range(_len - len(sentence)):
                sentence+=random.choice(number_chars)
            sentence += "\n"
            out_file.write(sentence)

            _len=random.randint(18,22)
            sentence= ''
            for x in range(1, random.randint(2,6)):
                sentence+=random.choice(eng_chars)
            sentence+="<<"
            for y in range(1, random.randint(2,6)):
                sentence+=random.choice(eng_chars)
            sentence+="<"
            for z in range(1, random.randint(2,6)):
                sentence+=random.choice(eng_chars)
            for v in range(_len - len(sentence)):
                sentence+="<"
            sentence += "\n"
            out_file.write(sentence)
            
        out_file.close()





def shuffle_lines(file_path):

    with open(file_path, "r") as f:
        lines = f.readlines()

    random.shuffle(lines)

    with open(file_path, "w") as f:
        f.writelines(lines)



if __name__=="__main__":
    # in_file_path = "./texts/underthesea_viet22k_vi_dict_ori.txt"
    in_file_path = "./texts/underthesea_viet39k.txt"
    out_file_path = "./texts/special_domain/cccd/short_code.txt"
    special_file_path = "./texts/special_chars.txt"
    # sentence_from_words(in_file_path, out_file_path)
    # random_sentence_from_words(in_file_path, out_file_path, num_sentences=100000)
    # random_sentence_from_special_char(out_file_path, special_file_path, num_sentences=100000)
    # random_sentence_from_words_with_special_char(in_file_path, out_file_path, special_file_path, num_words=1, num_special=3, num_sentences=30000)
    # random_sentence_from_words_with_special_char(in_file_path, out_file_path, special_file_path, num_words=2, num_special=0, num_sentences=10000)
    # random_sentence_from_words_with_special_char(in_file_path, out_file_path, special_file_path, num_words=2, num_special=1, num_sentences=50000) 
    
    random_sentence_number("./texts/special_domain/fix5char.txt", 1000)
    # random_date_month_year(out_file_path, num_sentences=5000)
    # random_DK_plate(out_file_path, num_sentences=5000)
    # random_date_month_year(out_file_path, num_sentences=500)
    # random_passport_code(out_file_path, num_sentences=3000)
    # random_id_code(out_file_path, num_sentences=3000)

    # shuffle_lines("./texts/special_domain/name.txt")
    # shuffle_lines("./texts/vutt_corpus_number.txt")
    # shuffle_lines("./texts/vutt_corpus39k_317.txt")
    # shuffle_lines("./texts/vutt_corpus_number.txt")
    # shuffle_lines("./texts/vutt_corpus39k_267.txt")
