# module - a file containing python code. May contain functions, classes, etc.
#        - used with modular programming, which is to separate a program into parts

# types of import = import modulemessages
#                 = import modulemessages as msg
#                 = from modulemessages import hello,bye
#                 = from modulemessages import hello,bye

#help("modules")

import modulemessages

modulemessages.hello()
modulemessages.bye()

print()

import modulemessages as msg

msg.hello()
msg.bye()

print()

from modulemessages import hello,bye

hello()
bye()

print()

from modulemessages import * #not used for large programs as can run into names conflict

hello()
bye()