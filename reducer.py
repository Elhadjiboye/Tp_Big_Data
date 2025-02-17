#!/usr/bin/env python3
import sys

word_count = {}

for line in sys.stdin:
    word, count = line.strip().split("\t")
    count = int(count)
    word_count[word] = word_count.get(word, 0) + count

for word, count in word_count.items():
    print(f"{word}\t{count}")
