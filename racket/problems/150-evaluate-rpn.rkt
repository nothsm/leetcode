#lang racket

(define (eval-rpn tokens)
  (let loop ([lst tokens] [res '()])
    (match lst
        ['() (car res)]
        [(cons "+" xs) (loop xs (cons (+ (second res) (first res)) (drop res 2)))]
        [(cons "-" xs) (loop xs (cons (- (second res) (first res)) (drop res 2)))]
        [(cons "*" xs) (loop xs (cons (* (second res) (first res)) (drop res 2)))]
        [(cons "/"xs) (loop xs (cons (quotient (second res) (first res)) (drop res 2)))]
        [(cons x xs) (loop xs (cons (string->number x) res))])))