from Base.Base import Base
import Page
class Sign_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_exit_account(self):
        # 点击已存在账号
        self.click_element(Page.exits_account_id)