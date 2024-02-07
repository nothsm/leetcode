#lang racket

; Definition for singly-linked list:
#|

; val : integer?
; next : (or/c list-node? #f)
(struct list-node
  (val next) #:mutable #:transparent)

; constructor
(define (make-list-node [val 0])
  (list-node val #f))

|#

(define (merge-two-lists list1 list2)
  (cond
    [(equal? list1 #f) list2]
    [(equal? list2 #f) list1]
    [(< (list-node-val list1) (list-node-val list2)) 
     (set-list-node-next! list1 (merge-two-lists (list-node-next list1) list2))
     list1]
    [else 
     (set-list-node-next! list2 (merge-two-lists list1 (list-node-next list2)))
     list2])
  )