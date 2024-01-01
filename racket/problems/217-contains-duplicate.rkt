#lang racket

(define (contains-duplicate nums)
  (not (= (length nums) (set-count (list->set nums)))))