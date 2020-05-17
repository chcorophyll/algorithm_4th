

class Anagram(object):

    def check_0(self, word_1, word_2):
        word_1 = word_1.lower()
        word_2 = word_2.lower()
        if not len(word_1) == len(word_2):
            return False
        temp_list = list(word_2)
        pos_1 = 0
        still_ok = True
        while pos_1 < len(word_1) and still_ok:
            pos_2 = 0
            found = False
            while pos_2 < len(temp_list) and not found:
                if word_1[pos_1] == temp_list[pos_2]:
                    found = True
                else:
                    pos_2 += 1
            if found:
                temp_list[pos_2] = None
            else:
                still_ok = False
            pos_1 += 1
        return still_ok

    def check_1(self, word_1, word_2):
        word_1 = list(word_1.lower())
        word_2 = list(word_2.lower())
        if not len(word_1) == len(word_2):
            return False
        word_1.sort()
        word_2.sort()
        pos = 0
        match = True
        while pos < len(word_1) and match:
            if word_1[pos] == word_2[pos]:
                pos += 1
            else:
                match = False
        return match

    def check_2(self, word_1, word_2):
        if not len(word_1) == len(word_2):
            return False
        count_1 = [0] * 26
        count_2 = [0] * 26
        for i in range(len(word_1)):
            pos = ord(word_1[i]) - ord("a")
            count_1[pos] = count_1[pos] + 1
        for i in range(len(word_2)):
            pos = ord(word_2[i]) - ord("a")
            count_2[pos] = count_2[pos] + 1
        pos = 0
        stillok = True
        while pos < len(count_1) and stillok:
            if count_1[pos] == count_2[pos]:
                pos += 1
            else:
                stillok = False
        return stillok

    def check_3(self, word_1, word_2):
        if not len(word_1) == len(word_2):
            return False
        count_1 = {}
        count_2 = {}
        for i in range(len(word_1)):
            count_1[word_1[i]] = count_1.get(word_1[word_1[i]], 0) + 1
        for i in range(len(word_2)):
            count_2[word_2[i]] = count_2.get(word_2[word_2[i]], 0) + 1
        pos = 0
        stillok = True
        while pos < len(word_1) and stillok:
            if count_1[word_1[pos]] == count_2[word_1[pos]]:
                pos += 1
            else:
                stillok = False
        return stillok



