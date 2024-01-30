#lang racket

; Definition for singly-linked list:
; val : integer?
; next : (or/c list-node? #f)
(struct list-node
  (val next) #:mutable #:transparent)

; constructor
(define (make-list-node [val 0])
  (list-node val #f))

(define (reverse-list head)
  (define (rev ll prev)
    (match ll
      [#f prev]
      [(list-node val next) (rev next (list-node val prev))]))
  (rev head #f))