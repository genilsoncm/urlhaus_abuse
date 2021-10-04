import urllib.request
import re

contents = urllib.request.urlopen("https://urlhaus.abuse.ch/downloads/text_online/").read()
contents = str(contents,'utf-8')


file_type = input('Digite "[i]" para gerar uma lista ip ou "[d]" para domain: ')

def print_file(input, file_name):
     with open(file_name, "w") as file:
            for i in input:
                file.write(i)
                file.write("\n")




def generate_list(file_type, contents):
    if 'i' == file_type: 
        ip = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", contents)
        ip = set(ip)
        print_file(ip, 'ip.txt')

    elif 'd' == file_type:
        domain = re.findall('://([\w\-\.]+)', contents)
        domain = set(domain)
        domain = filter(lambda x: x[0].isdigit() == False, domain)
        print_file(domain, 'domain.txt')

    else:
        print('Not permitted')

    


generate_list(file_type, contents)



