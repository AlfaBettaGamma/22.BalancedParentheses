def recParentheses(N, paren=None):
  if N == 1:
    res = ['()']
    return res
  else:
      if paren == 1:
        return ["()" * N]
      else:
        if not paren:
          paren = N
        string = "".join(["(" * paren, ")" * paren])
        if paren < N:
          string += "()" * (N-paren)
        return [string] + recParentheses(N, paren-1)

def BalancedParentheses(N):
  res = ''
  result = ''
  res = recParentheses(N, paren=None)
  for i in range(len(res)):
    if i == 0:
      result = '"' + result + res[i]+' '
    elif i == len(res)-1:
      result = result + res[i] + '"'
    else:
      result = result + res[i] +' '
  return result