#lang racket

(define (majority-element nums)
    (let loop ([lst nums] [res -1] [ct 0])
        (match lst
            ['() res]
            [(cons x xs) #:when (zero? ct) (loop xs x (add1 ct))]
            [(cons x xs) #:when (= x res) (loop xs res (add1 ct))]
            [(cons x xs) (loop xs res (sub1 ct))])))