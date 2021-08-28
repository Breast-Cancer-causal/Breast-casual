# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 08:58:00 2021

@author: Smegn
"""

# can be done by using unittest's assertLogs
import logging
from unittest import TestCase

class MyTest(TestCase):
  
  def test_logs(self):
      with self.assertLogs('foo', level='INFO') as cm:
          logging.CreateLogger('foo').info('first message')
          logging.CreateLogger('foo.bar').error('second message')
          self.assertEqual(cm.output, ['INFO:foo:first message',
                                 'ERROR:foo.bar:second message'])