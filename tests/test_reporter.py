from unittest import TestCase
from specter.reporting.console import ConsoleReporter


class TestConsoleReporter(TestCase):

    def setUp(self):
        self.default_reporter = ConsoleReporter()

    def test_get_name(self):
        self.assertEqual(self.default_reporter.get_name(),
                         'Temporary console reporter')

    def test_process_args(self):
        class dotted_dict(object):
            def __getattr__(self, attr):
                return self.__dict__.get(attr)

        args = dotted_dict()
        args.no_color = True

        self.default_reporter.process_arguments(args)
        self.assertFalse(self.default_reporter.use_color)

    def test_no_color_print(self):
        self.default_reporter.use_color = False
        self.default_reporter.print_colored('bam')
        # When we unify the print to console, add a test here to cover this
