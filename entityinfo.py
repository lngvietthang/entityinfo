# -*- encoding: utf8 -*-
import io
import regex as re

def load_patterns(patternFile):
    patterns = []
    with io.open(patternFile, encoding='utf8') as fin:
        for line in fin:
            line = line.strip()
            if line != "" and line[0] != '#':
                key, value = line.split(',')
                value = value[2:-1]
                # print key, value
                patterns.append((key, ur"{}".format(value)))

    return patterns

def detect_ask_entity_info(str, patterns):
    for patt in patterns:
        if re.search(patt[1], str.lower(), flags=re.UNICODE):
            return patt[0]
    return None


def main():
    personInfoPattFile = 'person-info-temp.txt'
    personInfoPatt = load_patterns(personInfoPattFile)
    countryInfoPattFile = 'country-info-temp.txt'
    countryInfoPatt = load_patterns(countryInfoPattFile)

    lstTestCases = [u"chiều cao của Bùi Anh Tuấn là bao nhiêu",
                    u"Diện tích của Hoa Kỳ là bao nhiêu",
                    u"Ngày mai là thứ mấy",
                    u"Bác Hồ sinh ngày mấy"]

    for test in lstTestCases:
        print test, detect_ask_entity_info(test, personInfoPatt + countryInfoPatt)


if __name__ == '__main__':
    main()
