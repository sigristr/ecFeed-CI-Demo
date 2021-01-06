Feature: ecFeed login

Background: Common steps
  Given Chrome browser is launched
  When ecFeed homepage is opened
  And button is Accepted
  And Login button is clicked
  And username "sigrid.strand@testify.no" and password "Persimon123!" are entered
  And Submit button is clicked
  And Accept cookies button


  Scenario: Navigate to My Teams
    Then Click on My Teams button

  Scenario: Navigate to My Projects
    Then Click on My Projects button

  Scenario: Navigate to Settings
    And Click on User Menu button
    Then Click on Settings button

  Scenario: Create new project
    And Click create new project
    And Enter project name "TestProject"
    Then Click create

  Scenario: Log out user and verify that My Projects is no longer available (last call will fail)
    And Click again on User Menu button
    And Log out
    Then Find my projects

