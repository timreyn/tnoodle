import tmt
import os

class Project(tmt.TmtProject):
	def getDependencies(self):
		return [ tmt.TmtProject.projects['jsracer'] ]

	def compile(self):
		oldDir = self._chdir()
		retVal, stdout, stderr = tmt.runCmd([ 'npm', 'install', '-d' ], showStatus=True)
		assert retVal == 0
		os.chdir(oldDir)

	def _chdir( self ):
		oldDir = os.path.abspath('.')
		os.chdir(tmt.projectName())
		return oldDir

	def run(self):
		self.compile()
		oldDir = self._chdir()
		tmt.runCmd([ 'node', 'noderacer.js' ], interactive=True)
		os.chdir(oldDir)

	def clean(self):
		pass

Project(tmt.projectName(), description="A nodejs server that multicasts turns to its clients")
