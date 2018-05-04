class Anagram():

    def is_anagram(self, string1, string2):
        string1sort = sorted(string1)
        # print(string1sort)
        string2sort = sorted(string2)
        # print(string2sort)
        if string1sort == string2sort:
            return True
        else:
            return False
