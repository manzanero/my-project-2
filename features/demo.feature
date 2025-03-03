
Feature: showing off behave

  Scenario Outline: sale Mario cuando la página es estática
    Given navego a "dynamic_content"
    When clico en "click here"
    Then <sale> Mario

    @regression
    Examples:
      | sale    |
      | sale    |

    Examples:
      | sale    |
      | no sale |