#lang racket

(define (str-str haystack needle)
    (let loop ([left 0] [right (string-length needle)])
        (if (> right (string-length haystack)) -1
        (match (substring haystack left right)
            [(? (lambda (sub) (equal? sub needle))) left]
            [_ (loop (add1 left) (add1 right))]))))