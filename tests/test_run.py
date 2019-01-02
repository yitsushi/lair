import os
from pyfakefs.fake_filesystem_unittest import TestCase
from lair.run import main
import lair


class TestRun(TestCase):
    def setUp(self):
        # We need all the template files
        # and now, I don't know better solution for that
        real_template_dir = os.path.join(
            os.path.dirname(lair.__file__),
            'templates')

        self.setUpPyfakefs()
        self.fs.add_real_directory(real_template_dir)

    def test_no_args(self):
        with self.assertRaises(SystemExit) as cm:
            main()

        self.assertEqual(cm.exception.code, 2)

    def test_project_name(self):
        main(['--project-name=test-project'])

        self.assertTrue(os.path.isdir('test-project'))
        self.assertTrue(os.path.isfile('test-project/requirements.txt'))

        with open('test-project/requirements.txt', 'r') as f:
            self.assertEqual(f.read(), 'flask\nkonfig\n')

    def test_project_name_rerun(self):
        main(['--project-name=test-project'])

        self.assertTrue(os.path.isdir('test-project'))
        self.assertTrue(os.path.isfile('test-project/requirements.txt'))

        with open('test-project/requirements.txt', 'r') as f:
            self.assertEqual(f.read(), 'flask\nkonfig\n')

        with self.assertRaises(SystemExit) as cm:
            main(['--project-name=test-project'])

        self.assertEqual(cm.exception.code, 1)

    def test_dependencies(self):
        main(['--project-name=test-project', '--dependencies=random,something'])

        self.assertTrue(os.path.isdir('test-project'))
        self.assertTrue(os.path.isfile('test-project/requirements.txt'))

        with open('test-project/requirements.txt') as f:
            self.assertEqual(f.read(), 'random\nsomething\n')