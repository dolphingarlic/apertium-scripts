import re

fin = open('morphology.txt', 'r')
fout = open('formatted_morphology.txt', 'w')

for line in fin:
    morph_list = re.findall(r'\^.*?\$', line)

    for word in morph_list:
        choices = word[1:-1].split('/')
        fout.write('\"<{}>\"\n'.format(choices[0]))

        for choice in choices[1:]:
            morphology = choice.split('<')
            fout.write('\t\"{}\"'.format(morphology[0]))

            for identifier in morphology[1:]:
                fout.write(' {}'.format(identifier[:-1]))

            fout.write('\n')

fout.close()
fin.close()
