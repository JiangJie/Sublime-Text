import sublime
import sublime_plugin


class UsestrictCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "'use strict';\n\n")
