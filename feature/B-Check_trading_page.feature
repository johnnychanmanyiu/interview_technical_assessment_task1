Feature: Check CRO/USDC trading page

    Scenario: B01 - Check CRO/USDC trading page layout
        Given I am on CRO/USDC trading page

        Then I should have trading view
        And I should have order list box
        And I should have trading history
        And I should have trading box

    Scenario: B02 - Reach login page
        Given I am on CRO/USDC trading page

        When I click login on trading box

        Then I should be on login page

    Scenario: B03 - Order history
        Given I am on CRO/USDC trading page
        And I login with <email> and <password>

        When I click order history

        Then I should have order history

        Examples:
            | email         | password |
            | aaa@gmail.com | Test1234 |

    Scenario: B04 - Trading box
        Given I am on CRO/USDC trading page

        When I input <price> and <amount>

        Then I should have <total>

        Examples:
            | price  | amount | total     |
            | 0.1600 | 100    | 16.000000 |