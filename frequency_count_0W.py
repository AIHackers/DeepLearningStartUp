from zhon.hanzi import punctuation
import nltk
import operator

#获取文本内容
with open("happiness_seg.txt",encoding='utf-8') as f:
    text = f.read()

#去除标点、空格
words = text.split()

word_list =[]

for word in words:
    if word not in punctuation:
        word_list.append(word)

#组成二元分词列表

bigram = list(nltk.bigrams(word_list))

#计算二元分词出现的频率

bigram_frequency ={}

for bigram_words in bigram:
    if bigram_words not in bigram_frequency:
        bigram_frequency[bigram_words] = 1
    else:
        bigram_frequency[bigram_words] += 1

#输入出现次数最多的前十个
bigram_frequency_sorted = sorted(
    bigram_frequency.items(), key=operator.itemgetter(1),reverse=True)

print("出现频率最高的前 10 个「二元词组」是")
for i in range(10):
    print(bigram_frequency_sorted[i])
