# ==========================================================================================================================================================#
#                                                   test_requirements.py - Test availability of required packages
# ==========================================================================================================================================================#
import unittest
import pkg_resources

from pathlib import Path

_REQUIREMENTS_PATH = Path(__file__).parent.with_name("requirements.txt")
#_REQUIREMENTS_PATH = "requirements/Windows_on_Python3.9.2/requirements.txt"
print(_REQUIREMENTS_PATH)

class TestRequirements(unittest.TestCase):
    """Test availability of required packages."""

    def test_requirements(self):
        """Test that each required package is available."""
        # Ref: https://stackoverflow.com/a/45474387/
        requirements = pkg_resources.parse_requirements(_REQUIREMENTS_PATH.open())
        for requirement in requirements:
            requirement = str(requirement)
            with self.subTest(requirement=requirement):
                pkg_resources.require(requirement)

TestRequirements.test_requirements()