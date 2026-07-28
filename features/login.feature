Feature: SauceDemo login
  As a shopper
  I want to log in to the store
  So that I can browse and buy products

  Background:
    Given the login page is open

  Scenario: Successful login lands on the products page
    When I log in as "standard_user" with password "secret_sauce"
    Then I should see the products page

  Scenario: Locked-out user is rejected
    When I log in as "locked_out_user" with password "secret_sauce"
    Then I should see an error containing "locked out"
