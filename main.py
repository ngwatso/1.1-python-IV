def buyAndSellStock(prices):
    
    topProfit = 0
    
    for b in range(len(prices)-1):
        s = max(prices[(b+1):])
        if (s - prices[b]) > topProfit:
            topProfit = (s - prices[b])
        else:
            continue
    return topProfit
    
    # O(n^2)
                

'''

U:

[1, 4, 3, 7, 8]
output = 7

[5, 6, 2]
output = 0

[4, 10, 1, 6]
output = 6

P:

create 3 variables, buy and sell topProfit. iterate through the list with both vars, checking the difference and returning the maximum proffit

'''

# ======================================

def alphabeticShift(inputString):
    
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    newStr = ""
    
    for j in inputString:
        for i in range(len(alpha)):    
            if j == 'z':
                newStr += 'a'
                break
            elif j == alpha[i]:
                newStr += alpha[i + 1]
                break
                
    return newStr
    

'''

U:

"crazy"
output = "dsbaz"

'''

# ======================================

def validParenthesesSequence(s):
    
    count = 0
    
    for i in s:
        if s.index(i) == 0 and i != "(":
            return False
        elif i == "(":
            count += 1
        elif i == ")":
            count -= 1
            if count == -1:
                return False
            else:
                continue
    if count > 0:
        return False
    else:
        return True    

'''

U:

"()()(())"
output = True

"()()())"
output = False

P:

iterate through list, if "(", add 1 to count, if ")", subtract 1 from count.  If count becomes -1, return False.  If count is > 0 at end of sequence, return False.

'''