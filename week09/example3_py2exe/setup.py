from distutils.core import setup
import py2exe
import os

__version__ = "0.0.1"

INNOSETUP_COMPILER = r'C:\InnoSetup\ISCC.exe'
############################################################
# Based on code from py2exe/samples/extending

class InnoScript:
    def __init__(self,
                 name,
                 lib_dir,
                 dist_dir,
                 console_exe_files = [],
                 lib_files = [],
                 version = "1.0"):
        self.lib_dir = lib_dir
        self.dist_dir = dist_dir
        if not self.dist_dir[-1] in "\\/":
            self.dist_dir += "\\"
        self.name = name
        self.version = version
        self.console_exe_files = [self.chop(p) for p in console_exe_files]
        self.lib_files = [self.chop(p) for p in lib_files]

    def chop(self, pathname):
        assert pathname.startswith(self.dist_dir)
        return pathname[len(self.dist_dir):]
    
    def create(self, pathname=None):
        if not pathname:
            pathname = os.path.join(self.dist_dir, self.name) + '.iss'
        print "InnoSetup script: %s" % pathname
        self.pathname = pathname
        ofi = self.file = open(pathname, "w")
        print >> ofi, "; WARNING: This script has been created by py2exe. Changes to this script"
        print >> ofi, "; will be overwritten the next time py2exe is run!\n"
        print >> ofi, r"[Setup]"
        print >> ofi, r"AppName=%s" % self.name
        print >> ofi, r"AppVersion=%s" % (self.version)
        print >> ofi, r"AppVerName=%s %s" % (self.name, self.version)
        print >> ofi, r"AppPublisher=Vulcan Inc."
        print >> ofi, r"DefaultDirName=C:\%s" % self.name
        print >> ofi, r"DefaultGroupName=%s" % self.name
        print >> ofi, r"Compression=lzma"
        print >> ofi, r"OutputDir=%s" % self.dist_dir
        print >> ofi, r"OutputBaseFilename=%s_%s_Setup" % (self.name,
                self.version)
        print >> ofi

        print >> ofi, r"[Files]"
        for path in self.console_exe_files + self.lib_files:
            flags = 'ignoreversion'
            if path.lower().endswith('.cfg'):
                flags += ' onlyifdoesntexist ' 
            print >> ofi, r'Source: "%s"; DestDir: "{app}\%s"; Flags: %s' % (path, os.path.dirname(path), flags)
        print >> ofi

        print >> ofi, r"[InstallDelete]"
        for path in filestodelete:
            print >> ofi, r'Type: filesandordirs; Name: "{app}\%s"' % path
        print >> ofi

        ofi.close()

    def compile(self):
        cmd = "%s %s" % (INNOSETUP_COMPILER, self.pathname)
        print "Running InnoSetup: %s" % cmd
        errorlevel = os.system(cmd)
        print "InnoSetup returned errorlevel: %s" % errorlevel


################################################################

from py2exe.build_exe import py2exe

class debug_installer(py2exe):
    def run(self):
        # First, let py2exe do it's work.
        py2exe.run(self)
        from pprint import pprint
        print "#" * 79
        print "#" * 79
        pprint(vars(self))
        
class build_installer(py2exe):
    # This class first builds the exe file(s), then 
    # creates a Windows installer.
    # You need InnoSetup installed into C:\InnoSetup.
    def run(self):
        # First, let py2exe do it's work.
        py2exe.run(self)

        lib_dir = self.lib_dir
        dist_dir = self.dist_dir
        
        # create the Installer, using the files py2exe 
        # has created.
        script = InnoScript("Hello",
                            lib_dir,
                            dist_dir,
                            self.console_exe_files,
                            self.lib_files,
                            __version__)
        print "*** creating the inno setup script***"
        script.create()
        print "*** compiling the inno setup script***"
        script.compile()
        # Note: By default the final setup.exe will 
        # be in an Output subdirectory.

##############################################################
## Main setup

# Used to tell InnoSetup which files to delete if found. 
filestodelete = ["some_old_file.txt"]

class Target:
    def __init__(self, **kw):
        # for the versioninfo resources
        self.name = "Name"
        self.description = "This is the description"
        self.company_name = "Company Name Inc."
        self.copyright = "Copyright 2004 Company Name Inc."
        self.version = __version__
        self.__dict__.update(kw)

setup(
    zipfile = "lib/library.zip",
    console = [ Target(script = "hello.py",
                    name = "hello",
                    description = "Print hello."),
                Target(script = "environment.py",
                    name = "environment",
                    description = "Print environment."),
                ],
    cmdclass = {"py2exe": build_installer},
    )



