#lang racket

(define (climb-stairs n)
    (let loop ([i n] [fst 1] [snd 0])
      (cond
        [(= i 0) fst]
        [else (loop (sub1 i) (+ fst snd) fst)])))