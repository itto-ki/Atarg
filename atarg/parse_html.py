import requests
from bs4 import BeautifulSoup


def get_inouts(url: str, contest: str, contest_number: int) -> [str]:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    pre_list = soup.find_all('pre')
    contest_number = contest_number
    inouts = list(map(
        lambda tag: tag.get_text().strip(),
        pre_list[1:]))    # 入力例は除外する
    if contest == 'ABC':
        if 1 <= contest_number <= 41:
            return inouts
        else:
            return inouts[:int(len(inouts)/2)]
    elif contest == 'ARC':
        pass
    elif contest == 'AGC':
        pass


def translate_task(contest: str, contest_number: int, task: str) -> str:
    translator = {'A': '1', 'B': '2', 'C': '3', 'D': '4'}
    if contest == 'ABC':
        if 1 <= contest_number <= 19:
            return translator[task]
        else:
            return task.lower()
    elif contest == 'ARC':
        pass
    elif contest == 'AGC':
        pass


def compose_url(contest: str, contest_number: int, task: str) -> str:
    host = 'https://beta.atcoder.jp/'
    return host + 'contests/' + contest.lower()\
            + '{:03d}'.format(contest_number)\
            + '/tasks/' + contest.lower()\
            + '{:03d}'.format(contest_number)\
            + '_' + task
