from conans import ConanFile, tools, os


class NpcapWpcapConan(ConanFile):
    name = "npcap-wpcap"
    version = "0.93"
    license = "NPCAP License"
    url = "https://github.com/bincrafters/conan-npcap"
    source_url = "https://github.com/nmap/npcap"
    settings = "arch", "compiler", "build_type"  
    lib_parent_name = "npcap"
    build_requires = "npcap-dll/0.93@bincrafters/testing"

    def source(self):
        self.run("git clone --recursive --single-branch --depth 1 --branch=v{0} {1}.git".format(self.version, self.source_url)) 
    
    def build(self):
        os.environ["VisualStudioVersion"]="" 
        # Above required to compile for VS14 from VS15
        # which is currently blocked conan due to a precondition on vcvarsall.bat

        sln_path = os.path.join("wpcap", "libpcap", "Win32", "Prj")
        sln_file = os.path.join(sln_path, "wpcap.sln")
        proj_file = os.path.join(sln_path, "wpcap.vcxproj")
   
        unzip_dir = "{0}".format(self.lib_parent_name)
        sln_path_full = os.path.join(unzip_dir, sln_file)
        proj_path_full = os.path.join(unzip_dir, proj_file)
        npcap_dep = self.deps_cpp_info["npcap-dll"]
        npcap_lib_file = os.path.join(npcap_dep.rootpath, npcap_dep.libdirs[0], "Packet.lib")
        tools.replace_in_file(proj_path_full, r'..\..\..\..\packetWin7\Dll\Project\Release No NetMon and AirPcap\Packet.lib', npcap_lib_file)
        tools.replace_in_file(proj_path_full, r'..\..\..\..\packetWin7\Dll\Project\x64\Release No NetMon and AirPcap\Packet.lib', npcap_lib_file)
        build_command = tools.msvc_build_command(self.settings, sln_path_full,  targets=["Build"], upgrade_project=False)
        
        if self.settings.arch == "x86":
            self.run(build_command.replace('"x86"', '"Win32"'))
        else:
            self.run(build_command)
            
    def package(self):
        libpcap_root = os.path.join(self.lib_parent_name, "wpcap","libpcap")
        self.copy("*.h", dst="include", src=libpcap_root)
        
        win32_ext_dir = os.path.join(self.lib_parent_name, "wpcap", "Win32-Extensions")
        self.copy("Win32-Extensions.h", dst="include", src=win32_ext_dir)
        
        arch_path = "x64" if self.settings.arch == "x86_64" else "x86"
        lib_dir = os.path.join(libpcap_root, "Win32", "Prj", arch_path, str(self.settings.build_type))
        self.copy("wpcap.lib", dst="lib", src=lib_dir, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = self.collect_libs()
