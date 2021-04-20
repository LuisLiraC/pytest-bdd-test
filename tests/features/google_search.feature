@web @google
  Feature: Google Web Browsing
    As a web surfer,
    I want to find information online,
    So I can learn new things and tasks done.

    Background:
      Given the Google Home Page is displayed

    Scenario Outline: Basic Google Search
      When the user searches for "<phrase>"
      Then results are shown for "<phrase>"
      Then print "<amount>" results

      Examples: Phrases
        |phrase    |amount|
        |automation|3     |