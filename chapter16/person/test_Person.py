import unittest

import Person as PersonClass

class Test(unittest.TestCase):
    """
    The basic class that inherits unittest.TestCase
    """
    person = PersonClass.Person()
    user_id = []
    user_name = []

    def test_0_set_name(self):
        print("Start set_name test\n")
        """
        Any method which starts sith 'test_' will be considered as a test case
        """
        for i in range(4):
            name = 'name' + str(i)
            self.user_name.append(name)
            user_id = self.person.set_name(name)
            self.assertIsNotNone(user_id)
            self.user_id.append(user_id)
        print("user_id length =", len(self.user_id))
        print(self.user_id)
        print("user_name length =", len(self.user_name))
        print(self.user_name)
        print("\nFinish set_name tests\n")

    def test_1_get_name(self):
        print("\nStart get_name test\n")
        """
        Any method that starts with 'test_' will be considered as a test case
        """
        length = len(self.user_id)
        print("user_id length =", length)
        print("user_name length =", len(self.user_name))
        for i in range(6):
            if i < length:
                self.assertEqual(self.user_name[i], self.person.get_name(self.user_id[i]))
            else:
                print("Testing for get_name no user test")
                self.assertEqual("There is no such user", self.person.get_name(i))
        print("\nFinish get_name test\n")


if __name__ == '__main__':
    unittest.main()
