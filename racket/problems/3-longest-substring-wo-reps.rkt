#lang racket

(define (length-of-longest-substring s)
    (define (go lst window window-st longest)
        (match lst
            ['() longest]
            [(cons c cs) 
                (cond [(set-member? window-st c) 
                         (let ([updated (cons c 
                                              (takef window 
                                                     (lambda (x) 
                                                        (not (equal? x c)))))])
                            (go cs
                                updated
                                (list->set updated)
                                longest))]
                      [else (go cs 
                                (cons c window) 
                                (set-add window-st c) 
                                (max longest 
                                     (add1 (length window))))])]))
    (go (string->list s) '() (set) 0))