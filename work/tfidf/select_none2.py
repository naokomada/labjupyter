# -*- coding: utf-8 -*-

import os, MeCab

tagger = MeCab.Tagger()
tagger.parseToNode('') # おまじない 

def lineWakatiWriter(line):
    node = tagger.parseToNode(line)
    while node:
        if node.feature.startswith('名詞'):
            print(node.surface)
            node = node.next

line = u"お仕事については基本的には店舗に配属してからのOJTが中心となりますが、先輩スタッフがしっかりとサポートしてくれるので、どなたも安心してお仕事していただけます。2013年には本社内に開発室を設置。店舗配属前にもトレーニングを行なってから実際の店舗に配属されるなど、サポート体制がしっかりと整っているのも当社の魅力。実際、経験が浅い方や未経験スタートのスタッフも多数活躍中！"
lineWakatiWriter(line)

