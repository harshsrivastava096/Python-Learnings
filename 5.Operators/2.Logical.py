# ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖1️⃣>AND➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
# ‼️Basic Condition
# Operand 1 = True
# O/p = Operand 2
# Operand 1 = False
# O/p = Operand 1
# ‼️

# 🟡Basic

# >>> a = True and True
# >>> print(a)
# >>> True

# >>> b = True and False
# >>> print(b)
# >>> False

# >>> c = False and True
# >>> print(c)
# >>> False

# >>> d = False and False
# >>> print(d)
# >>> False

# >>> e = True and True and False
# >>> print(e)
# >>> False

# >>> f = True and True and True
# >>> print(f)
# >>> True

# >>> g = False and True and True
# >>> print(g)
# >>> False

# >>> h = True and False and False
# >>> print(h)
# >>> False

# >>> i = True and True and False and True
# >>> print(i)
# >>> False

# >>> j = False and False
# >>> print(j)
# >>> False


# # 🟡Complex

# >>> a = (1+0j) and (0+1j)
# >>> print(a)
# >>> (0+1j)

# >>> b = (0+0j) and (2+3j)
# >>> print(b)
# >>> 0j

# >>> c = (2+2j) and (3+3j)
# >>> print(c)
# >>> (3+3j)

# >>> d = (0+1j) and (0+0j)
# >>> print(d)
# >>> 0j

# >>> e = (1+1j) and (2+2j) and (0+1j)
# >>> print(e)
# >>> (0+1j)

# >>> f = (0+0j) and (1+2j) and (3+0j)
# >>> print(f)
# >>> 0j

# >>> g = (1+0j) and (1+0j)
# >>> print(g)
# >>> (1+0j)

# >>> h = (5+5j) and (0+0j)
# >>> print(h)
# >>> 0j

# >>> i = (0+0j) and (0+0j)
# >>> print(i)
# >>> 0j

# >>> j = (1+2j) and (3+4j)
# >>> print(j)
# >>> (3+4j)

# # 🟡String

# >>> a = "Hello" and "World"
# >>> print(a)
# >>> World

# >>> b = "" and "Python"
# >>> print(b)
# >>> 

# >>> c = "Hi" and ""
# >>> print(c)
# >>> 

# >>> d = "" and ""
# >>> print(d)
# >>> 

# >>> e = "A" and "B" and "C"
# >>> print(e)
# >>> C

# >>> f = "" and "X" and "Y"
# >>> print(f)
# >>> 

# >>> g = "X" and "" and "Y"
# >>> print(g)
# >>> 

# >>> h = "Hi" and "Python" and ""
# >>> print(h)
# >>> 

# >>> i = "Data" and "Science" and "AI"
# >>> print(i)
# >>> AI

# >>> j = "" and "" and ""
# >>> print(j)
# >>> 


# # 🟡List

# >>> a = [1,2] and [3,4]
# >>> print(a)
# >>> [3, 4]

# >>> b = [] and [5,6]
# >>> print(b)
# >>> []

# >>> c = [0] and []
# >>> print(c)
# >>> []

# >>> d = [] and []
# >>> print(d)
# >>> []

# >>> e = [1,2,3] and [4,5,6] and []
# >>> print(e)
# >>> []

# >>> f = [7] and [8] and [9]
# >>> print(f)
# >>> [9]

# >>> g = [] and [1,2,3]
# >>> print(g)
# >>> []

# >>> h = [0] and [0,1]
# >>> print(h)
# >>> [0, 1]

# >>> i = [1] and []
# >>> print(i)
# >>> []

# >>> j = [True] and [False] and [True]
# >>> print(j)
# >>> [True]


# # 🟡Tuple

# >>> a = (1,2) and (3,4)
# >>> print(a)
# >>> (3, 4)

# >>> b = () and (5,6)
# >>> print(b)
# >>> ()

# >>> c = (0,) and ()
# >>> print(c)
# >>> ()

