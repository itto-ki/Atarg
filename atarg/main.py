import argparse

import parse_html
import execute


def parse_arguments():
    CONTESTS = ['ABC', 'ARC', 'AGC']
    TASKS = ['A', 'B', 'C', 'D']
    parser = argparse.ArgumentParser(
            prog='Atcoder Auto Tester',
            description='Testing tool before submit for atcoder',
            epilog='end',
            add_help=True,
            )
    parser.add_argument('contest', choices=CONTESTS, help='Contest name')
    parser.add_argument('number', type=int, help='Contest number')
    parser.add_argument('task', choices=TASKS, help='Task name')
    parser.add_argument(
            'command',
            help='Commands to solve',
            nargs='*')
    return parser.parse_args()


def main():
    args = parse_arguments()
    task = parse_html.translate_task(args.contest, args.number, args.task)
    url = parse_html.compose_url(args.contest, args.number, task)
    inouts = parse_html.get_inouts(url, args.contest, args.number)
    in_list = inouts[::2]
    out_list = inouts[1::2]
    execute.run_tests(in_list, out_list, args.command)


if __name__ == '__main__':
    main()
