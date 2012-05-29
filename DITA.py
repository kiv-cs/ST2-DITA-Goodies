import sublime, sublime_plugin

class DitaCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
		sels = self.view.sel()
		left_border = '<%s>' % args['tagname']
		right_border = '</%s>' % args['tagname']
		for sel in sels:
			self.insert_borders(edit, left_border, right_border, sel.begin(), sel.end())

	def insert_borders(self, edit, left_border, right_border, left_position, right_position):
		self.view.insert(edit, left_position, left_border)
		self.view.insert(edit, right_position + len(left_border), right_border)