#include <stdio.h>
int main() {
    int number;

    printf("Enter an integer: ");
    scanf("%d", &number);

    // true if number is less than 0
    if (number < 0) {
        printf("You entered %d.\n", number);
    }

    printf("The if statement is easy.");

    return 0;
}

#include <stdio.h>

int main()
{
    /* Variable declaration to store age */
    int age;

    /* Input age from user */
    printf("Enter your age: ");
    scanf("%d", &age);

    /* Use relational operator to check age */
    if(age >= 18)
    {
        /* If age is greater than or equal 18 years */
        printf("You are eligible to vote in India.");
    }

    return 0;
}