# >>> d = () and ()
# >>> print(d)
# >>> ()

# >>> e = (1,2,3) and (4,5,6) and ()
# >>> print(e)
# >>> ()

# >>> f = (7,) and (8,) and (9,)
# >>> print(f)
# >>> (9,)

# >>> g = () and (1,2,3)
# >>> print(g)
# >>> ()

# >>> h = (0,) and (0,1)
# >>> print(h)
# >>> (0, 1)

# >>> i = (1,) and ()
# >>> print(i)
# >>> ()

# >>> j = (True,) and (False,) and (True,)
# >>> print(j)
# >>> (True,)


# # 🟡Set

# >>> a = {1,2} and {3,4}
# >>> print(a)
# >>> {3, 4}

# >>> b = set() and {5,6}
# >>> print(b)
# >>> set()

# >>> c = {0} and set()
# >>> print(c)
# >>> set()

# >>> d = set() and set()
# >>> print(d)
# >>> set()

# >>> e = {1,2,3} and {4,5,6} and set()
# >>> print(e)
# >>> set()

# >>> f = {7} and {8} and {9}
# >>> print(f)
# >>> {9}

# >>> g = set() and {1,2,3}
# >>> print(g)
# >>> set()

# >>> h = {0} and {0,1}
# >>> print(h)
# >>> {0, 1}

# >>> i = {1} and set()
# >>> print(i)
# >>> set()

# >>> j = {True} and {False} and {True}
# >>> print(j)
# >>> {True}

# ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖2️⃣>OR➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
# ‼️Basic Condition
# Operand 1 = True
# O/p = Operand 1
# Operand 1 = False
# O/p = Operand 2
# ‼️

# 🟡Basic

# >>> a = True or True
# >>> print(a)
# >>> True

# >>> b = True or False
# >>> print(b)
# >>> True

# >>> c = False or True
# >>> print(c)
# >>> True

# >>> d = False or False
# >>> print(d)
# >>> False

# >>> e = True or True or False
# >>> print(e)
# >>> True

# >>> f = True or True or True
# >>> print(f)
# >>> True

# >>> g = False or True or False
# >>> print(g)
# >>> True

# >>> h = True or False or False
# >>> print(h)
# >>> True

# >>> i = False or False or True
# >>> print(i)
# >>> True

# >>> j = False or False
# >>> print(j)
# >>> False


# # 🟡Complex

# >>> a = (1+0j) and (0+1j)
# >>> print(a)
# >>> (0+1j)

# >>> b = (0+0j) and (2+3j)
# >>> print(b)
# >>> 0j

# >>> c = (2+2j) and (3+3j)
# >>> print(c)
# >>> (3+3j)

# >>> d = (0+1j) and (0+0j)
# >>> print(d)
# >>> 0j

# >>> e = (1+1j) and (2+2j) and (0+1j)
# >>> print(e)
# >>> (0+1j)

# >>> f = (0+0j) and (1+2j) and (3+0j)
# >>> print(f)
# >>> 0j

# >>> g = (1+0j) and (1+0j)
# >>> print(g)
# >>> (1+0j)

# >>> h = (5+5j) and (0+0j)
# >>> print(h)
# >>> 0j

# >>> i = (0+0j) and (0+0j)
# >>> print(i)
# >>> 0j

# >>> j = (1+2j) and (3+4j)
# >>> print(j)
# >>> (3+4j)

# # 🟡String

# >>> a = "Hello" or "World"
# >>> print(a)
# >>> Hello

# >>> b = "" or "Python"
# >>> print(b)
# >>> Python

# >>> c = "Hi" or ""
# >>> print(c)
# >>> Hi

# >>> d = "" or ""
# >>> print(d)
# >>> 

# >>> e = "A" or "B" or "C"
# >>> print(e)
# >>> A

# >>> f = "" or "X" or "Y"
# >>> print(f)
# >>> X

