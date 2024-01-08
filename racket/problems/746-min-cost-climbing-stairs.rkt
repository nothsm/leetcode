#lang racket

(define (min-cost-climbing-stairs cost)
    (let dp ([l (reverse cost)] [fst 0] [snd 0])
      (match l
        ['() (min fst snd)]
        [(cons x xs) (dp xs (min (+ x fst) (+ x snd)) fst)])))