import sys
import os
import requests
from bs4 import BeautifulSoup
from collections import deque
from colorama import init, Fore

init(autoreset=True)

agrs = sys.argv
save_dir = agrs[1]
history = deque()

if not os.path.exists(save_dir):
    os.mkdir(save_dir)

selected_tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li']


def print_content_request(request):
    soup = BeautifulSoup(request.content, 'html.parser')
    elements = soup.find_all(selected_tags)
    links = soup.find_all('a')
    for link in links:
        print(Fore.BLUE + link.text)
    for element in elements:
        print(element.text)


def read_file(dir_name):
    with open(dir_name) as page:
         for line in page:
             print(line.strip())


def save_content_request(request, dir_name):
    soup = BeautifulSoup(request.content, 'html.parser')
    elements = soup.find_all(selected_tags)
    links = soup.find_all('a')
    # write the file if not exist
    if not os.path.isfile(dir_name):
        with open(dir_name, 'w') as file:
            for link in links:
                file.write(Fore.BLUE + link.text)
            for element in elements:
                file.write(element.text)


while True:
    command = input()

    if command == 'exit':
        break

    if command == 'back':
        try:
            print(history.pop())
        except IndexError:
            pass

    if command in os.listdir(save_dir):
        os.chdir(save_dir)
        read_file(command)
        os.chdir('..')
    elif '.' in command:
        os.chdir(save_dir)

        name_to_save = command
        if not command.startswith(r'http://'):
            command = r'http://' + command

        req = requests.get(command)
        # print_content_request(req)
        save_content_request(req, name_to_save)
        read_file(name_to_save)

        os.chdir('..')
    else:
        print('Error: Incorrect URL')
#
#
# def save_page(name, content):
#     if not os.path.isfile(dir + '/' + name.rstrip('.com')):
#         with open(dir + '/' + name.rstrip('.com'), 'w') as file:
#             file.write(str(content))
#
#
# def search_page_in_file(url):
#     if os.path.isfile(dir + '/' + url.lstrip(base_url)):
#         with open(dir + '/' + url.lstrip(base_url), 'r') as file:
#             return file.read()
#     else:
#         return search_page_in_web(url=url, base_url=base_url)
#
#
# def search_page_in_web(url, base_url):
#     url.lstrip(base_url)
#     base_url += url
#     response = requests.get(url=base_url)
#
#     if response.status_code == 200:
#         content_text = ''
#         soup = BeautifulSoup(response.content, 'html.parser')
#         p = soup.find_all('p')
#         titles = soup.find_all('title')
#         ul = soup.find_all('ul')
#         li = soup.find_all('li')
#         ol = soup.find_all('ol')
#         a = soup.find_all('a')
#         h = soup.find_all('h1')
#         h.extend(soup.find_all('h2'))
#         h.extend(soup.find_all('h3'))
#         h.extend(soup.find_all('h4'))
#         h.extend(soup.find_all('h5'))
#         h.extend(soup.find_all('h6'))
#
#         for tag in titles:
#             content_text += tag.text + '\n'
#
#         for tag in a:
#             content_text += Fore.BLUE + tag.text + '\n'
#
#         for tag in p:
#             content_text += tag.text + '\n'
#
#         for tag in ul:
#             content_text += tag.text + '\n'
#
#         for tag in li:
#             content_text += tag.text + '\n'
#
#         for tag in ol:
#             content_text += tag.text + '\n'
#
#         for tag in h:
#             content_text += tag.text + '\n'
#
#         return content_text
#
#     return response.content


# write your code here
# while True:
#
#     url = input()
#
#     if 'exit' in url:
#         break
#     elif 'back' in url:
#         stack.pop()
#         print(stack[len(stack) - 1])
#     elif 'nytimescom' in url:
#         stack.append(nytimes_com)
#         print(stack[len(stack) - 1])
#     elif 'bloombergcom' in url:
#         stack.append(bloomberg_com)
#         print(stack[len(stack) - 1])
#     else:
#         content = search_page_in_file(url)
#         if content != 'Error: Incorrect URL':
#             stack.append(content)
#             save_page(name=url.lstrip(base_url), content=content)
#             print(stack[len(stack) - 1])
#         else:
#             print(content)
