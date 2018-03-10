# -*- coding: utf-8 -*-

import os, MeCab
# 分かち書きしたファイル格納用のディレクトリ
if not os.path.exists('wakati'):
    os.mkdir('wakati')

tagger = MeCab.Tagger()
tagger.parseToNode('') # おまじない 

def lineWakatiWriter(line, writer):
    node = tagger.parseToNode(line)
    while node:
        if node.feature.startswith('名詞'):
            writer.write(node.surface + '\n')
            node = node.next

for file in os.listdir('praporitext'):
    with open('praporitext/' + file, 'rt') as reader, open('wakati/' + file, 'wt') as writer:
        for line in reader:
            lineWakatiWriter(line, writer)
