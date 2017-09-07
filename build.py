from conan.packager import ConanMultiPackager, os


if __name__ == "__main__":
    builder = ConanMultiPackager(username=os.getenv("CONAN_USERNAME"), channel="stable")
    builder.add_common_builds()
    builder.run()
