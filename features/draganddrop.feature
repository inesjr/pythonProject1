Feature: drag and drop
  Scenario: drag and drop success
    Given the user is on the home page
    When he drag and drop the grey box in the blue box
    Then he sees a message "Dropped!"