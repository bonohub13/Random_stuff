#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Reiwa:
    def scream_reiwa(self):
        for i in range(10):
            print('令和だよ！ＲＥＩＷＡ＊＊＊ＲＥＩＷＡ＊＊＊ＲＥＩＷＡ!!!')
        print('平成でやったこと超えられますように！！！！！！！！！！')
        print('m~(・ω・`m~) ｺｴﾗﾚﾅｶｯﾀﾗ､ﾜｶｯﾃﾙﾅ?')

    def loop(self):
        end = False
        while not end:
            button = input('=== ENTER to escape ===')
            if button is '':
                end = True

if __name__ == "__main__":
    Reiwa().scream_reiwa()
    Reiwa().loop()
