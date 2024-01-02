#lang racket

(define (remove-stars s)
    (let loop ([lst (string->list s)] [res '()])
        (match lst
            ['() (list->string (reverse res))]
            [(cons #\* cs) (loop cs (cdr res))]
            [(cons c cs) (loop cs (cons c res))])))