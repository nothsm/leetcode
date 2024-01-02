#lang racket

(define (cal-points operations)
  (let loop ([lst operations] [record '()])
    (match lst
        ['() (apply + record)]
        [(cons "+" xs) (loop xs (cons (+ (first record) (second record)) record))]
        [(cons "D" xs) (loop xs (cons (* 2 (car record)) record))]
        [(cons "C" xs) (loop xs (cdr record))]
        [(cons x xs) (loop xs (cons (string->number x) record))])))