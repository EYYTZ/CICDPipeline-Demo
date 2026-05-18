import unittest
from app import add_numbers, multiply_numbers

class TestEdgeCases(unittest.TestCase):

    def test_add_strings_error(self):
        # 【故意失敗的特例】：假設前端不小心傳來字串 "1" 和 "2"
        # 在 Python 中 "1" + "2" 會變成字串 "12"
        # 但我們在這裡刻意斷言它應該等於整數 3，這樣就能觀察到錯誤報告的樣子
        self.assertEqual(add_numbers(1, 2), 3, "自訂錯誤警告：發現字串相加，結果不如預期！")

    def test_multiply_by_zero(self):
        # 【成功的邊界測試】：測試極端情況，例如乘以 0
        self.assertEqual(multiply_numbers(999, 0), 0)

if __name__ == '__main__':
    unittest.main()