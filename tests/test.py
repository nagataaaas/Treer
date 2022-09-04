import unittest
import treer


class TreerTest(unittest.TestCase):
    def test_dir(self):
        root = treer.DirTree.from_path(r'test_dir')
        self.assertIsInstance(root, treer.DirTree)
        self.assertEqual(root.name, '\x1b[36m\x1b[1mtest_dir\x1b[39m\x1b[22m\x1b[0m')
        root.colorize = False
        self.assertEqual(root.name, 'test_dir')
        self.assertEqual(root.draw(), '''test_dir
 ├── dir1
 │    ├── dir1-1
 │    │    └── dir1-1-1
 │    ├── dir1-2
 │    └── *dir1-3
 ├── dir1-1
 └── dir2
      ├── dir2-1
      └── dir2-2''')

    def test_mapping(self):
        root = treer.Tree.from_mapping({
            'root': {
                'dir1': {
                    'file1': None,
                    'file2': None,
                    'dir1-2': {
                        'file3': None,
                    },
                },
                'dir2': {
                    'file4': None,
                },
                'dir3': [
                    'file5',
                    'file6',
                ],
                'dir4': 'file8'
            }
        })
        self.assertIsInstance(root, treer.MapTree)
        root.colorize = False
        self.assertEqual(root.draw(), '''root
 ├── dir1
 │    ├── file1
 │    ├── file2
 │    └── dir1-2
 │         └── file3
 ├── dir2
 │    └── file4
 ├── dir3
 │    ├── file5
 │    └── file6
 └── dir4
      └── file8''')


if __name__ == '__main__':
    unittest.main()
