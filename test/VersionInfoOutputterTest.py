import unittest

from gitversionbuilder import VersionInfo
from gitversionbuilder import VersionInfoOutputter


class VersionInfoOutputterTest(unittest.TestCase):
    def test_output_cpp(self):
        expected = """
                // ---------------------------------------------------
                // This file is autogenerated by git-version-builder.
                // DO NOT MODIFY!
                // ---------------------------------------------------

                #pragma once
                #ifndef __GITVERSIONBUILDER__VERSION_H__
                #define __GITVERSIONBUILDER__VERSION_H__

                namespace version {
                    constexpr const char *VERSION_STRING = "v1.6-2-g230a";
                    constexpr const char *TAG_NAME = "v1.6";
                    constexpr const unsigned int COMMITS_SINCE_TAG = 2;
                    constexpr const char *GIT_COMMIT_ID = "230a";
                }

                #endif
            """
        actual = VersionInfoOutputter.to_cpp(VersionInfo.VersionInfo("v1.6", 2, "230a"))
        self.assertCodeEqual(expected, actual)

    def test_output_python(self):
        expected = """
                # ---------------------------------------------------
                # This file is autogenerated by git-version-builder.
                # DO NOT MODIFY!
                # ---------------------------------------------------

                VERSION_STRING = "v1.6-2-g230a"
                TAG_NAME = "v1.6"
                COMMITS_SINCE_TAG = 2
                GIT_COMMIT_ID = "230a"
            """
        actual = VersionInfoOutputter.to_python(VersionInfo.VersionInfo("v1.6", 2, "230a"))
        self.assertCodeEqual(expected, actual)

    def assertCodeEqual(self, expected, actual):
        self.assertEqual(self._normalize(expected), self._normalize(actual))

    def _normalize(self, string):
        lines = string.splitlines()
        normalized_lines = map(self._normalize_line, lines)
        without_empty_lines = filter(None, normalized_lines)
        return "\n".join(without_empty_lines)

    def _normalize_line(self, line):
        tokens = line.split()
        return " ".join(tokens)


if __name__ == '__main__':
    unittest.main()
