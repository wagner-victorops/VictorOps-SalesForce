import csv
import os

home_directory = str(os.path.expanduser('~'))

in_file = home_directory + '/Downloads/customer_email_domains.csv'

out_file = home_directory + '/Downloads/customer_email_domains_final.csv'

domains = []

ignored_domains = [
    'aol.com',
    'att.net',
    'comcast.net',
    'facebook.com',
    'gmail.com',
    'gmx.com',
    'googlemail.com',
    'google.com',
    'hotmail.com',
    'hotmail.co.uk',
    'mac.com',
    'me.com',
    'mail.com',
    'msn.com',
    'live.com',
    'sbcglobal.net',
    'verizon.net',
    'yahoo.com',
    'yahoo.co.uk',
    'gmx.net',
    'hush.com',
    'hushmail.com',
    'icloud.com',
    'outlook.com',
    'pobox.com',
    'protonmail.com',
    'zoho.com',
    'yandex.com',
    'bellsouth.net',
    'charter.net',
    'cox.net',
    'earthlink.net',
    'juno.com',
    'btinternet.com',
    'virginmedia.com',
    'blueyonder.co.uk',
    'freeserve.co.uk',
    'live.co.uk',
    'ntlworld.com',
    'o2.co.uk',
    'orange.net',
    'sky.com',
    'talktalk.co.uk',
    'tiscali.co.uk',
    'virgin.net',
    'wanadoo.co.uk',
    'bt.com',
    'sina.com',
    'sina.cn',
    'qq.com',
    'naver.com',
    'hanmail.net',
    'daum.net',
    'nate.com',
    'yahoo.co.jp',
    'yahoo.co.kr',
    'yahoo.co.id',
    'yahoo.co.in',
    'yahoo.com.sg',
    'yahoo.com.ph',
    '163.com',
    '126.com',
    'aliyun.com',
    'foxmail.com',
    'hotmail.fr',
    'live.fr',
    'laposte.net',
    'yahoo.fr',
    'wanadoo.fr',
    'orange.fr',
    'gmx.fr',
    'sfr.fr',
    'neuf.fr',
    'free.fr',
    'web.de',
    'yahoo.de',
    'libero.it',
    'virgilio.it',
    'hotmail.it',
    'aol.it',
    'tiscali.it',
    'alice.it',
    'live.it',
    'yahoo.it',
    'email.it',
    'tin.it',
    'poste.it',
    'teletu.it',
    'mail.ru',
    'rambler.ru',
    'yandex.ru',
    'ya.ru',
    'list.ru',
    'hotmail.be',
    'live.be',
    'skynet.be',
    'voo.be',
    'tvcablenet.be',
    'telenet.be',
    'hotmail.com.ar',
    'live.com.ar',
    'yahoo.com.ar',
    'fibertel.com.ar',
    'speedy.com.ar',
    'arnet.com.ar',
    'yahoo.com.mx',
    'live.com.mx',
    'hotmail.es',
    'hotmail.com.mx',
    'prodigy.net.mx',
    'yahoo.com.br',
    'hotmail.com.br',
    'outlook.com.br',
    'uol.com.br',
    'bol.com.br',
    'terra.com.br',
    'ig.com.br',
    'itelefonica.com.br',
    'r7.com',
    'zipmail.com.br',
    'globo.com',
    'globomail.com',
    'oi.com.br'
]

with open(in_file, "r", encoding='utf-8') as file:
    r = csv.reader(file)
    next(r, None)
    for row in r:
        if len(row) > 0 and ',' not in str(row):
            if row[0] not in domains:
                domains.append(row[0])
        elif ',' in str(row):
            comma_sep_list = row
            sub_list = comma_sep_list[0].split(",")
            for domain in sub_list:
                if domain not in domains:
                    domains.append(domain)

for d in domains:
    if d in ignored_domains:
        domains.remove(d)
    if d == '':
        domains.remove(d)
    if ' ' in d:
        new_string = d.strip()
        domains.remove(d)
        domains.append(new_string)

trimmed_list = domains[:-6]
final_list = []

for domain in trimmed_list:
    formatted_domain = str("*." + domain)
    final_list.append(formatted_domain)

print(str(len(final_list)) + " total domains")
final_list.sort()

with open(out_file, 'w', encoding='utf-8') as output:
    w = csv.writer(output, lineterminator='\n')
    w.writerow(["Email Domain"])
    for domain in final_list:
        w.writerow([domain])
