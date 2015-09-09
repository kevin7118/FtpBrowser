#!/usr/bin/python
# -*- coding: utf-8 -*-

import sublime
from sublime_plugin import WindowCommand, TextCommand
from . import treeview
import os
from os.path import basename

DEMO_PATH = 'D:\\Workspace\\SublimeFileBrowser\\'

def show(window, path):
	view = window.new_file()
	view.set_scratch(True)

	if path == os.sep:
		view_name = path
	else:
		view_name = basename(path.rstrip(os.sep))

	name = u"𝌆 {0}".format(view_name)
	view.set_name(name)
	view.settings().set('base_path', path)
	window.focus_view(view)


class FtpBrowserCommand(WindowCommand):
	def run(self):
		show(self.window, DEMO_PATH)


class DirTreeCommand(TextCommand, TreeView):
	def run(self):
		pass

	def populate_view():
		pass

	def continue_refreshing():
		pass
		