#lang racket

(define (anagram s)
    (foldl (lambda (i acc) (hash-update acc (string-ref s i) add1 0))
           (hash)
           (range (string-length s))))

(define (is-anagram s t)
  (equal? (anagram s) (anagram t)))