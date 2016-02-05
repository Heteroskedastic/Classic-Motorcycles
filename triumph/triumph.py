__author__ = 'vincentdavis'
# Python 3
# based on this document
# http://www.britishspares.com/41.php

import re
from itertools import permutations

tri_50_62_code = {'1950': (100, 99999, 'From 100N'),
                      '1951': (101, 15808, '101NA, 15808NA'),
                      '1952': (32303, 44134, '32303, 44134'),
                      '1954': (44135, 56699, '44135, 56699'),
                      '1955': (56700, 70929, '56700, 70929'),
                      '1956a': (70930, 82799, '70930, 82799 then 0100 - 0944'),
                      '1956b': ('0100', '0944', '0100, 0944'),
                      '1957': ('0945', '011115', '0945, 011115'),
                      '1958': ('011116', '020075', '011116, 020075'),
                      '1959': ('020076', '029363', '020076, 029363'),
                      '1960a': ('029364', '030424', '029364, 030424 then D101 - D7726'),
                      '1960b': (101, 7726, 'D101 - D7726'),
                      '1961': (7727, 15788, 'D7727 - D15788'),
                      '1962': (15789, 99999, 'D15789 on')}

# Engine No. Unit 650cc
tri_650_63_69_code = {'1963': (101, 5824),
                     '1964': (5825, 13374),
                     '1965': (13375, 24874),
                     '1966': (24875, 44393),
                     '1967': (44394, 66245),
                     '1968': (66246, 85903),
                     '1969': (85904, 90282)}

tri_57_69_code = {'1957': (101, 760),
                  '1958': (761, 5484),
                  '1959': (5485, 11511),
                  '1960': (11512, 18611),
                  '1961': (18612, 25251),
                  '1962': (25252, 29732),
                  '1963': (29733, 32464),
                  '1964': (32465, 35986),
                  '1965': (35987, 40527),
                  '1966': (40528, 49832),
                  '1968': (57083, 65572),
                  '1969': (65573, 67331)}

tri_69_83_pre_code = {'a': ('January', '78-79'),
                      'b': ('February', '79-80'),
                      'c': ('March', '68-69'),
                      'd': ('April', '69-70'),
                      'e': ('May', '70-71'),
                      'g': ('June', '71-72'),
                      'h': ('July', '72-23'),
                      'j': ('August', '73-74'),
                      'k': ('September', '74-75'),
                      'n': ('October', '75-76'),
                      'p': ('November', '76-77'),
                      'x': ('December', '77-78'),
                      'ca': (None, '80-81'),
                      'da': (None, '81-82'),
                      'ea': (None, '82-83')}

def tri_650_63_69(vin):
    vin = vin.lower()
    alpha_digit = re.match(r'^(\D+)+(\d+)$', vin)
    g = alpha_digit.groups()
    if g[0]=='du' and int(g[1]) >= 101 and int(g[1]) <= 90282 and len(g[1]) == len(str(int(g[1]))):
        for key, v in tri_650_63_69_code.items():
            if v[0] <= int(g[1]) <= v[1]:
                return 'Unit 650cc Model year ' + key

def tri_57_69(vin):
    vin = vin.lower()
    alpha_digit = re.match(r'^(\D+)+(\d+)$', vin)
    g = alpha_digit.groups()
    if g[0]=='h' and int(g[1]) >= 101 and int(g[1]) <= 90282 and len(g[1]) == len(str(int(g[1]))):
        for key, v in tri_57_69_code.items():
            if v[0] <= int(g[1]) <= v[1]:
                return 'Unit 350/500 Model year ' + key

def tri_69_80(vin):
    vin = vin.lower()
    alpha_digit = re.match(r'^(\D+)+(\d+)$', vin)
    g = alpha_digit.groups()
    prefixes = [m[0] + m[1] for m in permutations('abcdeghjknpx', 2)]
    if alpha_digit and g[0] in prefixes:
        return 'Triumph Twins, Triples & Singles Built ' + tri_69_83_pre_code[g[0][0]][0] + ' 19' + tri_69_83_pre_code[g[0][1]][1]

def tri_81_83(vin):
    '''
    KDA	1981 models	Sept 1980 - Apr 1981
    EDA	1982 models	May 1981 - Jan 1982
    BEA	1983 models	Feb 1982 - Jan 1983
    T140V AEA34393 - Last model Jan 21st, 1983
    :param vin:
    :return:
    '''
    vin = vin.lower()
    alpha_digit = re.match(r'^(\D+)+(\d+)$', vin)
    g = alpha_digit.groups()
    prefixes = [m[0] + m[1] for m in permutations('abcdeghjknpx', 2)]
    if alpha_digit and g[0][:2] in prefixes and len(g[0])==3 and g[0][-1]=='a':
        return '500/650 Unit Construction Built ' + tri_69_83_pre_code[g[0][0]][0] + ' 19' + tri_69_83_pre_code[g[0][1:]][1]


###############################################
# Quick test
definitions = [tri_650_63_69, tri_57_69, tri_69_80, tri_81_83]
# vins = ['HK12345', 'AEA34393', 'h29733', 'du35987']
# for v in vins:
#     print('**** ' + v + ' ****')
#     for d in definitions:
#         print(d(v))
