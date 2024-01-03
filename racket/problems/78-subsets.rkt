#lang racket

(define (subsets nums)
  (let loop ([l nums] [so-far '()] [acc '()])
    (match l
        ['() (cons so-far acc)]
        [(cons x xs) (append (loop xs (cons x so-far) acc)
                             (loop xs so-far acc))])))