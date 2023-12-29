#lang racket

(define (index-of s c)
    (or 
    (ormap (lambda (x i) (if (equal? x c) i #f))
           (string->list s)
           (range (string-length s))) 
    -1))

(index-of "abc" #\d)