#!/usr/bin/python3

from snippets import (
    read_file,
    calculate_unpaid_loans,
    calculate_paid_loans,
    average_paid_loans,
    arr
)

if __name__ == "__main__":
    try:
      
      
        json_file = read_file()
        assert len(json_file["loans"]) == 15, 
        "Number of loans should equal 15"
        assert (calculate_unpaid_loans(json_file) == 11062), 
        "Total unpaid loans should equal 11062"
        assert (calculate_paid_loans(json_file) == 29493.85304 ), 
        "Total paid loans should equal 29493.85304"
        assert ( average_paid_loans(json_file) == 2681.2593672727276), 
        "Average of paid loans should equal 2681.2593672727276"
        assert arr() == ["baz"], 
         "This should return a single item 'baz'"
        assert arr() == [ "baz"], 
        "When I call the function the second time I should still get a single element in the array"
        
        print("All test passed successfully!! 😀")
        
        
    except (AssertionError, SyntaxError, TypeError) as e:
        print(error, " 😢")
        
    finally