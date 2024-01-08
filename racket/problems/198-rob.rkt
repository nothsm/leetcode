#lang racket

(define (rob nums)
  (define (brute l a)
    (match l
      ['() a]
      [(cons x '()) (max (brute '() (+ a x)) (brute '() a))]
      [(cons x xs) (max (brute (cdr xs) (+ a x)) (brute xs a))]))

  (let dp ([l (reverse nums)] [fst 0] [snd 0])
    (match l
      ['() (max fst snd)]
      [(cons x xs) (dp xs (max (+ x snd) fst) fst)])))