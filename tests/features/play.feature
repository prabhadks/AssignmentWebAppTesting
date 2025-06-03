Feature: Play Streamer verification

  Scenario: Verify that the Streamer is loaded
    Given User go to Twitch
    Then Twitch home page is displayed
    And User clicks on the Search icon from home page
    When Enters "StarCraft II" in Search box
    And User scrolls down 2 times on directory page
    And User selects a streamer
    Then User is navigated to the Streamer page
    And User waits till the streamer is loaded