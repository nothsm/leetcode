#lang racket

(define (array-sign nums)
  (sgn (apply * nums)))