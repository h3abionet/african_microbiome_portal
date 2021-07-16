#!/usr/bin/env python

import itertools
# This code was acquired from StackOverflow


class Seeder(object):

    """Docstring for Seeder. """

    def __init__(self):
        """TODO: to be defined. """
        self.seed = set()
        self.cache = dict()

    def get_seed(self, word):
        LIMIT = 3
        seed = self.cache.get(word, None)
        if seed is not None:
            return seed
        for seed in self.seeds:
            if self.distance(seed, word) <= LIMIT:
                self.cache[word] = seed
                return seed
        self.seeds.add(word)
        self.cache[word] = word
        return word

    def distance(self, s1, s2):
        l1 = len(s1)
        l2 = len(s2)
        matrix = [list(range(zz, zz + l1 + 1)) for zz in range(l2 + 1)]
        for zz in range(0, l2):
            for sz in range(0, l1):
                if s1[sz] == s2[zz]:
                    matrix[zz+1][sz+1] = min(matrix[zz+1][sz] + 1,
                                             matrix[zz][sz+1] + 1, matrix[zz][sz])
                else:
                    matrix[zz+1][sz+1] = min(matrix[zz+1][sz] + 1,
                                             matrix[zz][sz+1] + 1, matrix[zz][sz] + 1)
        return matrix[l2][l1]


def group_similar(words):
    seeder = Seeder()
    words = sorted(words, key=seeder.get_seed)
    groups = itertools.groupby(words, key=seeder.get_seed)
    return [list(v) for k, v in groups]
