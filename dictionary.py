dictionary = "hello salam goodbye khodafez say goftan we ma you shoma"

my_dict = {}
dict()
key_value = dictionary.split(" ")
for i in range(0,len(key_value),2):
    key = key_value[i]
    value = key_value[i+1]
    my_dict[key] = value
print(my_dict)

def translate_sentence(jomle, my_dict):
    words = jomle.split()
    translated_words = []

    for word in words:
        translated_word = my_dict.get(word.lower(), word)
        translated_words.append(translated_word)

    translate_sentence = " ".join(translated_words)
    return translate_sentence

jomle = "we say goodbye to you tonight"
translate_sentence = translate_sentence(jomle, my_dict)
print(translate_sentence)







# d = 'salam. mehrdad hastam,mikham test konam'
#
# counter = dict()
#
# for letter in d:
#     counter[letter] = counter.get(letter, 0) + 1
# for letter in list(counter.keys()):
#     print(letter, counter[letter])

#
# countries = ['iran','iran','iran','iran','iran','iran','iran', 'shili', 'italy', 'shili', 'italy', 'shili', 'italy', 'iraq','iran','iran','iran','iran', 'shili', 'italy']
# votes = dict()
# for country in countries:
#     if country in votes:
#         votes[country] += 1
#     else:
#         votes[country] = 1
# sorted_votes = sorted(votes.items(), key=lambda x: x[1], reverse=True)
# for country, votes in sorted_votes:
#     print(f'{country}: {votes}')

