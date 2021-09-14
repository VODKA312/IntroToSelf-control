message_1 = """
Congratulations! 

You found the first message. Can you find the second? 

You might want to change the variable name from 
secret_messages.message_1 to something else."""

message_2 = """
Nice work! You found the second message!

Now, take a look at the toolbar at the top of the notebook. Insert 
a new cell and print message_3 by doing the following:

1. Select Insert > Insert Cell Below
2. Click the new cell to get a cursor. Type the following:

print(secret_messages.message_3) 

3. Press Ctrl + Enter to run
"""

message_3 = """
Great! There is still one more message to find but it's not named 
what you think. Luckily, you can use autocomplete to discover
what it's called. To do that:

1. Insert a cell below this one.
2. Type the following into the cell (including the . )

print(secret_messages.)

3. Then, with your cursor to the right of the . press the Tab key on your 
   keyboard. You should see all of the variables contained in 
   the secret_messages file.
   
4. Use the arrow keys to navigate down to the last message and 
   press enter. If you then run the cell you should see the last
   message.
"""

final_message = """
                                               ____
                                              |    |                         
                                              |  O |                          
                                              |    |                         
                                  ..---:::::::-----------. ::::;;.
                               .'""'""'                  ;;   \  ":.
                            .''                          ;     \   "\__.
                          .'                            ;;      ;   \\";
                        .'                              ;   _____;   \\/
                      .'                               :; ;"     \ ___:'.
                    .'--...........................    : =   ____:"    \ \\
               ..-""                               "'"'  o"'"     ;     ; :
          .--""  .----- ..----...    _.-    --.  ..-"     ;       ;     ; ;
       .""_-     "--""-----'""    _-"        .-""         ;        ;    .-.
    .'  .'                      ."         ."              ;       ;   /. |
   /-./'                      ."          /           _..  ;       ;   ;;;|
  :  ;-.______               /       _________==.    /_  \ ;       ;   ;;;;
  ;  / |      ""'""'""'"".---.""'""'"          :    /" ". |;       ; _; ;;;
 /"-/  |                /   /                  /   /     ;|;      ;-" | ;';
:-  :   "'"----______  /   /              ____.   .  ."'. ;;   .-"..T"   .
'. "  ___            "":   '""'""'""'""'""    .   ; ;    ;; ;." ."   '--"
 ",   __ "'"  ""---... :- - - - - - - - - ' '  ; ;  ;    ;;"  ."
  /. ;  "'"---___                             ;  ; ;     ;|.""
 :  ":           "'"----.    .-------.       ;   ; ;     ;:
  \  '--__               \   \        \     /    | ;     ;;
   '-..   ""'"---___      :   .______..\ __/..-""|  ;   ; ;
       ""--..       "'"--"        m l s         .   ". . ;
             ""------...                  ..--""      " :
                        ""'""'""'""'""'""'    \        /
                                               "------"
                                               
Good work, you've found the final message! 

But you can add more! Click the "Jupyter" logo in the 
top-left of the notebook and then navigate to secret_messages.py

(or if you prefer, explore some of the other notebooks we've 
created for you to explore).

You can add your own variables and then navigate back to this
notebook to try printing them.
"""