#jieba Word-cut
import jieba

jieba.enable_paddle()

strs1 = ["我是清华水利系的", "我是清华土木系的", "我是中科大数学系的"]
for strs in strs1:
    seg_list = jieba.cut(strs, use_paddle = True)
    print("Paddle Mode: " + "/".join(list(seg_list)))


result = jieba.tokenize(u'永和服装饰品有限公司')
for tk in result:
    print("word %s\t\t start: %d \t\t end: %d" % (tk[0], tk[1], tk[2]))


result = jieba.tokenize(u'永和服装饰品有限公司')

jieba.enable_paddle()
strs1 = ["我是清华水利系的，您这边是什么东西"]
for strs in strs1:
    segList = jieba.cut(strs, use_paddle = True)
    print("Paddle Mode: " + "/".join(list(segList)))




