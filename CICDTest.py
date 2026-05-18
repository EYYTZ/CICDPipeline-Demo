import unittest
# 從 app.py 匯入我們要測試的函式
from app import add_numbers, multiply_numbers

# ==========================================
# 單元測試區：CI 階段將會自動執行這個區塊
# ==========================================
class TestCICDPipeline(unittest.TestCase):

    def test_add_numbers(self):
        # 測試 2 + 3 是否正確等於 5
        # 如果未來有人不小心改壞了邏輯，這裡就會報錯，CI 也會隨之失敗並阻擋佈署
        self.assertEqual(add_numbers(2, 3), 5)

    def test_multiply_numbers(self):
        # 測試 4 * 5 是否正確等於 20
        self.assertEqual(multiply_numbers(4, 5), 20)

if __name__ == '__main__':
    # 當直接執行此腳本時，啟動單元測試
    unittest.main()
