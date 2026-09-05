Reflection: 

Question 1. 

The test I chose to review over is the follow code: 

    def test_page_contains_heading(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "About Me")

In requirement 6, we were told to ensure we had the text "About Me" containted on our about.html page. The code above will test our code to ensure that there is a text that says About Me and that it is containted in the about.html page. If there wasn't text that says Aboout Me, the test would throw an error. Although this test checks for the "About Me" text, one thing it would not be able to catch is whether or not is it used as a heading or just as a paragraph. So, if the requirement was that my heading needed to be "About Me", but I had my actual heading as "About Jesus", but then I wrote "About Me" in my paragraph, it would not catch this and would pass the test.

Question 2.

Adding a fourth link to the navigation bar would first consist creating a new html page to actually link to. For editing any of our current files, you should just have to edit one file, which would be base.html. The reason for this is because base.html contains all of the repetitive html that we would have to retype if we did not have it. It also contains our href code, which once we add a fourth page, we would have to edit the base.html to include the new href to link to the fourth page. If we didn't have base.html, we would have to edit 3 files in total. We'd have to go into all the other html files and individually add the href link to the fourth page to each one.
