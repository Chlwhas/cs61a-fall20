(define (caar x) (car (car x)))

(define (cadr x) (car (cdr x)))

(define (cdar x) (cdr (car x)))

(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement
(define (zip pairs) 'replace-this-line)

; ; Problem 15
; ; Returns a list of two-element lists
(define (enumerate s)
  (define (inner lst index res)
    (cond 
      ((null? lst)
       res
      )
      (else
       (inner (cdr lst)
              (+ index 1)
              (append res (list (list index (car lst))))
       )
      )
    )
  )
  (inner s 0 '())
)

; ; Problem 16
; ; Merge two lists LIST1 and LIST2 according to COMP and return
; ; the merged lists.
(define (merge comp list1 list2)
  (cond 
    ((null? list1)
     list2
    )
    ((null? list2)
     list1
    )
    ((comp (car list1) (car list2))
     (cons (car list1) (merge comp (cdr list1) list2))
    )
    (else
     (cons (car list2) (merge comp list1 (cdr list2)))
    )
  )
)

(merge < '(1 5 7 9) '(4 8 10))

; expect (1 4 5 7 8 9 10)
(merge > '(9 7 5 1) '(10 8 4 3))

; expect (10 9 8 7 5 4 3 1)
; ; Problem 17
(define (nondecreaselist lst)
  (if (null? lst)
      '()
      (helper (cdr lst) (list (car lst)) '())
  )
)

(define (helper remaining current result)
  (cond 
    ((and (null? remaining) (null? current))
     result
    )
    ((or (and (null? (cdr remaining)) (null? current))
         (< (cadr remaining) (car remaining))
     )
     (helper (cdr remaining)
             '()
             (append result
                     (list (append current (list (car remaining))))
             )
     )
    )
    (else
     (helper (cdr remaining)
             (append current (list (car remaining)))
             result
     )
    )
  )
)

; ; Problem EC
; ; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr)))
)

(define lambda? (check-special 'lambda))

(define define? (check-special 'define))

(define quoted? (check-special 'quote))

(define let? (check-special 'let))

; ; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond 
    ((atom? expr)
     expr
    )
    ((quoted? expr)
     expr
    )
    ((or (lambda? expr) (define? expr))
     (let ((form (car expr))
           (params (cadr expr))
           (body (cddr expr))
          )
       (cons form (cons params (map let-to-lambda body)))
     )
    )
    ((let? expr)
     (let ((values (cadr expr))
           (body (cddr expr))
          )
       (define symbols (map car values))
       (define args
               (map (lambda (v) (let-to-lambda (cadr v))) values)
       )
       (append (list (cons 'lambda
                           (cons symbols (map let-to-lambda body))
                     )
               )
               args
       )
     )
    )
    (else
     (map let-to-lambda expr)
    )
  )
)
