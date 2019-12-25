#! /usr/bin/env python3
#coding:utf8

import os.path as op
import string

class Lib:
    def __init__(self, fileLoc, store = {}):
        self._store = store
        self._fileLoc = fileLoc

    def inBookDict(self):
        print('open book dict file...')
        content = ''

        if op.exists(self._fileLoc):
            with open(self._fileLoc) as file1:
                content = file1.readlines()
            for i in range(len(content)):
                content[i] = content[i][:-1:]
                content[i] = content[i].split(' ')
                self._store[content[i][0]] = content[i][1]
            print('get book dict successifully')
        else:
            print('get book dict failed')

    def outBookDict(self):
        print('output book dict to file...')
        if op.exists(self._fileLoc):
            print('add new book to original store...')
            file1 = open(self._fileLoc, 'a')
            for key in self._newBook:
                file1.writelines(key + ' ' + self._store[key] + '\n')
        else:
            print('create file and write data...')
            file1 = open(self._fileLoc, 'w')
            for item in self._store.items():
                file1.writelines(item[0] + ' ' + item[1] + '\n')

        file1.close()

    def listAll(self):
        for item in self._store.items():
            print(item[0], item[1])

    def findBooks(self, stone, tag):
        result = []
        if tag == 'key':
            for i in stone:
                try:
                    name = self._store[i]
                except KeyError:
                    result.append(None)
                else:
                    result.append(name)
        else:
            for i in stone:
                midResult = []
                for item in self._store.items():
                    if i in item[1]:
                        midResult.append(item)
                result.append(midResult)
        return result

    def changeBookName(self, key, newName):
        try:
            self._store[key] = newName
        except KeyError:
            print('ERROR, no this book')

    def deleteBook(self, key):
        try:
            self._store.pop(key)
        except KeyError:
            print('ERROR, no this book')

    def addBook(self, key, name):
        lowerCase = list(string.ascii_lowercase)
        upperCase = list(string.ascii_uppercase)
        selfDef = ['?', '!', '.', ',', '$']
        
        lowerCase.extend(upperCase)
        lowerCase.extend(selfDef)
        
        nameList = list(name)
        for i in lowerCase:
            if i in nameList:
                for k in range(name.count(i)):
                    nameList.remove(i)
        if not nameList == []:
            print('ERROR, invalid book name')
            print(nameList)
            return
        
        self._store[key] = name
        self._newBook.append(key)
    
    def output(self):
        print(self._store)
        print(self._fileLoc)



    _fileLoc = ''
    _oldBookNum = 0
    _newBook = []
    _store = {}

