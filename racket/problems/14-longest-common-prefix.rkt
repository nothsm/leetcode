#lang racket

(define (longest-common-prefix strs)
  (define (go lst pre)
    (match lst
        ['() (list->string pre)]
        [(cons s ss) (go ss (take-common-prefix (string->list s) pre))]))
  (go (cdr strs) (string->list (car strs))))