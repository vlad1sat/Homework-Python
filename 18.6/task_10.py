import string

text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'.split()
letters = string.ascii_letters
solve_text = []
key = 3


def logic_transcripts_text(base_key):
    for word in text:
        text_decryption = text_decryption(word)
        shift_text = shift_base_text(text_decryption, base_key)
        if shift_text.endswith("/"):
            base_key += 1
            solve_text.append(shift_text)
        else:
            solve_text.append(shift_text)


def text_decryption(base_text):
    translated = ''
    for word_text in base_text:
        if word_text in letters:
            num_index = letters.find(word_text)
            translated += letters[num_index - 1]
        else:
            translated += word_text
    return translated


def shift_base_text(base_text, key_shift):
    shift = key_shift % len(base_text)
    return base_text[-shift:] + base_text[:-shift]


def replace_text(base_text):
    base_text = " ".join(base_text)
    base_text = base_text.replace("+", "*").replace("-", ",").replace("(", "'")
    base_text = base_text.replace("..", "-").replace('"', "!").replace("/", ".\n")
    return base_text


logic_transcripts_text(key)
solve_text = replace_text(solve_text)
print(solve_text)
