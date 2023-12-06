#lang racket

(define (is-valid s)
    (define (valid? open close) ; returns true if open and close form "()" or "{}" or "[]"
        (or (and (equal? open #\()  (equal? close #\))) 
            (and (equal? open #\{)  (equal? close #\})) 
            (and (equal? open #\[)  (equal? close #\]))))
    (define (helper parens unmatched all-valid?)
        (match parens
            ['() (and all-valid? (empty? unmatched))] ; if unmatched is not empty, then we have unmatched parentheses
            [(cons p ps) 
                (match p 
                    [(or #\( #\{ #\[) (helper ps (cons p unmatched) all-valid?)] ; if p is open paren, then we have one more unmatched paren
                    [(or #\) #\} #\]) ; if p is closing paren: 
                        (match unmatched
                            ['() #f] ; if there's no unmatched parentheses, s is not valid
                            [(cons s ss) (helper ps ss (and all-valid? (valid? s p)))])])])) ; otherwise check if the next unmatched paren matches s
    (helper (string->list s) '() #t))
