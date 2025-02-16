
### Assignment on String

Task 1: K-Ostad

Two strings of lowercase alphabets are called K-Ostad if they can be transformed into each other using at most K operations . The allowed operations are:

✅ Insert a character 
✅ Delete a character 
✅ Change a character

✅ Swap any two characters

If one string can be converted into the other within K modifications , they are K-Ostad . Otherwise, they are not.

Examples :  

Input:  str1 = "anagram" , str2 = "grammar" , k = 3 
Output:  Yes 
Explanation: Since we are allowed up to 3 modifications, we can transform 'grammar' into 'anagram' by changing 'r' → 'n' and 'm' → 'a'. Thus, the two strings are K-Ostad.


Input:  str1 = "ostad", str2 = "boss", k = 1 
Output:  No 
Explanation: We can do operation on only 1 
character but there is a need of more than 1 operation. 


Task 2: Encrypt-Decrypt

Given a string S consisting of N lowercase English letters , your task is to encrypt the string using the following steps:

Replace every substring of consecutive identical characters with a concatenation of the character and its count .

Reverse the transformed string to get the final encrypted result.

Decrypt the string and show that the decrypted string is similar to the input.  

Examples:

Input: S = “aaaaaaaaaaaa” 
Output: “11a” 
Explanation:

First convert the given string to “a11” ie write, character along with its frequency. 

Then, finally reverse the string ie “11a”.

Input: S = “ostad” 
Output: “ 1d1a1t1s1o”
