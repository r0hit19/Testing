
# Import
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains

# set path for Chrome web driver
PATH="C://Program Files (x86)//chromedriver.exe"


# Unit Tests
class theSparksFoundationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(PATH)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    # Testing the motto in the navbar "   ...inspiring,innovating,integrating"
    def test_motto_text(self):
        self.driver.get("https://www.thesparksfoundationsingapore.org/")
        logo=self.driver.find_element_by_xpath("//div[@id='home']/div/div/h1/a/span").text
        self.assertEqual("    ...inspiring,innovating,integrating",logo,"Wrong motto text")
        print("Test:1 successful")

    #Testing the title of the homepage
    def test_title(self):
        self.driver.get("https://www.thesparksfoundationsingapore.org/")
        title=self.driver.title
        self.assertEqual("The Sparks Foundation | Home",title,"Wrong title text")
        print("Test:2 successful")

    #Testcase for checking the about page text section " Our Vision Statement "
    def test_about_Vision(self):
        self.driver.get("https://www.thesparksfoundationsingapore.org/")
        self.driver.find_element_by_xpath("//nav[@id='link-effect-3']/ul/li/a").click()
        time.sleep(2)
        act=ActionChains(self.driver)
        act.click(self.driver.find_element_by_link_text("Vision, Mission and Values")).perform()
        time.sleep(2)
        s=self.driver.find_element_by_class_name("tittle-agileits-w3layouts").text
        self.assertEqual("Our Vision Statement",s,"wrong")
        self.driver.back()
        time.sleep(2)
        print("Test:3 successful")

    # Testing Guiding principle page heading
    def test_about_Principles(self):
        self.driver.get("https://www.thesparksfoundationsingapore.org/")
        self.driver.find_element_by_xpath("//nav[@id='link-effect-3']/ul/li/a").click()
        time.sleep(2)
        act=ActionChains(self.driver)
        act.click(self.driver.find_element_by_link_text("Guiding Principles")).perform()
        time.sleep(2)
        s=self.driver.find_element_by_class_name("tittle-agileits-w3layouts").text
        time.sleep(2)
        self.assertEqual("Guiding Principles Based On Our Goals, Mission And Core Values",s,"wrong")
        self.driver.back()
        time.sleep(2)
        print("Test:4 successful")

    # Testing the founder name
    def test_about_Founder_Name(self):
        self.driver.get("https://www.thesparksfoundationsingapore.org/")
        self.driver.find_element_by_xpath("//nav[@id='link-effect-3']/ul/li/a").click()
        time.sleep(2)
        act=ActionChains(self.driver)
        act.click(self.driver.find_element_by_link_text("Executive Team")).perform()
        time.sleep(2)
        s=self.driver.find_element_by_xpath("//div[@class='media-body']/h4").text
        time.sleep(2)
        self.assertEqual("Priyesh Kumar",s,"wrong")
        self.driver.back()
        time.sleep(2)
        print("Test:5 successful")

    # Testing the footer content
    def test_Footer(self):
        self.driver.get("https://www.thesparksfoundationsingapore.org/")
        self.driver.execute_script("arguments[0].scrollIntoView()",self.driver.find_element_by_xpath("//div[@class='copyright-wthree']/p"))
        s=self.driver.find_element_by_xpath("//div[@class='copyright-wthree']/p").text
        self.assertEqual("© 2017 The Sparks Foundation. All Rights Reserved | Design by W3layouts", s, "wrong")
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        print("Test:6 successful")

    # Testing Policies and Code page heading
    def test_Policies(self):
        self.driver.get("https://www.thesparksfoundationsingapore.org/")
        self.driver.find_element_by_xpath("//nav[@id='link-effect-3']/ul/li[2]/a").click()
        time.sleep(2)
        act = ActionChains(self.driver)
        act.click(self.driver.find_element_by_link_text("Personal Data Policy")).perform()
        time.sleep(2)
        s = self.driver.find_element_by_xpath("//div[@class='w3l-blog-list']/h4").text
        time.sleep(2)
        self.assertEqual("Policies and Code", s, "wrong")
        self.driver.back()
        time.sleep(2)
        print("Test:7 successful")


    # Testing code of ethics page heading
    def test_Code_of_Ethics(self):
        self.driver.get("https://www.thesparksfoundationsingapore.org/")
        self.driver.find_element_by_xpath("//nav[@id='link-effect-3']/ul/li[2]/a").click()
        time.sleep(2)
        act = ActionChains(self.driver)
        act.click(self.driver.find_element_by_link_text("Code of Ethics and Conduct")).perform()
        time.sleep(2)
        s = self.driver.find_element_by_xpath("//div[@class='single-middle']/h3/span").text
        time.sleep(2)
        self.assertEqual("Excerpts From The Code Of Ethics And Conduct", s, "wrong")
        self.driver.back()
        time.sleep(2)
        print("Test:8 successful")


    # testing display of iframe "embedded youtube"
    def test_homepage_display(self):
        self.driver.get("https://www.thesparksfoundationsingapore.org/")
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView()",self.driver.find_element_by_tag_name("iframe"))
        if self.driver.find_element_by_tag_name("iframe").is_displayed():
            self.driver.switch_to.frame("youtube-video")
            self.driver.find_element_by_class_name("ytp-large-play-button").click()
            time.sleep(6)
            print("Test:9 successful")
            assert True
        else:
            assert False

    # Testing Learn more button
    def test_learnMore_buttons(self):
        self.driver.get("https://www.thesparksfoundationsingapore.org/")
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView()", self.driver.find_element_by_xpath("//div[@class='about-w3layouts']/div/div[2]/a"))
        if self.driver.find_element_by_xpath("//div[@class='about-w3layouts']/div/div[2]/a").is_enabled():
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class='about-w3layouts']/div/div[2]/a").click()
            time.sleep(5)
            self.driver.back()
            print("Test:10 successful")
            assert True
        else:
            assert False

    # Testing Know more button
    def test_knowMore_buttons(self):
        self.driver.get("https://www.thesparksfoundationsingapore.org/")
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView()", self.driver.find_element_by_class_name("container"))
        # //div[@class='services-info']/a
        if self.driver.find_element_by_xpath("//div[@class='services-info']/a").is_enabled():
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class='services-info']/a").click()
            time.sleep(5)
            self.driver.back()
            print("Test:11 successful")
            assert True
        else:
            assert False

    # Tesing the totop hover button
    def test_toTopHover(self):
        self.driver.get("https://www.thesparksfoundationsingapore.org/")
        self.driver.execute_script("arguments[0].scrollIntoView()",
                                   self.driver.find_element_by_xpath("//div[@class='copyright-wthree']/p"))
        time.sleep(2)
        if self.driver.find_element_by_id("toTop").is_displayed() and self.driver.find_element_by_id("toTop").is_enabled():
            self.driver.find_element_by_id("toTop").click()
            time.sleep(3)
            print("Test:12 successful")
            assert True

        else:
            assert False
    # Testing the Navbar
    def test_navbar_presence(self):
        self.driver.get("https://www.thesparksfoundationsingapore.org/")
        if self.driver.find_element_by_tag_name("nav").is_enabled() and self.driver.find_element_by_tag_name("nav").is_enabled():
            print("Test:13 successful")
            assert True
        else:
            assert False

    #Testing the Link dropdown
    def test_Links(self):
        self.driver.get("https://www.thesparksfoundationsingapore.org/")
        self.driver.find_element_by_xpath("//nav[@id='link-effect-3']/ul/li[4]/a").click()
        time.sleep(2)
        act = ActionChains(self.driver)
        act.click(self.driver.find_element_by_link_text("AI in Education")).perform()
        time.sleep(2)
        s = self.driver.find_element_by_class_name("inner-tittle-w3layouts").text
        self.assertEqual("AI In Education", s, "wrong")
        self.driver.back()
        self.driver.find_element_by_xpath("//nav[@id='link-effect-3']/ul/li[4]/a").click()
        time.sleep(2)
        act = ActionChains(self.driver)
        act.click(self.driver.find_element_by_link_text("Salient Features")).perform()
        time.sleep(2)
        s = self.driver.find_element_by_class_name("inner-tittle-w3layouts").text
        self.assertEqual("LINKS Salient Features", s, "wrong")
        self.driver.back()
        self.driver.find_element_by_xpath("//nav[@id='link-effect-3']/ul/li[4]/a").click()
        time.sleep(2)
        act = ActionChains(self.driver)
        act.click(self.driver.find_element_by_link_text("Software & App")).perform()
        time.sleep(2)
        s = self.driver.find_element_by_class_name("inner-tittle-w3layouts").text
        self.assertEqual("LINKS Suite", s, "wrong")
        self.driver.back()

        time.sleep(2)
        print("Test:14 successful")

    # Testing the media icons
    def test_media_icons(self):
        time.sleep(6)
        self.driver.get("https://www.thesparksfoundationsingapore.org/")
        self.driver.execute_script("arguments[0].scrollIntoView()",self.driver.find_element_by_xpath("//div[@class='top-header-agile-right']"))

        icon1=self.driver.find_element_by_xpath("//div[@class='top-header-agile-right']/ul/li[1]/a")
        icon2 = self.driver.find_element_by_xpath("//div[@class='top-header-agile-right']/ul/li[2]/a")
        icon3 = self.driver.find_element_by_xpath("//div[@class='top-header-agile-right']/ul/li[3]/a")
        icon4 = self.driver.find_element_by_xpath("//div[@class='top-header-agile-right']/ul/li[4]/a")
        icon5 = self.driver.find_element_by_xpath("//div[@class='top-header-agile-right']/ul/li[5]/a")
        icon6 = self.driver.find_element_by_xpath("//div[@class='top-header-agile-right']/ul/li[6]/a")
        if ((icon1.is_displayed() and icon1.is_enabled()) and (icon2.is_displayed() and icon2.is_enabled()) and
            (icon3.is_displayed() and icon3.is_enabled()) and (icon4.is_displayed() and icon4.is_enabled()) and
            (icon5.is_displayed() and icon5.is_enabled()) and (icon6.is_displayed() and icon6.is_enabled())):
            print("Test:15 successful")
            assert True
        else:
            assert False
        time.sleep(5)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed')

if __name__=='__main__':
    unittest.main()
