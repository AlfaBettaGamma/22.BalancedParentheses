def recParentheses(N, paren=None):
  dstring = ''
  fstring = ''
  gstring = ''
  if N == 1:
    res = ['()']
    return res
  else:
      if paren == 1:
        return ["()" * N]
      else:
        if not paren:
          paren = N
        string = "".join(["(" * paren, ")" * paren ])
        if paren < N-1:
          dstring = string + "".join(["(" * (N-paren), ")" * (N-paren)]) + ' '
        if paren < N:
          dstring += '(' + '()'*paren + ')' + '()'*(N-paren-1)
          fstring = "()" * (N-paren) + string 
          string += "()" * (N-paren) 
          if paren == N//2:  
            gstring = '()'*(N-paren-1) + '(' + '()'*paren + ')' 
        return [string] + [fstring] + [dstring] + [gstring] + recParentheses(N, paren-1)

def BalancedParentheses(N):
  res = ''
  result = ''
  n = 0
  res = recParentheses(N, paren=None)
  n = res.count('')
  for i in range(n):
    res.remove('')
  for i in range(len(res)):
    if i == 0:
      result = result + res[i] + ' '
    elif i == len(res)-1:
      result = result + res[i]
    else:
      result = result + res[i] + ' '
  return result