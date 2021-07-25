#!/usr/bin/python3
# -*-coding:utf-8-*-
import os
import json
import re


def readFile(path):
    if os.path.exists(path):
        try:
            f = open(path, "r")
            data = f.read()
            return data
        except IOError as e:
            print(e)
            return None
    else:
        return None


if __name__ == '__main__':
    source = readFile("xzqh.txt")
    result = source.split('\n')
    for line in result:
        # *([\u4e00-\u9fa5]{2,10})
        newLine = line.replace(r'\s+', '')
        print(newLine)
        matchResults = re.search(r'(\d{6})([\u4e00-\u9fa5]{2,10})', newLine, re.I)
        # print(matchResults)
        # print(matchResults.group(0))
        # print(matchResults.group(1))
