#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import subprocess

from book_tester import ChapterTest, DO_SERVER_COMMANDS
LOCAL = False

class Chapter9Test(ChapterTest):
    chapter_name = 'chapter_manual_deployment'
    previous_chapter = 'chapter_prettification'

    def setUp(self):
        super().setUp()
        if DO_SERVER_COMMANDS:
            subprocess.check_call(['vagrant', 'snapshot', 'restore', 'MANUAL_1'])


    def test_listings_and_commands_and_output(self):
        self.parse_listings()

        # sanity checks
        self.assertEqual(self.listings[0].type, 'code listing with git ref')
        self.assertEqual(self.listings[1].type, 'test')

        self.start_with_checkout()

        # skips
        self.skip_with_check(18, 'replace the URL in the next line with')


        # hack fast-forward
        skip = False
        if skip:
            self.pos = 8
            self.sourcetree.run_command('git checkout {0}'.format(
                self.sourcetree.get_commit_spec('ch08l001')
            ))

        while self.pos < len(self.listings):
            listing = self.listings[self.pos]
            print(self.pos, listing.type, repr(listing))
            self.recognise_listing_and_process_it()

        self.assert_all_listings_checked(self.listings)
        self.check_final_diff()



if __name__ == '__main__':
    unittest.main()
