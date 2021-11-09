from unittest import mock
from unittest import TestCase, main
from HW4 import (
    user_pin_string,
    pin_loop,
    withdrawal_amount_string,
    subtraction_account
)

# @mockpatch(package.module.function/classname)

class Test_user_pin_string(TestCase):
    @mock.patch("HW4.HW4.user_pin_string")
    def test_mock_user_input(self, mock_user_input):
        mock_user_input.return_value = 'hi'
        self.assertEqual(user_pin_string('hi'), ValueError)



if __name__ == "__main__":
    main()