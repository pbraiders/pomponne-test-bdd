@admin @usermgnt
Feature: Password update, success cases
    SMART: ✔️

    Scenario: Update a password
        Given I am on an activated user account page
        When I change the password
        Then I can sign in to this account using the new password
