Feature: ecFeed login

Scenario: Basic test of ecFeed
  Given Chrome browser is launched
  When ecFeed homepage is opened
  And button is Accepted
  And Login button is clicked
  And username "ecFeed.automation@gmail.com" and password "#password123!" are entered
  And Submit button is clicked
  And Accept cookies button

  Then Click on My Teams button
  Then Click on My Projects button
  Then Click create new project
  Then Enter project name "TestProject"
  Then Click create


  Then Click on User Menu button
  Then Click on Settings button
  Then Click again on User Menu button
  Then Log out
  Then Find my projects

