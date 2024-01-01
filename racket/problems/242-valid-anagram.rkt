#lang racket

#|
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
 
Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
|#

(define (anagram s)
    (foldl (lambda (i acc) (hash-update acc (string-ref s i) add1 0))
           (hash)
           (range (string-length s))))

(define (is-anagram s t)
  (equal? (anagram s) (anagram t)))