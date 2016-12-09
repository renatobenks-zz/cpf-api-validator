# Unittest lib
import unittest

# Call controller
from app.Controllers.UserCPFController.UserCPFController import UserCPFController


class TestCpfGenerated(unittest.TestCase):
    def testReturnWhenUserNotExists(self):
        message_error = {
            "message": {
                "error": "username sent don't found"
            }
        }

        self.assertEqual(UserCPFController.getGeneratedCpf([], 1), message_error)

    def testResponseForExistIssue(self):
        pass
