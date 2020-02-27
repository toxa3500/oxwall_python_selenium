Feature: Post feature
  Description: User can add a post with photo and without photo on Dashboard page
  or on Main page.
  The post appears on the page in few seconds after posting without page reloading.
  User can delete poat added by him. Only admin can delete every news.
  Scenario Outline: Create text post (without photos)
    Given initial amount of post in Oxwall database
    Given I as a logged user
    When I add a new post with <text> in Dashboard page
    Then a new post block appears before old table of posts
    Then this post block has this <text> and author as this user and time "within 1 minute"
    Examples:
    |  text               |
    | !@#%^&<a *%^*{}))_+ |
    | New 1234098765!     |
    | Привіт!             |
    Scenario: Delete post
      Description: TODO
      Given dgfd
      When sdg
      Then gfh