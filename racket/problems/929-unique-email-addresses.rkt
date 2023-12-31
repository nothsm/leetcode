#lang racket

(define (dot? char)
    (equal? char #\.))

(define (parse email)
    (let* ([lst (string-split email "@")]
           [loc (car (string-split (first lst) "+"))]
           [no-dots (list->string (filter-not dot? (string->list loc)))]
           [dom (second lst)]) 
        (string-append no-dots "@" dom)))

(define (num-unique-emails emails)
  (length (remove-duplicates (map parse emails))))