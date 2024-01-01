#lang racket

(define (anagram s)
    (foldl (lambda (i acc) (hash-update acc (string-ref s i) add1 0))
           (hash)
           (range (string-length s))))

(define (group-anagrams strs)
  (group-by anagram strs))
