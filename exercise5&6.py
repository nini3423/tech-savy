def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

team = 'New England Patriots'
print (any_lowercase1(team))

#Returns false, this will only check for the first character of the string. If the first character is lowercase, despite of the other words, it will return true. 

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

team = 'Carrot'
print (any_lowercase2(team))
#Returns true, it checks if the string 'c' is lower case. If the '' is C then it would be False. 

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

team = 'Carrot'
print (any_lowercase3(team))
#flag indicate the function to be true when it could be false, lets the program know a certain condition of the function. 

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


#although it flags this function to be false in the beginning, because the string function is lowercase therefore with the "or" it would be false or true, hence true.

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
team = 'carrot'
print (any_lowercase5(team))

#This function checks for the first character. If the first letter is not lower then print false. 

#exercise 6

ord('c') - ord('a')

# encrypted_msg = "'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

encrypted_msg = 'map';

print('A', ord('A')) # 65
print('Z', ord('Z')) # 90
print('a', ord('a')) # 97
print('z', ord('z')) # 122

def rotate_word(encrypted_msg, delta):
  orginal_msg = ''
  for letter in encrypted_msg:
    if letter.isalpha():
      next_num = ord(letter) + delta

      if(next_num > ord('z')):
        next_num = ord('a') + (next_num - ord('a')) % 26
      elif(next_num > ord('Z')):
        next_num = ord('A') + (next_num - ord('A')) % 26
      # TODO: implement -delta situation

      decrpted_letter = chr(next_num)
    else:
      sdecrpted_letter = letter

    orginal_msg += decrpted_letter
  return orginal_msg

print(rotate_word(encrypted_msg, 2))
# print(decrypt('Y', 3))


