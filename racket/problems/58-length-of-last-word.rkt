#lang racket

(define (length-of-last-word s)
    (string-length (last (string-split s))))