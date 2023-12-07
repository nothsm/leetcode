#lang racket

(define (char-alphanum? c)
    (or (char-numeric? c) (char-alphabetic? c)))

(define (is-palindrome s)
    (let* ([str (filter char-alphanum? (string->list (string-downcase s)))])
    (equal? str (reverse str))))