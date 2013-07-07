import unittest
from taskpaper import TaskPaper


class EmptyObject(unittest.TestCase):
    def test_empty_taskpaper(self):
        "should handle empty object okay"
        til = TaskPaper()
        self.assertEqual(0, len(til.items))
        self.assertEqual(0, til.level())


class EmptyFile(unittest.TestCase):
    def test_missing_input(self):
        "Must pass input to parse"
        self.assertRaises(TypeError, TaskPaper.parse, (None,))

    def test_empty_input(self):
        "should handle empty file okay"
        til = TaskPaper.parse('')
        self.assertEqual(0, len(til.items))


class ParseString(unittest.TestCase):
    def test_one_level(self):
        "Can't parse string, but doesn't error"
        input_string = 'project 1:\n\t- task 1\n\t- task 2\n'
        til = TaskPaper.parse(input_string)
        # will claim some large number of items
        self.assertTrue(len(til.items) > 3)

    def test_list_of_strings(self):
        lines = 'project 1:\n\t- task 1\n\t- task 2\n'.splitlines()
        til = TaskPaper.parse(lines)
        # one top level item
        self.assertEqual(1, len(til.items))
        # 3 total items
        self.assertEqual(3, sum(1 for _ in til))


class TagHandling(unittest.TestCase):
    lines = 'project 1 @tag1:\n\t- task 1 @tag1(content) @tag2(content)\n' \
            '\t- task 2 @tag2(multi word)\n'.splitlines()

    def test_find_all_tags(self):
        "Find all tags"
        til = TaskPaper.parse(self.lines)
        tag_count = sum(len(i.tags.keys()) for i in til)
        self.assertEqual(4, tag_count)

    def test_find_desired_tags(self):
        "find just specified tags"
        til = TaskPaper.parse(self.lines)
        for tag in ('tag1', 'tag2'):
            tag_count = sum(1 for _ in til.select(lambda _: tag in _.tags))
            self.assertEqual(2, tag_count)


class FormatCorrectness(unittest.TestCase):
    def test_format_no_tags(self):
        line = 'project 1:\n\t- task 1\n\tcomment 1'
        til = TaskPaper.parse(line.splitlines())
        output = til.format()
        self.assertEqual(line, output)


if __name__ == '__main__':
    unittest.main()
