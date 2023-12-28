#lang racket

(define (most-common ht)
    (car
    (for/fold ([max-freq (cons #\x -1)])
              ([(k v) ht])
        (argmax cdr (list max-freq (cons k v))))))


(most-common (hash #\a 3 #\b 2 #\c 300))