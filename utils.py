import re
crazy_regex = r"(Den \d{1,2}\. \w+ \d{4})\n*Aktdetaljer\n*Akttitel:(.*)Aktnummer: *(\d+)\nSagsnummer: *(\d* *- *\d*)\n*Akt-ID:\n*(\d*)\n*Dato:\n*Type:\n*([\d-]+\s[\d:]+)\n+(\S*)\n*Dokumenter:\n*(.*)"


crazy = r"(Den \d{1,2}\. \w+ \d{4})\n*Aktdetaljer\n*Akttitel:(.*)Aktnummer: *(\d+)\nSagsnummer: *(\d* *- *\d*)\n*Akt-ID:\n*(\d*)\n*Dato:\n*Type:\n*([\d-]+\s[\d:]+)\n+(\S*)\n*Dokumenter:\n*(.*)"


covercheck_regex = r"(\d{1,2}\. \w+ \d{4})\n+Aktdetaljer\n+Akttitel:"
simple_covercheck_regex = r'Aktdetaljer'


regex2 = r"Akt"

def get_matches(text):
    # text = text.replace("[", "\[").replace("]", "\]").replace("(", "\(").replace(")", "\)")
    # print (text)
    matches = re.search(crazy, text)

    if matches is None: return []
    return matches


def is_cover(text):
    if re.search(simple_covercheck_regex, text) is not None:
        return True


def is_document(text):
    if re.search(r"== ", text) is not None:
        return True

def get_cover_details(text):
    result = {}
    if not is_cover(text): return result
    
    regex_dict = {
        'Akttitel': r'Akttitel: *(.+)Aktnummer',
        'Aktnummer': r'Aktnummer: *(\d+)\n',
        'Sagsnummer': r'Sagsnummer: *(.\d+ - \d+)\n',
        'Akt-ID': r'Akt-ID: *\n*(\d+)',
        'Dato': r'Dato:\nType:\n([^\n]+)\n',
        'Type': r'Dato:\nType:\n[^\n]+\n([^\n]+)\n',
        'Dokumenter': r'Dokumenter:\n(.+)'


    }


    for key, regex in regex_dict.items():

        result[key] = re.search(regex, text, re.DOTALL).group(1) if re.search(regex, text, re.DOTALL) else None

    return result


if __name__ == '__main__':
    test_text = """Den 22. februar 2023
Aktdetaljer
Akttitel: Udkast til materiale til styregruppemøde 17.
marts mm (Arb. grp. industriudledn. MFS)
Aktnummer: 193
Sagsnummer: 2020 - 2896
Akt-ID:
6637667
Dato:
Type:
13-03-2020 11:48:57
Udgående
Dokumenter:
[1] Udkast til materiale til styregruppemøde 17. marts mm (Arb. grp.
industriudledn. MFS).eml
[2] Bilag 1 Delopgaver - juridiske løsningsspor.docx
[3] Organisering og tidsplan - juridisk løsningsspor.docx"""


    print (is_cover(test_text))
    print (get_cover_details(test_text))