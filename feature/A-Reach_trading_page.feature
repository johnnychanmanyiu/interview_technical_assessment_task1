Feature: Reach CRO/USDC trading page

    Scenario: A01 - Go to homepage
        Given I go to homepage

        Then I should be on homepage

    Scenario: A02 - Go to CRO/USDC trading page
        Given I am on homepage

        When I click CRO Markets
        And I click CRO/USDC

        Then I should be on CRO/USDC trading page