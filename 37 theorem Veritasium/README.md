# The 37 theory proof
Inspired by one of the favorite science channels of All time
In the video the mathematician stated something interesting about the number 37 and its multiples.
For any multiple of 37 reverse it and put a 0 between all of its digits and the new number will be a multiple for 37.
Example : 37→703,703=19∗3737→703,703=19∗37.
I found this very interesting to prove, so I went ahead to prove it using excel (for pseudo code) and then by using Python.

Approach,
-	A function to create multiples of 37.
    -	Single for loop can do the trick
-	A function that inverts (palindrome) the output from first function.
    -	~Converts the number to string.~
    -	~Reverse the string.~
    - ~Convert string back to int.~
    -	String idea was revoked and the input was reversed as int instead.
    -	This was fairly easy as solution to Palindrome problem was already coded previously.
- A function to add zeroes between the numbers.
    -	Converts the inverted int into string and adds ‘0’ (as a string) between the numbers.
-	Finally, to check divisibility of this new number.
    -	Call the Reverse int function N times where 0 < N < 10^n for every multiple of 37.