# >>> g = "X" or "" or "Y"
# >>> print(g)
# >>> X

# >>> h = "Hi" or "Python" or ""
# >>> print(h)
# >>> Hi

# >>> i = "Data" or "Science" or "AI"
# >>> print(i)
# >>> Data

# >>> j = "" or "" or ""
# >>> print(j)
# >>> 


# # 🟡List

# >>> a = [1,2] or [3,4]
# >>> print(a)
# >>> [1, 2]

# >>> b = [] or [5,6]
# >>> print(b)
# >>> [5, 6]

# >>> c = [0] or []
# >>> print(c)
# >>> [0]

# >>> d = [] or []
# >>> print(d)
# >>> []

# >>> e = [1,2,3] or [4,5,6] or []
# >>> print(e)
# >>> [1, 2, 3]

# >>> f = [7] or [8] or [9]
# >>> print(f)
# >>> [7]

# >>> g = [] or [1,2,3]
# >>> print(g)
# >>> [1, 2, 3]

# >>> h = [0] or [0,1]
# >>> print(h)
# >>> [0]

# >>> i = [1] or []
# >>> print(i)
# >>> [1]

# >>> j = [True] or [False] or [True]
# >>> print(j)
# >>> [True]


# # 🟡Tuple

# >>> a = (1,2) or (3,4)
# >>> print(a)
# >>> (1, 2)

# >>> b = () or (5,6)
# >>> print(b)
# >>> (5, 6)

# >>> c = (0,) or ()
# >>> print(c)
# >>> (0,)

# >>> d = () or ()
# >>> print(d)
# >>> ()

# >>> e = (1,2,3) or (4,5,6) or ()
# >>> print(e)
# >>> (1, 2, 3)

# >>> f = (7,) or (8,) or (9,)
# >>> print(f)
# >>> (7,)

# >>> g = () or (1,2,3)
# >>> print(g)
# >>> (1, 2, 3)

# >>> h = (0,) or (0,1)
# >>> print(h)
# >>> (0,)

# >>> i = (1,) or ()
# >>> print(i)
# >>> (1,)

# >>> j = (True,) or (False,) or (True,)
# >>> print(j)
# >>> (True,)


# # 🟡Set

# >>> a = {1,2} or {3,4}
# >>> print(a)
# >>> {1, 2}

# >>> b = set() or {5,6}
# >>> print(b)
# >>> {5, 6}

# >>> c = {0} or set()
# >>> print(c)
# >>> {0}

# >>> d = set() or set()
# >>> print(d)
# >>> set()

# >>> e = {1,2,3} or {4,5,6} or set()
# >>> print(e)
# >>> {1, 2, 3}

# >>> f = {7} or {8} or {9}
# >>> print(f)
# >>> {7}

# >>> g = set() or {1,2,3}
# >>> print(g)
# >>> {1, 2, 3}

# >>> h = {0} or {0,1}
# >>> print(h)
# >>> {0}

# >>> i = {1} or set()
# >>> print(i)
# >>> {1}

# >>> j = {True} or {False} or {True}
# >>> print(j)
# >>> {True}

# ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖3️⃣>NOT➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
# ‼️Basic Condition
# Operand = True
# O/p = False
# Operand = False
# O/p = True
# ‼️

# 🟡Basic

# >>> a = not True
# >>> print(a)
# >>> False

# >>> b = not False
# >>> print(b)
# >>> True

# >>> c = not (5 > 3)
# >>> print(c)
# >>> False

# >>> d = not (2 == 2)
# >>> print(d)
# >>> False

# >>> e = not (10 < 5)
# >>> print(e)
# >>> True

# >>> f = not (0)
# >>> print(f)
# >>> True

# >>> g = not (1)
# >>> print(g)
# >>> False

# >>> h = not (True and False)
# >>> print(h)
# >>> True

# >>> i = not (False or True)
# >>> print(i)
# >>> False

