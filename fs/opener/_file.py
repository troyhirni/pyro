"""
Copyright 2017 Troy Hirni
This file is part of the pyro project, distributed under
the terms of the GNU Affero General Public License.
"""

class Opener(object):
	def open(self, *a, **k):
		return file(*a, **k)
