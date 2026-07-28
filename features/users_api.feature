Feature: Users API
  As an API consumer
  I want to retrieve users
  So that I can integrate with the service

  Scenario: Fetch the full list of users
    When I request the list of users
    Then the response status should be 200
    And the response should contain 10 users

  Scenario Outline: Fetch a single user by id
    When I request user "<user_id>"
    Then the response status should be 200
    And the returned user id should be "<user_id>"

    Examples:
      | user_id |
      | 1       |
      | 5       |
      | 10      |
