#lang racket

(define (pivot-index nums)
  (let loop ([l nums] [i 0] [sl 0] [sr (apply + (cdr nums))])
    (match l
        ['() -1]
        [(list x) #:when (not (zero? sl)) -1]
        [_ #:when (= sl sr) i]
        [(cons x xs) (loop xs (add1 i) (+ sl x) (- sr (car xs)))])))