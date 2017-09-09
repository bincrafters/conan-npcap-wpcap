from conans import ConanFile, CMake
import os


class NpcapWpcapTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    username = os.getenv("CONAN_USERNAME", "bincrafters")
    channel = os.getenv("CONAN_CHANNEL", "testing")
    requires = "Catch/1.9.6@uilianries/stable"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir=self.conanfile_directory, build_dir="./")
        cmake.build()

    def imports(self):
        self.copy("*", dst="bin", src="lib")
        self.copy("*", dst="bin", src="bin")

    def test(self):
        cmake = CMake(self)
        cmake.test()
