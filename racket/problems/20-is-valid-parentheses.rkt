#lang racket

(define (is-valid s)
    (let loop ([lst (string->list s)] [ps '()])
        (match lst
            ['() (empty? ps)]
            [(cons #\( ss) (loop ss (cons #\( ps))]
            [(cons #\{ ss) (loop ss (cons #\{ ps))]
            [(cons #\[ ss) (loop ss (cons #\[ ps))]
            [(cons #\) ss) (and (not (empty? ps)) (equal? (car ps) #\() (loop ss (cdr ps)))]
            [(cons #\} ss) (and (not (empty? ps)) (equal? (car ps) #\{) (loop ss (cdr ps)))]
            [(cons #\] ss) (and (not (empty? ps)) (equal? (car ps) #\[) (loop ss (cdr ps)))])))