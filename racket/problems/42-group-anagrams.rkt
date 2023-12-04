#lang racket

(define (anagram str)
    (foldl 
        (lambda (char ht) (hash-update ht char add1 0))
        #hash()
        (string->list str)))

(define (group-anagrams strs)
  (group-by anagram strs))
