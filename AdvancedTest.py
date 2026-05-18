import unittest
from unittest.mock import Mock # 從內建函式庫匯入 Mock 類別

# 假設這是我們在 app.py 裡要測試的複雜函式
# 它接收使用者資料和一個資料庫連線物件
def process_user_signup(user_data, db_connection):
    """
    處理使用者註冊的商業邏輯。
    - 如果 email 缺失，回傳 400 錯誤。
    - 成功則呼叫資料庫存檔 (副作用)。
    - 最後回傳成功訊息與 201 狀態碼。
    """
    if "email" not in user_data or not user_data["email"]:
        # 這是可直接測試的「回傳值」
        return {"status": "error", "message": "Email is required"}, 400
    
    # 這是我們要用 Mock 測試的「副作用」
    db_connection.save(user_data) 
    
    # 這也是可直接測試的「回傳值」
    return {"status": "success", "user_id": 123}, 201


class TestAdvancedLogic(unittest.TestCase):

    def test_signup_api_response_format(self):
        """
        測試情境1：當輸入有效時，API 回應的格式與狀態碼是否正確
        """
        # 準備：我們不需要一個真的資料庫，所以我們建立一個假的 (Mock)
        mock_db = Mock()
        user = {"email": "test@example.com", "password": "password123"}
        
        # 執行：呼叫我們的函式
        response_body, status_code = process_user_signup(user, mock_db)
        
        # 斷言 (Assert)：檢查多個條件
        self.assertEqual(status_code, 201) # 1. 檢查 HTTP 狀態碼
        self.assertEqual(response_body["status"], "success") # 2. 檢查回傳的 JSON Body 內容
        self.assertIn("user_id", response_body) # 3. 檢查 'user_id' 這個 key 是否存在

    def test_signup_database_interaction(self):
        """
        測試情境2：當呼叫 API 時，它是否有「正確地」呼叫資料庫存檔
        """
        # 準備：再次建立一個假的資料庫物件
        mock_db = Mock()
        user = {"email": "test@example.com", "password": "password123"}
        
        # 執行
        process_user_signup(user, mock_db)
        
        # 斷言 (Assert)：我們不檢查回傳值，而是檢查「行為」
        mock_db.save.assert_called_once_with(user) # 斷言 .save() 方法是否被呼叫過一次，且傳入的參數是 user

    def test_signup_missing_email_error(self):
        """
        測試情境3：當輸入無效時 (缺少 email)，是否回傳正確的錯誤訊息，且「沒有」呼叫資料庫
        """
        mock_db = Mock()
        invalid_user = {"password": "password123"} # 故意不給 email
        
        process_user_signup(invalid_user, mock_db)
        
        # 斷言「資料庫存檔」這個動作「完全沒有」被執行
        mock_db.save.assert_not_called()