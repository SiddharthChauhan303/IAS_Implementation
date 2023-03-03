For the following IAS Architecture Implementation in Python language:
(main file:assignment1.py)
(result file:result.txt)


------------------------------------------------------------
For Volume:
1 (choice) (user input)
l b h  (user input)
(enter the following assembly code to see the output)

LOAD MQ,M(X) 500 MUL M(X) 501
LOAD MQ 0 STOR M(X) 503
LOAD MQ,M(X) 502 MUL M(X) 503
LOAD MQ 0 STOR M(X) 503
HALT
-------------------------------------------------------------
-------------------------------------------------------------
For Surface Area:
2 (choice)(user input))
l b h (user input)
(enter the following assembly code to see the output)

LOAD MQ,M(X) 500 MUL M(X) 501
LOAD MQ 0 STOR M(X) 503
LOAD MQ,M(X) 501 MUL M(X) 502
LOAD MQ 0 STOR M(X) 504
LOAD MQ,M(X) 502 MUL M(X) 500
LOAD MQ 0 STOR M(X) 505
LOAD M(X) 503 ADD M(X) 504
STOR M(X) 506
LOAD M(X) 506 ADD M(X) 505
STOR M(X) 506
LOAD MQ,M(X) 506 MUL M(X) 900
LOAD MQ 0 STOR M(X) 506
HALT
---------------------------------------------------------------
---------------------------------------------------------------
For power(a,b):
3 (choice)(user input)
a b (user input)
(enter the following assembly code to see the output)

LOAD MQ,M(X) 501 MUL M(X) 500
LOAD MQ 0 STOR M(X) 507
LOAD M(X) 507 STOR M(X) 501
JUMP M(X,0:20) 0
HALT
---------------------------------------------------------------
What JUMP instruction does, 
JUMP M(X,0:19) 0
jumps back the execution to the zeroth line of assembly code 
So fucntions which are recursive in nature can be performed using
JUMP instruction in assembly language.
---------------------------------------------------------------
END OF README.txt file
