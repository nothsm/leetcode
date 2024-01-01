#lang racket

(define (majority-element nums)
    (let loop ([lst nums] [res -1] [ct 0])
        (match lst
            ['() res]
            [(cons x xs) (cond [(zero? ct) (loop xs x (add1 ct))]
                               [else (loop xs res ((if (= x res) add1 sub1) ct))])])))