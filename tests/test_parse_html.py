import unittest
from atarg import parse_html


class HTMLParserTest(unittest.TestCase):
    def test_fetch_input_and_output(self):
        self.assertEqual(
                parse_html.fetch_input_and_output(
                    'https://beta.atcoder.jp/contests/abc020/tasks/abc020_a',
                    'ABC', 20),
                ['1', 'ABC', '2', 'chokudai'])
        self.assertEqual(
                parse_html.fetch_input_and_output(
                    'https://beta.atcoder.jp/contests/abc001/tasks/abc001_1',
                    'ABC', 1),
                ['15\r\n10', '5', '0\r\n0', '0', '5\r\n20', '-15'])

    def test_translate_task(self):
        self.assertEqual(parse_html.translate_task('ABC', 19, 'A'), '1')
        self.assertEqual(parse_html.translate_task('ABC', 20, 'A'), 'a')

    def test_compose_url(self):
        self.assertEqual(
                parse_html.compose_url('ABC', 19, '1'),
                'https://beta.atcoder.jp/contests/abc019/tasks/abc019_1')
        self.assertEqual(
                parse_html.compose_url('ABC', 20, 'a'),
                'https://beta.atcoder.jp/contests/abc020/tasks/abc020_a')


if __name__ == '__main__':
    unittest.main()