# >>> j = not (3 != 3)
# >>> print(j)
# >>> True


# # 🟡Complex

# >>> a = not (0+0j)
# >>> print(a)
# >>> True

# >>> b = not (1+0j)
# >>> print(b)
# >>> False

# >>> c = not (0+1j)
# >>> print(c)
# >>> False

# >>> d = not (2+3j)
# >>> print(d)
# >>> False

# >>> e = not (0+0j) and (1+1j)
# >>> print(e)
# >>> True

# >>> f = not (3+4j)
# >>> print(f)
# >>> False

# >>> g = not (0+0j) or (2+2j)
# >>> print(g)
# >>> True

# >>> h = not (5+0j)
# >>> print(h)
# >>> False

# >>> i = not (0+0j)
# >>> print(i)
# >>> True

# >>> j = not (1+2j)
# >>> print(j)
# >>> False

# # 🟡String

# >>> a = not "Hello"
# >>> print(a)
# >>> False

# >>> b = not ""
# >>> print(b)
# >>> True

# >>> c = not "Python"
# >>> print(c)
# >>> False

# >>> d = not ""
# >>> print(d)
# >>> True

# >>> e = not "Hi" and not ""
# >>> print(e)
# >>> True

# >>> f = not "" or not "World"
# >>> print(f)
# >>> True

# >>> g = not "Data" and not "Science"
# >>> print(g)
# >>> False

# >>> h = not "" and not ""
# >>> print(h)
# >>> True

# >>> i = not "AI" or not ""
# >>> print(i)
# >>> True

# >>> j = not "X" and not "Y"
# >>> print(j)
# >>> False


# # 🟡List

# >>> a = not [1,2]
# >>> print(a)
# >>> False

# >>> b = not []
# >>> print(b)
# >>> True

# >>> c = not [0]
# >>> print(c)
# >>> False

# >>> d = not []
# >>> print(d)
# >>> True

# >>> e = not [1,2,3] and not []
# >>> print(e)
# >>> False

# >>> f = not [] or not [4,5]
# >>> print(f)
# >>> True

# >>> g = not [True] and not [False]
# >>> print(g)
# >>> False

# >>> h = not [] and not []
# >>> print(h)
# >>> True

# >>> i = not [0,1] or not []
# >>> print(i)
# >>> True

# >>> j = not [7,8] and not [9]
# >>> print(j)
# >>> False


# # 🟡Tuple

# >>> a = not (1,2)
# >>> print(a)
# >>> False

# >>> b = not ()
# >>> print(b)
# >>> True

# >>> c = not (0,)
# >>> print(c)
# >>> False

# >>> d = not ()
# >>> print(d)
# >>> True

# >>> e = not (1,2,3) and not ()
# >>> print(e)
# >>> False

# >>> f = not () or not (4,5)
# >>> print(f)
# >>> True

# >>> g = not (True,) and not (False,)
# >>> print(g)
# >>> False

# >>> h = not () and not ()
# >>> print(h)
# >>> True

# >>> i = not (0,1) or not ()
# >>> print(i)
# >>> True

# >>> j = not (7,8) and not (9,)
# >>> print(j)
# >>> False


# # 🟡Set

# >>> a = not {1,2}
# >>> print(a)
# >>> False

# >>> b = not set()
# >>> print(b)
# >>> True

# >>> c = not {0}
# >>> print(c)
# >>> False

# >>> d = not set()
# >>> print(d)
# >>> True

# >>> e = not {1,2,3} and not set()
# >>> print(e)
# >>> False

# >>> f = not set() or not {4,5}
# >>> print(f)
# >>> True

# >>> g = not {True} and not {False}
# >>> print(g)
# >>> False

# >>> h = not set() and not set()
# >>> print(h)
# >>> True

# >>> i = not {0,1} or not set()
# >>> print(i)
# >>> True

# >>> j = not {7,8} and not {9}
# >>> print(j)
# >>> False